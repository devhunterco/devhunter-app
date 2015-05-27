

## Devhunt-community

[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/devhunterco)


Esta app esta construida con Python utilizando Django como framework.

La idea es bridar todos los features necesarios para organizar cualquier comunidad.

## Configuración 


- Incluir el archivo `local_settigs.py` en el directorio devhunt [Descargar aquí](https://gist.github.com/uzi200/5a6fa6eebb997a709040)
-  Instalar virtualenv `sudo pip install virtualenv`
-  En el repo hacer `virtualenv env && source env/bin/activate`
-  Instalar todas las dependencias `pip install -r requirements.txt`
-  Migrar la base de datos `./manage.py migrate`
-  Sincronizar los modelos `./manage.py syncdb`
-  Crear las tablas para los indices del cache `./manage.py createcachetable foro_cache`
-  Correr el servidor `./manage.py runserver`
-  Happy coding :D


## Todo list

- [ ] Integración Auth con githubs


### Relase v0.2

- [x] Modulo eventos
- [x] Calendario

### Relase v0.1

- [x] Pefiles
- [x] Comentarios (con formato, imagenes)
- [x] Notificaciones(Interno y mail)
- [x] Admin interface



### Frameworks / API's 

- [Django 1.7](https://github.com/django/django)
- [Spirit 0.1.3](https://github.com/nitely/Spirit/tree/master)
- [Github API](https://developer.github.com/v3/)
- [Trello API](https://trello.com/docs/)


### Licencia

Licensed under the [MIT License](http://opensource.org/licenses/MIT).

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
