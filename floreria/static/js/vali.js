$(document).ready(function() {
    console.log("JavaScript cargado correctamente");

    $("#registro").submit(function(event) {
        var nombreUsuario = $("#id_username").val();
        var nombre = $("#id_nombre").val();
        var edad = $("#id_edad").val();
        var correo = $("#id_correo").val();

        console.log("Datos ingresados: ", { nombreUsuario, nombre, edad, correo });

        var nombreValido = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(nombre);
        if (!nombreValido) {
            alert("Nombre y apellido no debe contener caracteres especiales ni números.");
            event.preventDefault();
            return;
        }

        if (parseInt(edad) < 18) {
            alert("Debes ser mayor de 18 años para registrarte.");
            event.preventDefault();
            return;
        }

        alert("Formulario enviado correctamente.");
    });
});

