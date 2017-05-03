# Actividades evaluativas

Según las actividades de la programación académica general es posible que se incluya en sus actividades evaluativas a modo de bonificación la entrega de un trabajo sobre un congreso de ciencias básicas.  

## Cuestionario UVirtual

Posee intentos ilimitados separados por 3 horas y de duración 50 minutos para la solución del cuestionario de taller 1, conservando la nota del más alto. Esta actividad es de carácter individual.  

El cuestionario posee 5 preguntas abiertas de respuesta numérica (con tolerancia para respuestas decimales) o texto (para algunas respuestas especiales como la indicación del infinito o de no aplicar). La mayor parte de preguntas no dan ponderación intermedia (es buena o mala la respuesta).  

Para las respuestas numéricas, tenga en cuenta que la plataforma fuerza el uso del separador decimal `,`, de forma que la respuesta con el `.` no se acepta. Tenga presente la indicación de tolerancia dada en cada pregunta (puede ser dada como cifras decimales o como cifras significativas), ya que una cantidad mal aproximada representará una respuesta completamente errónea. Use además solo el valor numérico sin indicación de unidades (use siempre la cantidad en S.I. o en las unidades indicadas por el problema).  

Si requiere de revisión de su respuesta, no solo marque la pregunta sino que además notifique al docente por correo (de la plataforma) justificando el motivo de revisión. La revisión solo se hará si la justificación es adecuada.  

## Escritas

Las actividades escritas son los quices, parcial, final y taller 2. Todas estas comparten las siguientes normas de presentación.

### Marcación

La marcación incorrecta de su nombre en la actividad evaluativa representa que no fue participe de la misma, y será equivalente no solo a perder la actividad sino a no asistir a la sesión correspondiente. La responsabilidad de la marcación de su nombre es propia. Indique también el grupo, hora y fecha de la actividad.  

### Ortografía

Haga uso de una adecuada ortografía y gramática en sus informes. Esto ayudará a transmitir adecuadamente sus ideas y no generar malinterpretaciones o sentidos ambiguos sobre su concepto en la actividad.  

Su actividad tendrá una ponderación sobre este aspecto según afecte la legibilidad de la misma.  

Tenga en cuentas las [tildes en mayúsculas](http://www.rae.es/consultas/tilde-en-las-mayusculas "Tilde en las mayúsculas. Real Academia Española. Consultado el 19 de febrero de 2017."), las cuales también se marcan acorde a las reglas de la ortografía española. Históricamente estas no se marcaban usualmente ante la dificultad de la marcación de acentos en las máquinas de escribir, problema solucionado en la era digital.  

### Escribir matemáticas

Puede usar tanto `.` como `,` de separador decimal, siempre que sea consistente. Eso quiere decir que una vez usado uno de ellos, este sigue siendo el separador decimal en toda la entrega. La aparición del separador contrario implica un valor inexistente y por ende lleva a la presencia de valores no justificados que se deriven del valor inconsistente (para efectos prácticos, no presento la solución).  

Debe tener consistencia simbólica, lo cual quiere decir que una vez asignado un símbolo este sigue con el mismo significado en todo el desarrollo. Por ejemplo, si la masa de un cuerpo dado fue definida como $m$, ya no podrá ser definida como $M$ más adelante, pues son símbolos diferentes. Tenga en cuenta el estilo, pues el cambio de estilo representa un símbolo diferente, como se ilustra a continuación:  
>>$M = \mathit{M} \neq \mathbf{M} \neq \mathrm{M} \neq \mathcal{M} \neq \boldsymbol{M}\neq m$.  

Recuerde que la negrilla corresponde a vectores.  

>>$\boldsymbol{v}\equiv\vec{v}$

Recuerde que al escribir una expresión matemática, debe considerar la jerarquía de operadores. Eso quiere decir que existe una convención sobre el orden de las operaciones y que en caso de que deba realizarse en otro orden debe usar elementos de agrupación de forma adecuada.  

>>$4 + 5 \cdot 3 \neq (4+5)\cdot3$

Esto mismo es válido para las unidades físicas, ya que estas son elementos algebraicos (todo valor numérico que sea una cantidad con unidades, debe tenerlas registradas).  

>>$4 + 5\ \mathrm{m} \neq (4+5)\ \mathrm{m}$

Un paréntesis o cualquier tipo de agrupamiento (las divisiones con barra horizontal y las raíces entre otras) deben cubrir completamente la expresión matemática.  

+   $(\frac{3}{4})$: Erróneo.  
+   $\left(\frac{3}{4}\right.$: Erróneo.  
+   $\left(\frac{3}{4}\right)$: Correcto.  

Tenga en cuenta que en el álgebra los símbolos consecutivos representan un producto. Por lo mismo, la indicación de una minúscula no es equivalente a un subíndice (usado para distinguir entre símbolos que inician igual).  

$V_a \neq Va$. $V_a$ indica que hay un caso particular $a$ de $V$, mientras que $va$ es equivalente a $V\cdot a$.  

Los símbolos de los operadores cumplen reglas también, siendo particular recordar que el símbolo `*` no se puede usar como producto. Formas posibles de producto son:  

+   $2\times 3$: Las lineas son perfectamente rectas y perpendiculares. Si son vectores es el producto cruz.  
+   $2\cdot 3$: El punto va a mitad de renglón. Si son vectores es el producto punto.  
+   $(2)(3)$: Agrupaciones contiguas representan producto.  
+   $gt$: Variables contiguas representan producto.  
+   $2g$: Cantidades numéricas contiguas a una variable representan producto.  

Formas erradas de producto:  
+   $2x3$: Erróneo.  
+   2x3: Erróneo.  
+   2.3: Erróneo.  
+   $2*3$: Erróneo.  

Es necesario tener en cuenta el uso adecuado de $=$, $\rightarrow$ y :. El símbolo igual establece una relación de igualdad o asignación entre cantidades (uso exclusivo en expresiones matemáticas), el símbolo de la flecha es la relación lógica de implicación o una relación de orden y el símbolo de dos puntos se usa para asociar significados.  

Si usa negrilla (o texto reteñido a mano) en los símbolos es equivalente al uso de la flecha sobre la letra sin negrilla ($\vec{v}$), y representa vectores.  

## Software requerido

Software requerido para el desarrollo del taller 2.

+   Interprete o compilador de lenguaje de programación:  
    +   Python 3 (implementación oficial, CPython): Instalación recomendada con [Anaconda](https://www.continuum.io/downloads) o [miniconda](http://conda.pydata.org/miniconda.html) (en caso de equipos de bajas capacidades). Se recomienda como editor Spyder, Ninja, Atom o Jupyterlab.  
    +   Lenguaje M: Su código debe funcionar en [Octave 4](https://www.gnu.org/software/octave/download.html), que es un clon libre de Matlab.  
    +   Java (implementación estandar [OpenJDK](http://openjdk.java.net/)) versión 8.  
+   Software de procesamiento de texto (Microsoft Word, [LibreOffice Writer](https://es.libreoffice.org/ "Software libre de procesamiento de texto multiplataforma."), LaTeX -[Compilador](https://miktex.org/download "Compilador libre de LaTeX para windows.") y [Editor](http://www.xm1math.net/texmaker/download.html "Editor libre y multiplataforma de LaTeX.")-).  
+   Jupyter Notebook: Opcional, para aspirar a bonificación en los talleres. Si instalo python con ayuda de Anaconda, este ya estará instalado. De lo contrario, siga las [instrucciones](http://jupyter.readthedocs.io/en/latest/install.html).  
+   [7zip](http://www.7-zip.org/download.html) (recomendado para comprimir zip).  
