# Lanzador Windows del laboratorio

El frontend propio `tools/windows/HyundaiLauncher.cs` se compila como `Hyundai-i20N-Lab.exe`. Abre una ventana en castellano con **Iniciar multimedia**, **Detener**, **Abrir visor** y **Último registro**. Al abrirla inicia el perfil integrado `multimedia`; el navegador se abre cuando el controlador confirma Home original visible y alineado.

Este repositorio distribuye el frontend y documentación. No incluye el runtime privado, firmware, imágenes base, recursos decodificados ni una máquina virtual preparada. Descargar o compilar el frontend por sí solo no instala el emulador. Cada usuario debe obtener independientemente el firmware compatible desde [Hyundai Navigation Update](https://update.hyundai.com/EU/ES/home), con [búsqueda oficial](https://update.hyundai.com/EU/ES/search). El objetivo del laboratorio es BC3N Gen5W_L Europa/España; no se distribuyen mapas ni licencias.

## Compilación e instalación en un laboratorio existente

1. Copiar `HyundaiLauncher.cs` y `build.cmd` a una carpeta Windows independiente.
2. Copiar `launcher-config.example.json` como `launcher-config.json` y configurar la distribución WSL y la ruta Linux del laboratorio. La ruta actual debe ser absoluta, sin espacios ni metacaracteres; el programa rechaza configuraciones no admitidas.
3. Ejecutar `build.cmd` con el compilador .NET Framework existente. No cambia ExecutionPolicy, firewall ni seguridad del sistema.
4. Crear un acceso directo al ejecutable. No hay instalación global ni reinstalación automática de scripts antiguos.

## Contrato con el controlador local

El frontend ejecuta `wsl.exe --distribution DISTRO --exec /usr/bin/python3 LAB/host/windows-session.py` con una de estas órdenes:

| Orden | Resultado requerido |
| --- | --- |
| `start --profile multimedia` | Inicia una sola VM, con overlay nuevo; rechaza otra sesión activa. Devuelve pronto, sin esperar al arranque gráfico. |
| `status --json` | JSON con `status`, `active`, `run_id`, `message`, `log`, `viewer`. Estados: detenido/arrancando/listo/error. Solo da listo después de comprobar la interfaz original. |
| `stop` | Solicita apagado al único controlador propietario, espera salida y guarda evidencias; nunca adopta una VM ajena. |
| `log` | Últimas líneas del registro propio, sin ejecutar órdenes del usuario. |

La exclusión de instancias Windows usa un mutex de usuario. El backend privado añade bloqueo WSL y validación PID/tiempo de nacimiento/identificador de sesión. El visor se conecta por loopback con un identificador de sesión y se habilita solo tras la entrega real del control. La VM usa `-nic none`. Una ventana antigua del navegador no controla una sesión nueva.

**Detener** conserva el overlay de esa sesión para diagnóstico; el siguiente arranque crea otro. La sesión integrada tiene un límite explícito de cuatro horas, no un ensayo obligatorio de diez minutos. El arranque medido tarda varios minutos y algunas transiciones son lentas bajo QEMU TCG/software; evitar pulsaciones repetidas durante una transición. El ratón no requiere comandos Linux.

## Validación desde Windows

`LauncherTest.cs` es una herramienta propia de UIAutomation para la ventana del lanzador. `Start` y `Stop` invocan los botones reales; `Duplicate` comprueba que una segunda instancia se cierra y queda una sola ventana. No sustituye la comprobación visual de la HMI, ni prueba por sí sola que una aplicación OEM sea navegable. No necesita cambiar políticas de PowerShell. Las capturas o registros privados no forman parte del repositorio.

Ver el progreso integrado y los límites en [el informe del producto](PROGRESS-2026-11-07-WINDOWS-PRODUCT.md).

`build-test.cmd` compila el comprobador de los botones. `build-browser-test.cmd` compila `BrowserMouse.cs`: solo usarlo sobre la sesión propia ya preparada, sin otro operador. Comprueba ventana/documento noVNC y foco antes de enviar un único arrastre por la franja inferior; no arranca/apaga VM ni abre serial. Los ejecutables de diagnóstico no forman parte del lanzador del propietario.

La prueba offline se ejecuta con `python3 tools/verify_product_delivery.py /ruta/a/run/privado/finalizado`. Necesita Pillow y las referencias privadas; no publica esos datos. Su alcance es la evidencia registrada, no una certificación del firmware ni del emulador completo.
