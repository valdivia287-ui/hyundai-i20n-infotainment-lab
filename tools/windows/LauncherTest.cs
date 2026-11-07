using System;using System.Linq;using System.Diagnostics;using System.Drawing;using System.Drawing.Imaging;using System.Runtime.InteropServices;using System.Text;using System.Windows.Automation;
class LauncherTest {
 [StructLayout(LayoutKind.Sequential)] public struct Rect {public int Left,Top,Right,Bottom;}
 [DllImport("user32.dll")] static extern bool SetProcessDPIAware();
 [DllImport("user32.dll")] static extern bool GetWindowRect(IntPtr h,out Rect r);
 [DllImport("user32.dll")] static extern bool PrintWindow(IntPtr h,IntPtr dc,uint flags);
 static void Main(string[] args){SetProcessDPIAware();Console.OutputEncoding=Encoding.UTF8;
  var ps=Process.GetProcessesByName("Hyundai-i20N-Lab").Where(candidate=>candidate.MainWindowHandle!=IntPtr.Zero).ToArray();if(ps.Length!=1)throw new Exception("Se esperaba una ventana del lanzador");var p=ps[0];var w=AutomationElement.FromHandle(p.MainWindowHandle);string action=args.Length>0?args[0]:"Inspect";
  if(action=="Start"||action=="Stop"||action=="Log"){string name=action=="Start"?"Iniciar multimedia":action=="Stop"?"Detener":"Último registro";var b=w.FindFirst(TreeScope.Descendants,new PropertyCondition(AutomationElement.NameProperty,name));if(b==null||!b.Current.IsEnabled)throw new Exception("Botón no disponible");((InvokePattern)b.GetCurrentPattern(InvokePattern.Pattern)).Invoke();}
  if(action=="Close"){((WindowPattern)w.GetCurrentPattern(WindowPattern.Pattern)).Close();}
  if(action=="Duplicate"){using(var next=Process.Start(p.MainModule.FileName)){if(!next.WaitForExit(10000))throw new Exception("La segunda instancia no se cerró");}}
  if(action=="Capture"){Rect r;GetWindowRect(p.MainWindowHandle,out r);using(var bmp=new Bitmap(r.Right-r.Left,r.Bottom-r.Top)){using(var g=Graphics.FromImage(bmp)){IntPtr dc=g.GetHdc();try{if(!PrintWindow(p.MainWindowHandle,dc,2))throw new Exception("Captura fallida");}finally{g.ReleaseHdc(dc);}}bmp.Save(args[1],ImageFormat.Png);}}
  Console.WriteLine("{\"action\":\""+action+"\",\"pid\":"+p.Id+",\"window_count\":"+Process.GetProcessesByName("Hyundai-i20N-Lab").Count(x=>x.MainWindowHandle!=IntPtr.Zero)+",\"utc\":\""+DateTime.UtcNow.ToString("o")+"\"}");
 }
}
