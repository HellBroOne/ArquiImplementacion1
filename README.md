# ArquiImplementacion1
Repo de la tarea de Arqui 
- Hacer la imagen del cliente: docker build -t cliente .
- Correr el cliente: docker run --name cliente -p 0.0.0.0:5000:5000 -v ${PWD}:/dashboard cliente
