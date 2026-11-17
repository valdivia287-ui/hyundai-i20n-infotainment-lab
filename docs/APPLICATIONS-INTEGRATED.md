# Disponibilidad de aplicaciones

**Vigente a 18 noviembre 2026.** Dos niveles separados: el **producto aceptado** (lanzador Windows v1, tabla de abajo, sin cambios) y los **resultados de desarrollo**, comprobados en overlays aparte y **no** integrados en el producto. Los avisos acumulados anteriores están en [history/APPLICATIONS-INTEGRATED-to-2026-11-08.md](history/APPLICATIONS-INTEGRATED-to-2026-11-08.md). Estado general: [STATUS.md](STATUS.md).

## Desarrollo (no promovido)

| Aplicación/vista | Resultado en desarrollo | Límite | Informe |
| --- | --- | --- | --- |
| Ajustes: General, Teclado, Pantalla | Páginas originales en español y retorno nativo a Home | Recursos y latencia | [General](PROGRESS-2026-11-08-SETTINGS-GENERAL-SPANISH.md) |
| Ajustes: Tema, Botón N, Perfil | Páginas internas, entrada real y Home; sin cambiar preferencias | — | [Categorías](PROGRESS-2026-11-08-SETTINGS-CATEGORIES-ASTC.md) |
| Ajustes: Conexión Bluetooth53, Android Auto, Apple CarPlay | UI española, Atrás/Home, ilustración original por CPU | Sin teléfono ni proyección real | [Bluetooth](PROGRESS-2026-11-08-BLUETOOTH-SETTINGS.md) |
| Ajustes: Sonido50 y Ecualizador | Contenido y arte completos en español, navegación interna, Home | Cabeceras de Posición/Guía incompletas; audio/DSP sin verificar | [Sonido](PROGRESS-2026-11-08-SETTINGS-ORDER-SOUND.md) |
| Nota de voz117 | Lista vacía en español, Atrás/Home | Sin grabación ni reproducción | [Categorías](PROGRESS-2026-11-08-SETTINGS-CATEGORIES-ASTC.md) |
| Reloj (TimeManager original) | Hora/fecha reales de la VM en Home | Solo UTC; Madrid/DST pendiente | [Reloj](PROGRESS-2026-11-08-ORIGINAL-CLOCK.md) |
| Medios / AppMediaPlayer (100) | Petición real 304/2/27→302/0/308; con proveedor original `mediaCount=1` | Sin interfaz nueva | [Estado](STATUS.md#pending-in-suggested-order) |
| Teléfono (121) | Abierto como primera vista del proceso compartido; llega al flujo original de añadir dispositivo | Sin Bluetooth, emparejamiento ni llamadas | [Cobertura 17/11](PROGRESS-2026-11-17-INTERACTIVE-LAB.md) |
| Tema/disposición (480) | Pantalla original, navegación a Ventana partida y retorno a Home | No se cambiaron preferencias | [Cobertura 15/11](PROGRESS-2026-11-15-FUNCTIONAL-COVERAGE.md) |
| Teclado/búsqueda (460) | Entrada y borrado de texto, resultados filtrados y retorno a Home | Solo menús instalados localmente | [Cobertura 15/11](PROGRESS-2026-11-15-FUNCTIONAL-COVERAGE.md) |
| Ajustes del vehículo (61) | Asistencia al conductor y Aparcamiento de seguridad, navegación interna y Home | Requiere fixture privado de contacto ON; sin otras señales del coche | [Cobertura 15/11](PROGRESS-2026-11-15-FUNCTIONAL-COVERAGE.md) |
| Modo silencioso (368) | Interruptor original activado/desactivado y retorno a Home | Sin comprobar audio ni ocupantes físicos | [Cobertura 15/11](PROGRESS-2026-11-15-FUNCTIONAL-COVERAGE.md) |
| Hyundai LIVE (450) | Menú original y aviso correcto de navegación no disponible | Sin red, navegación ni servicios Hyundai | [Cobertura 15/11](PROGRESS-2026-11-15-FUNCTIONAL-COVERAGE.md) |
| Climatización (13) | UI original OFF/sin datos y retorno a Home | Sin CAN; control probado sin cambio visible | [Cobertura 15/11](PROGRESS-2026-11-15-FUNCTIONAL-COVERAGE.md) |
| Perfil (362) | Página Invitado aceptada y retorno a Home | Selector Driver 1/2 no fiable y dependiente de servicios de cuenta; no se creó perfil | [Cobertura 17/11](PROGRESS-2026-11-17-INTERACTIVE-LAB.md) |
| Valet (29) | Teclado original acepta un PIN de prueba dos veces y muestra «Modo aparcacoches en uso.» | Persistencia y salida no demostradas; falta respuesta del vehículo | [Cobertura 17/11](PROGRESS-2026-11-17-INTERACTIVE-LAB.md) |
| Engineering Mode (301) | Pantalla original de introducción de contraseña dibujada | No se introdujo contraseña ni se pulsó ningún control de diagnóstico, escritura o reset | [Cobertura 17/11](PROGRESS-2026-11-17-INTERACTIVE-LAB.md) |
| Radio DAB/FM (77) | Pantalla, Lista DAB/FM y selector aceptados en repetición; retorno a Home sin core observado | Sin sintonizador RF, emisoras ni audio | [Cobertura 17/11](PROGRESS-2026-11-17-INTERACTIVE-LAB.md) |
| Bluelink/TMS (203/227) | Provisión, información de módem, código de verificación, ayuda y avisos dibujan | IMEI/VIN/códigos vacíos o a cero; sin módem, cuenta ni servicio Hyundai | [Cobertura 17/11](PROGRESS-2026-11-17-INTERACTIVE-LAB.md) |
| Laboratorio interactivo privado | Sesión integrada persistente con abrir/Home/captura/estado/parada y visor local | No distribuido; arranque 2–6 min; la rueda se bloquea para mitigar un crash de Weston | [Cobertura 17/11](PROGRESS-2026-11-17-INTERACTIVE-LAB.md) |

La combinación de proveedores (reloj + Bluetooth + Ajustes en un mismo arranque) sigue mostrando un bloqueo inicial de General; no se integra hasta aislar el orden de arranque.

## Producto aceptado v1 (congelado, 7 noviembre)

Resultados del perfil BC3N25MY, offline, con país Europa y español EU. La tabla diferencia vistas lógicas del mismo Home y ejecutables independientes. Los resultados previos de perfiles separados se conservan y no se extrapolan.

| Aplicación/vista | Estado integrado | Resultado y límite |
| --- | --- | --- |
| Home (11) | Navegable | Pantalla original completa, arrastre y menús por ratón; alguna textura fuera del conjunto observado sigue ausente. |
| N Mode (500) | Navegable | Vista original Track dentro de Home, ceros/OFF nativos, entrada y vuelta a Home. No telemetría ni cambios del vehículo. |
| Manual | Navegable | Vista original española dentro de Home, QR/texto y Atrás. No se abrió el enlace web ni se afirma manual completo offline. |
| Radio (77) | Navegable (UI) | FM original visible, 0.0 MHz/sin sintonizador. Regreso con el botón Home tras dibujo completo comprobado en las sesiones integradas. Otro recorrido dejó Home sin buffer; no se generaliza a todas las secuencias. No audio/RF probado. |
| Ajustes / AppSetup (60) | Parcial | Raíz de Home visible; proveedor original registrado, superficie oculta/sin buffer y posterior terminación ordenada por AppManager. Sonido no mostró contenido. |
| Medios / AppMediaPlayer (100) | Parcial | Proveedor original vivo/registrado con runtime OEM TSE verificado; el icono no mostró interfaz nueva. No fuentes conectadas. |
| Nota de voz (117) | Parcial | El perfil anterior sí mostró la lista vacía; el integrado 81/high1 no mostró contenido. No micrófono/grabación. |
| Teléfono (121) | Sin hardware | Sin Bluetooth/smartphone; no se repitió su inicialización fallida anterior. No se atribuye todo su fallo al hardware sin evidencia. |
| Proyección | Sin hardware | Sin smartphone. El clic no abrió otra UI; no se inventa un popup ni una conexión. |
| Climatización (13) | Ausente | Ejecutable ausente en la base inspeccionada; un icono no demuestra aplicación disponible. Tampoco hay climatizador físico. |
| Modo silencioso | Sin hardware | No accionado: sin altavoces/ocupantes reales. |
| Navegación (30) | Ausente | Ejecutable ausente en el montaje actual. Recuperación del host separada; mapas, licencias y montaje por verificar. |
| Actualización / flasheo / ingeniería / diagnóstico / eCall | Excluida por seguridad | No se ejecutan. Los servicios internos no se cuentan como aplicaciones gráficas. |

El arranque opcional de proveedores de Ajustes/Medios coincidió con textos cambiados a inglés pese a argumentos `-l:7`. La causa exacta no está aislada; estos proveedores no se precargan en el perfil de uso del propietario. La VM/overlay experimental es independiente y conserva evidencias privadas.

El inventario estático completo contiene 35 entradas Launcher y 154 entradas lógicas del gestor; **no equivalen a 189 aplicaciones independientes ni verificadas**. La ronda integrada recorre varios iconos consecutivamente en una sola VM y continúa cuando uno falla. No promete navegación, audio, servicios móviles ni el sistema completo. [Lanzador Windows](WINDOWS-LAUNCHER.md) · [Evidencia integrada](PROGRESS-2026-11-07-WINDOWS-PRODUCT.md).
