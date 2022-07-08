var headerNav = `
    <div class="container">
        <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
          <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
            <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
            <span class="fs-4">Listado Gráficos</span>
          </a>
    
          <ul class="nav nav-pills" id="navigation">
            <li class="nav-item"><a href="/" class="nav-link active" aria-current="page">Total Ventas</a></li> 
            <li class="nav-item"><a href="/api-total-ventas" class="nav-link">api-total-ventas</a></li>
            <li class="nav-item"><a href="/other" class="nav-link">other</a></li>
            <li class="nav-item"><a href="/sqlite" class="nav-link">sqlite</a>
          </ul>
        </header>
      </div>
      `
var navigation = document.getElementById('navigation')
    navigation.innerHTML = headerNav
    
