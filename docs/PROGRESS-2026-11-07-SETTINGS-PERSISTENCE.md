# Ajustes: persistencia original y contenido nuevo en desarrollo

El lanzador Windows v1 aceptado se conserva sin cambios. Esta investigación usa un directorio de desarrollo, un único QEMU sin red y overlays independientes. No representa todavía una aplicación nueva entregada al propietario.

## Comprobado

- AppSetup original se inicia mediante la API real de AppLauncher (proveedor 60). Sonido es la aplicación lógica 50.
- Con la persistencia ausente, Peer.Ping real devuelve NoReply. El hilo principal capturado duerme en nanosleep mientras la traza repite accesos fallidos al lock y a las tablas de recursos. Crear únicamente el directorio permite progresar parcialmente, pero no muestra contenido ni evita que el gestor termine el proveedor.
- El fstab original usa una partición de datos bajo dos rutas: `/Data/mnt-c` y `/Data/mnt-wt`. Un bind temporal reproduce ese alias dentro del overlay, sin tocar el almacenamiento del coche.
- El daemon original `pers_admin_svc`, su configuración original de instalación y el paquete original de defaults permiten inicializar las tablas. No se han creado respuestas D-Bus ni tablas de configuración falsas, y no se han ejecutado actualizadores, reset ni herramientas de diagnóstico.
- En el ensayo con ese arranque, Peer.Ping respondió de forma consecutiva y **AppSetup mostró Sonido y Ecualizador originales**. El ratón seleccionó la página interna Ecualizador. Se observaron valores originales a cero; no se cambiaron parámetros de audio ni se atribuye funcionalidad al hardware ausente.

## Pendiente antes de integrar

La superficie conservaba un destino de 1920×720 sobre una salida de 1280×800 y quedaba recortada. Un overlay posterior verifica una adaptación propia del destino a 1280×730, condicionada al propietario AppSetup, su capa activa y tres getters originales concordantes. Ecualizador se muestra completo y responde a la selección con ratón. No se modifica el QML de AppSetup.

El primer ensayo con contenido terminó por su límite programado y rechazó el clic de retorno por proximidad al cierre. En el overlay posterior, **el botón Home original sí devolvió a Home completo y alineado**: los tres getters originales regresaron a11, la superficie de Home volvió a tener buffer y AppSetup quedó oculto. Otro clic real abrió de nuevo Ajustes desde Home. Las transiciones aún tardan decenas de segundos. Esto acredita el recorrido de desarrollo; falta resolver idioma y recursos antes de promoverlo al producto. No confundir los cierres programados con fallos espontáneos de Home.

AppSetup emite `NotifyLanguageChanged(3)` durante la inicialización y hace pasar textos a inglés. Debe conservarse español mediante su mecanismo original antes de la promoción. La traza completa amplía el inventario a 43 recursos realmente solicitados: 39 se han decodificado con hashes y roundtrip de píxeles; cuatro payloads recuperados están vacíos y se excluyen sin reconstrucción. Este conjunto todavía no se ha instalado ni validado en una VM. No se publican texturas ni capturas recortadas o incompletas.

## Adaptaciones y límites de procedencia

La configuración aceptada de Home conserva un override QML heredado que intenta fijar `vehicleVariant` a 23. Las descripciones anteriores generales de «sin modificaciones QML» deben entenderse con este matiz. Esto no es una corrección nueva de Ajustes: su QML se mantiene original. La selección nativa de argumentos 81/high1/pf1/nm2 y la ausencia de los adaptadores N de capacidad/argv son comprobaciones diferentes.

Se conserva la separación entre coche físico MY23 España/Europa con software actualizado en 2025 y perfil de software experimental BC3N25MY preferido por el propietario. No se ha validado la disponibilidad de todas las opciones físicas que el menú de ajustes pueda enumerar.

## Medios y siguientes pruebas

En la misma sesión se inició AppMediaPlayer original con sus argumentos BC3N25MY y el enlace temporal verificado a su biblioteca OEM. Se observó su superficie registrada sin buffer. El clic de Nota de voz ocurrió antes de que Home completara el dibujo: el ensayo es inconcluso y no demuestra un bloqueo del proveedor. La siguiente prueba debe esperar la imagen completa antes de la entrada, y limitarse al primer fallo real. No se probó grabación ni se inventaron dispositivos.

## Código compartido

`tools/guest/prepare_oem_persistence.sh` es código propio experimental. Exige marcadores del laboratorio, arranque virtual por vda, fingerprints del daemon/paquete y rutas de datos conocidas. Rechaza contenido inesperado y conserva el enlace heredado al cubrirlo mediante bind. Solo inicia el daemon normal en el overlay; no incluye binarios, defaults, RCT ni datos OEM. El límite de 1200 s corresponde a este desarrollo y debe ajustarse explícitamente antes de una integración duradera.

El firmware debe obtenerse independientemente del [portal oficial Hyundai](https://update.hyundai.com/EU/ES/home), para la unidad compatible. No se publica contenido propietario, mapas, licencias, trazas, cores ni imágenes de VM.
