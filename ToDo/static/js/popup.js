document.addEventListener('DOMContentLoaded', function () {
    const deleteLinks = document.querySelectorAll('.delete-link');
  
    deleteLinks.forEach((link) => {
      link.addEventListener('click', function (e) {
        e.preventDefault();
  
        // Get the URL from the href attribute of the delete link
        const url = this.getAttribute('href');
  
        // Fetch the HTML fragment for the delete view popup using AJAX
        fetch(url)
          .then((response) => response.text())
          .then((html) => {
            // Create a popup element and set its content to the fetched HTML fragment
            const popup = document.createElement('div');
            popup.innerHTML = html;
  
            // Extract the task ID from the delete link's href
            const taskId = url.split('/').reverse()[1]; // Assuming the URL format is '/task_delete/{task_id}/'
  
            // Add the task ID to the form action URL
            const form = popup.querySelector('form');
            form.action = form.action.replace('task_id', taskId);
  
            // Add the popup to the DOM
            // Append the popup as the first child of the document body
            document.body.insertBefore(popup, document.body.firstChild);
  
            // Add a click event listener to the "Delete" button in the popup
            const deleteButton = popup.querySelector('input[type="submit"]');
            deleteButton.addEventListener('click', function () {
              // Submit the delete form
              form.submit();
            });
  
            // Add a click event listener to the "Cancel" link in the popup
            const cancelButton = popup.querySelector('a.cancel-link');
            cancelButton.addEventListener('click', function () {
              // Remove the popup from the DOM
              document.body.removeChild(popup);
            });
          })
          .catch((error) => {
            console.error('Error fetching delete view HTML:', error);
          });
      });
    });
  });