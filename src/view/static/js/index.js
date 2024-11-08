$("#agregar_ip").submit(function(event) {
    event.preventDefault();  // Evita que el formulario se envíe de manera tradicional
    $.ajax({
        type: "POST",
        url: "/agregar_ip",
        data: $(this).serialize(),
        success: function(response) {
            alert(response.message);  // Muestra un mensaje de éxito
            // Opcionalmente, puedes limpiar el formulario o actualizar la interfaz
        },
        error: function() {
            alert("Hubo un error al agregar la IP.");
        }
    });
});

$("#agregar-usuario").submit(function(event) {
    event.preventDefault();  // Evita que el formulario se envíe de manera tradicional
    $.ajax({
        type: "POST",
        url: "/agregar_usuario",
        data: $(this).serialize(),
        success: function(response) {
            alert(response.message);  // Muestra un mensaje de éxito
            // Opcionalmente, puedes limpiar el formulario o actualizar la interfaz
        },
        error: function() {
            alert("Hubo un error al agregar el Usuario.");
        }
    });
});

$("#limitar-bh").submit(function(event) {
    event.preventDefault();  // Evita que el formulario se envíe de manera tradicional
    $.ajax({
        type: "POST",
        url: "/limitar_bh",
        data: $(this).serialize(),
        success: function(response) {
            alert(response.message);  // Muestra un mensaje de éxito
            // Opcionalmente, puedes limpiar el formulario o actualizar la interfaz
        },
        error: function() {
            alert("Hubo un error al limitar el ancho de banda.");
        }
    });
});

$("#editar-bh").submit(function(event) {
    event.preventDefault();  // Evita que el formulario se envíe de manera tradicional
    $.ajax({
        type: "POST",
        url: "/editar_bh",
        data: $(this).serialize(),
        success: function(response) {
            alert(response.message);  // Muestra un mensaje de éxito
            // Opcionalmente, puedes limpiar el formulario o actualizar la interfaz
        },
        error: function() {
            alert("Hubo un error al editar el ancho de banda.");
        }
    });
});

$("#eliminar-bh").submit(function(event) {
    event.preventDefault();  // Evita que el formulario se envíe de manera tradicional
    $.ajax({
        type: "POST",
        url: "/eliminar_bh",
        data: $(this).serialize(),
        success: function(response) {
            alert(response.message);  // Muestra un mensaje de éxito
            // Opcionalmente, puedes limpiar el formulario o actualizar la interfaz
        },
        error: function() {
            alert("Hubo un error al editar el ancho de banda.");
        }
    });
});



// botones principales
function showForm(formId) {
    document.getElementById('crear-usuario').classList.add('hidden');
    document.getElementById('agregar-ip').classList.add('hidden');
    document.getElementById('ancho-banda').classList.add('hidden');
    document.getElementById(formId).classList.remove('hidden');
}

// botones secundarios
function toggleForm(showId, hideId, hideId2) {
    document.getElementById(showId).classList.remove('hidden');
    document.getElementById(hideId).classList.add('hidden');
    document.getElementById(hideId2).classList.add('hidden');
}