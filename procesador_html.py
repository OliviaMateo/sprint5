class ProcesadorHtml:

    def __init__(self,cliente_json) -> None:
        elemento=cliente_json["direccion"]
        calle=elemento["calle"]
        numero=elemento["numero"]
        cuidad=elemento["ciudad"]
        provincia=elemento["provincia"]
        pais=elemento["pais"]
        
        self.texto_html =f'''<html>
                <title>Listado de transacciones</title>
                <body>
                    <h1>{cliente_json['apellido']}, {cliente_json['nombre']}</h1>
                    <div>Número cliente: {cliente_json['numero']}</div>
                    <div>DNI: {cliente_json['dni']}</div>
                    <div>Dirección: Calle: {calle}, nro: {numero} - Ciudad: {cuidad} - {provincia}, {pais}</div>
                    <table>
                        <tr><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto</td><td>Razon</td></tr>
                    '''
    def escribir_html_rechazo(self,transaccion,razon):
        self.texto_html=self.texto_html+f'''<tr></tr>'''
        self.texto_html=self.texto_html+f'''<tr><td>{transaccion['fecha']} -</td><td> {transaccion['tipo']} -</td><td> {transaccion['estado']} -</td><td> {transaccion['monto']} -</td><td> {razon} </td></tr>'''
        self.texto_html=self.texto_html+f'''<tr></tr>'''
    
    def escribir_html_aceptacion(self,transaccion):
        self.texto_html=self.texto_html+f'''<tr></tr>'''
        self.texto_html=self.texto_html+f'''<tr><td>{transaccion['fecha']} -</td><td> {transaccion['tipo']} -</td><td> {transaccion['estado']} -</td><td> {transaccion['monto']} -</td><td> -   -   - </td></tr>'''
        self.texto_html=self.texto_html+f'''<tr></tr>'''   
        
        
    def cerrar_html(self):
        self.texto_html= self.texto_html+f'''
                    </table>
                </body>
            </html>'''
