// Original laboratory launcher. Contains no OEM software or resources.
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using System.Web.Script.Serialization;
using System.Windows.Forms;

public sealed class HyundaiLauncher : Form {
    readonly Button start = new Button(), stop = new Button(), viewer = new Button(), logs = new Button();
    readonly Label status = new Label(), detail = new Label();
    readonly System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();
    readonly string folder = AppDomain.CurrentDomain.BaseDirectory;
    readonly JavaScriptSerializer json = new JavaScriptSerializer();
    string distro, root, openedRun = "", lastRun = "";
    bool busy, polling, active, closing, forceClose; string lastError="";
    [DllImport("user32.dll")] static extern bool SetForegroundWindow(IntPtr handle);
    [DllImport("user32.dll")] static extern bool ShowWindow(IntPtr handle, int value);

    public HyundaiLauncher() {
        var config = json.Deserialize<Dictionary<string,object>>(File.ReadAllText(Path.Combine(folder,"launcher-config.json")));
        distro = Convert.ToString(config["distribution"]); root = Convert.ToString(config["labRoot"]);
        if (!Regex.IsMatch(distro,@"^[A-Za-z0-9_.-]+$") || !Regex.IsMatch(root,@"^/[A-Za-z0-9_./-]+$")) throw new Exception("Configuración del laboratorio no válida.");
        Text = "Hyundai i20 N · Multimedia original"; Size = new Size(690,340); MinimumSize = Size;
        StartPosition = FormStartPosition.CenterScreen; Font = new Font("Segoe UI",10); BackColor=Color.FromArgb(241,245,249);
        var title = new Label { Text="Hyundai i20 N · Laboratorio", Font=new Font("Segoe UI",18,FontStyle.Bold), AutoSize=true, Location=new Point(25,20) };
        status.SetBounds(27,65,610,32); status.Font = new Font("Segoe UI",15,FontStyle.Bold);
        detail.SetBounds(28,104,610,65); detail.Text="Preparando el multimedia original…";
        start.Text="Iniciar multimedia"; stop.Text="Detener"; viewer.Text="Abrir visor"; logs.Text="Último registro";
        Button[] buttons={start,stop,viewer,logs};
        for(int i=0;i<buttons.Length;i++){buttons[i].SetBounds(25+i*158,185,150,45); Controls.Add(buttons[i]);}
        var note = new Label {Text="Perfil BC3N25MY · Español · Sin conexión al vehículo",AutoSize=true,Location=new Point(27,253),ForeColor=Color.DimGray};
        Controls.AddRange(new Control[]{title,status,detail,note});
        start.Click += async (s,e)=>await StartMultimedia(); stop.Click += async (s,e)=>await StopMultimedia();
        viewer.Click += (s,e)=>OpenViewer(); logs.Click += async(s,e)=>await OpenLog();
        timer.Interval=2500; timer.Tick += async(s,e)=>await Poll();
        Shown += async(s,e)=>{timer.Start(); Event("ventana_abierta"); await StartMultimedia();};
        FormClosing += async(s,e)=>{
            if(forceClose)return; e.Cancel=true; if(closing)return; closing=true; timer.Stop();
            while(busy)await Task.Delay(300);
            await StopMultimedia();
            if(!active){forceClose=true;Close();}else{closing=false;timer.Start();}
        };
        SetStatus("detenido","Preparado para iniciar.");
    }
    void Event(string text) { try { lock(folder) File.AppendAllText(Path.Combine(folder,"launcher-events.log"),DateTime.UtcNow.ToString("o")+" "+text+Environment.NewLine,Encoding.UTF8); }catch{} }
    void SetStatus(string value,string message) {
        status.Text= value=="listo"?"Listo":value=="arrancando"?"Arrancando…":value=="error"?"Error":"Detenido";
        status.ForeColor=value=="listo"?Color.DarkGreen:value=="error"?Color.Firebrick:value=="arrancando"?Color.DarkGoldenrod:Color.FromArgb(40,55,70);
        detail.Text=message; start.Enabled=!busy&&!active; stop.Enabled=!busy&&active; viewer.Enabled=active;
        try {
            string content=json.Serialize(new{status=value,message=message,active=active,run_id=lastRun,pid=Process.GetCurrentProcess().Id,window_handle=Handle.ToInt64(),utc=DateTime.UtcNow.ToString("o")});
            string path=Path.Combine(folder,"launcher-status.json"),tmp=path+".tmp";File.WriteAllText(tmp,content,Encoding.UTF8);
            if(File.Exists(path))File.Replace(tmp,path,null);else File.Move(tmp,path);
        }catch{}
    }
    Task<string> Wsl(params string[] action) {
        return Task.Factory.StartNew(()=>{
            var parts=new List<string>{"--distribution",distro,"--exec","/usr/bin/python3",root+"/host/windows-session.py"};parts.AddRange(action);
            var quoted=new List<string>();foreach(var part in parts){if(part.Contains("\"")||part.Contains("\n"))throw new Exception("Argumento no válido.");quoted.Add(part);}
            var info=new ProcessStartInfo(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.System),"wsl.exe"),String.Join(" ",quoted.ToArray())) {UseShellExecute=false,CreateNoWindow=true,RedirectStandardOutput=true,RedirectStandardError=true,StandardOutputEncoding=Encoding.UTF8,StandardErrorEncoding=Encoding.UTF8};
            using(var process=Process.Start(info)){
                Task<string> output=process.StandardOutput.ReadToEndAsync(),error=process.StandardError.ReadToEndAsync();
                if(!process.WaitForExit(110000))throw new Exception("WSL tarda demasiado en responder. Consulte el último registro; la VM no se cierra a la fuerza.");
                Task.WaitAll(output,error);if(process.ExitCode!=0)throw new Exception((output.Result+" "+error.Result).Trim());return output.Result;
            }
        });
    }
    async Task StartMultimedia(){
        if(busy)return;busy=true;lastError="";SetStatus("arrancando","Arrancando WSL y el multimedia. Home aparecerá al completar el inicio.");Event("boton_iniciar");
        try{Event((await Wsl("start","--profile","multimedia")).Trim());active=true;}
        catch(Exception e){Event("error_inicio "+e.Message);lastError="No se pudo iniciar el multimedia. Pulse Último registro para ver el motivo.";SetStatus("error",lastError);}
        finally{busy=false;} await Poll();
    }
    async Task StopMultimedia(){
        if(busy)return;busy=true;SetStatus("arrancando","Apagando la máquina virtual y guardando los registros…");Event("boton_detener");
        try{Event((await Wsl("stop")).Trim());active=false;lastError="";SetStatus("detenido","Multimedia apagado. El próximo inicio creará un overlay nuevo.");}
        catch(Exception e){Event("error_parada "+e.Message);SetStatus("error",e.Message);}
        finally{busy=false;} if(!closing)await Poll();
    }
    async Task Poll(){
        if(polling||busy)return;polling=true;
        try{
            var data=json.Deserialize<Dictionary<string,object>>(await Wsl("status","--json"));active=Convert.ToBoolean(data["active"]);lastRun=Convert.ToString(data["run_id"]);
            string value=Convert.ToString(data["status"]),message=Convert.ToString(data["message"]);
            if(value=="arrancando")message="Arrancando el multimedia original. El visor se abrirá cuando Home esté listo.";
            if(value=="detenido"&&lastError!=""){value="error";message=lastError;}
            if(value=="detenido")message="Multimedia apagado. Pulse Iniciar multimedia para abrir una sesión limpia.";
            SetStatus(value,message);
            if(value=="listo"&&openedRun!=lastRun){openedRun=lastRun;OpenViewer();Event("home_listo_visor_abierto "+lastRun);}
        }catch(Exception e){SetStatus("error","No se puede consultar WSL. Use Último registro.");Event("error_estado "+e.Message);}finally{polling=false;}
    }
    void OpenViewer(){try{Process.Start(new ProcessStartInfo("http://127.0.0.1:6080/laboratorio"){UseShellExecute=true});}catch(Exception e){Event("error_visor "+e.Message);SetStatus("error","No se pudo abrir el navegador. Use Abrir visor.");}}
    async Task OpenLog(){
        string path=Path.Combine(folder,"ultimo-registro.txt");try{File.WriteAllText(path,await Wsl("log"),Encoding.UTF8);}catch{path=Path.Combine(folder,"launcher-events.log");}
        try{Process.Start(new ProcessStartInfo("notepad.exe","\""+path+"\""){UseShellExecute=false});}catch(Exception e){Event(e.Message);}
    }
    [STAThread] public static void Main(){
        bool created;using(var mutex=new Mutex(true,@"Local\Hyundai-i20N-Lab-Launcher",out created)){
            if(!created){foreach(var p in Process.GetProcessesByName("Hyundai-i20N-Lab")){if(p.MainWindowHandle!=IntPtr.Zero){ShowWindow(p.MainWindowHandle,9);SetForegroundWindow(p.MainWindowHandle);break;}}return;}
            Application.EnableVisualStyles();Application.SetCompatibleTextRenderingDefault(false);
            try{Application.Run(new HyundaiLauncher());}catch(Exception e){MessageBox.Show(e.Message,"No se pudo abrir Hyundai i20 N Lab",MessageBoxButtons.OK,MessageBoxIcon.Error);}
        }
    }
}
