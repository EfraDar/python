# Obtener la dirección de correo electrónico del usuario
email  =  input ( "¿Cuál es su dirección de correo electrónico ?:" ). tira ()

# Corta el nombre de usuario
nombre_usuario  =  correo electrónico [: correo electrónico . índice ( "@" )]

# Corta el nombre de dominio
nombre_dominio  =  correo electrónico [ correo electrónico . índice ( "@" ) + 1 :]

# Formato de mensaje
output  =  "Su nombre de usuario es '{}' y su nombre de dominio es '{}'" . formato ( nombre_usuario , nombre_dominio )

# Mostrar mensaje de salida
imprimir ( salida )