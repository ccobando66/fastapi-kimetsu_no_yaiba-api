<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="fastapikimetsu_no_yaibaapi_0"></a>fastapi-kimetsu_no_yaiba-api</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="_API_interactivo_referente_a_mundo_de_kimetsu_no_yaiba__1"></a><em>API interactivo referente a mundo de kimetsu no yaiba</em></h2>
<p class="has-line-data" data-line-start="3" data-line-end="4"><a href="https://fastapi.tiangolo.com/"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="N|Solid"></a></p>
<h2 class="code-line" data-line-start=5 data-line-end=6 ><a id="Caractersticas_5"></a>Características</h2>
<ul>
<li class="has-line-data" data-line-start="7" data-line-end="8">Consultas sobre características y cualidades de cada personaje</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">Posibilidad de agregar respiraciones, organización, katanas nichirin y técnicas</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">Sistema de autenticación y autorización implementando Oauth2 y JWT</li>
<li class="has-line-data" data-line-start="10" data-line-end="11">interacción al momento de agregar kanatas nichirin</li>
<li class="has-line-data" data-line-start="11" data-line-end="13">Documentación enpoint con swagger</li>
</ul>
<h2 class="code-line" data-line-start=13 data-line-end=14 ><a id="Estructura_13"></a>Estructura</h2>
<pre><code class="has-line-data" data-line-start="16" data-line-end="67" class="language-s">├── auth
│   ├── JWT.py
│   ├── _auth2.py
│
├── config
│   ├── config.py
│
├── helpers
│   ├── get_afiliacion_for_personaje.py
│   ├── get_espadas_for_personaje.py
│   ├── get_especies_for_personaje.py
│
├── main.py
│
├── models
│   ├── afiliacion_personaje.py
│   ├── afiliacion.py
│   ├── espada_personaje.py
│   ├── espada.py
│   ├── especie_personaje.py
│   ├── especie.py
│   ├── personaje.py
│   ├── respiraciones_personaje.py
│   ├── respiraciones.py
│   ├── tecnica.py
│   └── usuario.py
│
├── requirements.txt
│
├── routers
│   ├── afiliacion.py
│   ├── auth.py
│   ├── espadas.py
│   ├── especies.py
│   ├── personajes.py
│   ├── respiraciones.py
│   └── tecnica.py
│
├── schema
│   ├── afiliacion_personaje_schema.py
│   ├── afiliacion_schema.py
│   ├── espada_personaje_schema.py
│   ├── espada_schema.py
│   ├── especie_personaje_schema.py
│   ├── especie_schema.py
│   ├── personaje_schema.py
│   ├── respiraciones_personaje_schema.py
│   ├── respiraciones_schema.py
│   ├── tecnica_schema.py
│   └── usuario_schema.py
</code></pre>
<h2 class="code-line" data-line-start=69 data-line-end=70 ><a id="End_points_69"></a>End points</h2>
<p class="has-line-data" data-line-start="70" data-line-end="71">Métodos de acceso a la información e interacción de la API</p>
<h3 class="code-line" data-line-start=72 data-line-end=73 ><a id="_Personajes__72"></a><em>Personajes</em></h3>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>HTTP Request</th>
<th>Path</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/</td>
<td>Get All Personajes</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/personaje/{id_personaje}</td>
<td>Get Personaje</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/personaje</td>
<td>Create Personaje</td>
</tr>
<tr>
<td>PUT</td>
<td>/api/v1/personaje/{id_personaje}</td>
<td>Update Personaje</td>
</tr>
</tbody>
</table>
<h3 class="code-line" data-line-start=80 data-line-end=81 ><a id="_Respiraciones__80"></a><em>Respiraciones</em></h3>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>HTTP Request</th>
<th>Path</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/api/v1/respiracion</td>
<td>Get All Respiraciones</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/respiracion/{id_respiracion}</td>
<td>Get Respiraciones</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/respiracion/personaje/{id_personaje}</td>
<td>Get Respiraciones by Personajes</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/respiracion/</td>
<td>Create Respiraciones</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/respiracion/personaje</td>
<td>Create Respiraciones to Personajes</td>
</tr>
</tbody>
</table>
<h3 class="code-line" data-line-start=89 data-line-end=90 ><a id="_Espadas__89"></a><em>Espadas</em></h3>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>HTTP Request</th>
<th>Path</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/api/v1/espadas</td>
<td>Get All Especies</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/espadas/danadas</td>
<td>Get All Espadas dañadas</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/espadas/{id_espadas}</td>
<td>Get Espadas</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/espadas/personaje/{id_personaje}</td>
<td>Get Espadas by Personajes</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/espadas/</td>
<td>Create Espadas</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/espadas/personaje</td>
<td>Create Espadas to Personajes</td>
</tr>
</tbody>
</table>
<h3 class="code-line" data-line-start=99 data-line-end=100 ><a id="_AUTH__99"></a><em>AUTH</em></h3>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>HTTP Request</th>
<th>Path</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/token/me</td>
<td>Read user</td>
</tr>
<tr>
<td>POST</td>
<td>/token/jwt</td>
<td>Create JWT</td>
</tr>
</tbody>
</table>
<h3 class="code-line" data-line-start=106 data-line-end=107 ><a id="_Tecnicas__106"></a><em>Tecnicas</em></h3>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>HTTP Request</th>
<th>Path</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/api/v1/tecnicas</td>
<td>Get All Tecnicas</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/tecnicas/{id_tecnica}</td>
<td>Get Tecnicas</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/tecnicas/personaje/{id_personaje}</td>
<td>Get Tecnicas by personaje</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/tecnicas/</td>
<td>Create Tecnicas</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/tecnicas/personaje</td>
<td>Create Tecnicas to Personajes</td>
</tr>
</tbody>
</table>
<h3 class="code-line" data-line-start=115 data-line-end=116 ><a id="_Afiliaciones__115"></a><em>Afiliaciones</em></h3>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>HTTP Request</th>
<th>Path</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/api/v1/afiliacion</td>
<td>Get All afiliacion</td>
</tr>
<tr>
<td>GET</td>
<td>/api/v1/afiliacion/personaje/{id_personaje}</td>
<td>Get afiliacion</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/afiliacion/</td>
<td>Create afiliacion</td>
</tr>
<tr>
<td>POST</td>
<td>/api/v1/tecnicas/personaje</td>
<td>Create afiliacion to Personajes</td>
</tr>
</tbody>
</table>
<h2 class="code-line" data-line-start=126 data-line-end=127 ><a id="instalacin_126"></a>instalación</h2>
<p class="has-line-data" data-line-start="127" data-line-end="128">Versión usada en este proyecto <a href="https://www.python.org/">Python 3.10</a>  o superior</p>
<p class="has-line-data" data-line-start="129" data-line-end="130">Clonar repositorio.</p>
<pre><code class="has-line-data" data-line-start="131" data-line-end="135" class="language-sh">git <span class="hljs-built_in">clone</span> https://github.com/ccobando66/fastapi-kimetsu_no_yaiba-api.git
<span class="hljs-built_in">cd</span> fastapi-kimetsu_no_yaiba-api --&gt; linux
dir fastapi-kimetsu_no_yaiba-api --&gt; windows
</code></pre>
<p class="has-line-data" data-line-start="136" data-line-end="137">Crear entono virtual venv…</p>
<pre><code class="has-line-data" data-line-start="139" data-line-end="143" class="language-sh">python3.<span class="hljs-number">10</span> -m venv venv
<span class="hljs-built_in">source</span> venv/bin/activate --&gt; linux
venv\Scripts\activate.bat --&gt; windows
</code></pre>
<p class="has-line-data" data-line-start="144" data-line-end="145">Instalar dependencias en el entorno virtual…</p>
<pre><code class="has-line-data" data-line-start="147" data-line-end="149" class="language-sh">pip3.<span class="hljs-number">10</span> install -r requirements.txt
</code></pre>
<p class="has-line-data" data-line-start="149" data-line-end="150">Iniciar servidor uvicorn…</p>
<pre><code class="has-line-data" data-line-start="152" data-line-end="154" class="language-sh">uvicorn main:app --host <span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span> --port <span class="hljs-number">8080</span> --reload 
</code></pre>
<h2 class="code-line" data-line-start=154 data-line-end=155 ><a id="Desarrollo_154"></a>Desarrollo</h2>
<h4 class="code-line" data-line-start=156 data-line-end=157 ><a id="_Base_de_datos__156"></a><em>Base de datos</em></h4>
<p class="has-line-data" data-line-start="158" data-line-end="161">Base de datos utilizada para realizar pruebas a cada endpoint<br>
base de datos postgresql <a href="https://web3portal.com/BADUjpKqovO4Sh4PpoznMKR_47llzdOl6SHgq8okxAzuaA">link Data base postgresql</a><br>
version PostgreSQL 15.1 x64</p>
<p class="has-line-data" data-line-start="162" data-line-end="163">restaurar base de datos:</p>
<pre><code class="has-line-data" data-line-start="165" data-line-end="167" class="language-sh">psql -U username <span class="hljs-operator">-f</span> kny.backup
</code></pre>
<h4 class="code-line" data-line-start=168 data-line-end=169 ><a id="Creditos_168"></a>Creditos</h4>
<p class="has-line-data" data-line-start="169" data-line-end="170"><a href="https://kimetsu-no-yaiba.fandom.com/es/wiki/Kimetsu_no_Yaiba_Wiki">Kimetsu no Yaiba Wiki</a></p>
