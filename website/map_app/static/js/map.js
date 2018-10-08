let map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: new google.maps.LatLng(-5.7793, -35.2009)
  });

  // Recebe em json todas as instituições 
  let instituicoes = [];
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        JSON.parse(xhttp.responseText).forEach( function (element) {
          instituicoes.push(element);
        }); 
      }
  };
  xhttp.open("GET", "api/instituicoes", false);
  xhttp.send();

  // Recebe em json todos os orgãos
  let orgaos = [];
  let xhttp2 = new XMLHttpRequest();
  xhttp2.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        JSON.parse(xhttp2.responseText).forEach( function (element) {
          orgaos.push(element);
        }); 
      }
  };
  xhttp2.open("GET", "api/orgao/pk/1", false);
  xhttp2.send();

  // Recebe em json todas as despesas de um dado ano
  let despesas = [];
  let xhttp3 = new XMLHttpRequest();
  xhttp3.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      JSON.parse(xhttp3.responseText).forEach( function (element) {
        // Se a despesa tiver localização então adicionar ao array
        if (element.localizacao != null) {
          despesas.push(element);
        }
      });
    }
  };
  xhttp3.open("GET", "api/despesa/ano/2018", false);
  xhttp3.send();

  // Define um icone diferente para as instituições, orgãos e as despesas
  let iconBase = 'https://maps.google.com/mapfiles/kml/paddle/';
  let icons = {
    instituicao: {
      icon: iconBase + 'blu-stars.png'
    },
    despesa: {
      icon: iconBase + 'ylw-stars.png'
    },
    orgao: {
      icon: iconBase + 'grn-stars.png'
    }
  };
  
  // Adiciona todas as marcações de instituições
  let markers_inst = instituicoes.map(function(instituicao, i) {
    let marker = new google.maps.Marker({
      position: new google.maps.LatLng(instituicao.localizacao.latitude, instituicao.localizacao.longitude),
      icon: icons['instituicao'].icon,
      title: instituicao.nome,
      map: map
    });

    marker.addListener('click', function() {
      let detalhe_despesa = document.getElementById('detalhe');
      detalhe_despesa.style.backgroundColor = "blue";
    });

    return marker;
  });

  // Adiciona todas as marcações de orgãos
  let markers_orgaos = orgaos.map(function(orgao, i) {
    let marker = new google.maps.Marker({
      position: new google.maps.LatLng(orgao.localizacao.latitude, orgao.localizacao.longitude),
      icon: icons['orgao'].icon,
      title: orgao.nome,
      map: map
    });

    marker.addListener('click', function() {
      let detalhe_despesa = document.getElementById('detalhe');
      detalhe_despesa.style.backgroundColor = "green";
    });

    return marker;
  });

  // Adiciona todas as marcações das despesas
  let markers_despesas = despesas.map(function(despesa, i) {
    let marker = new google.maps.Marker({
      position: new google.maps.LatLng(despesa.localizacao.latitude, despesa.localizacao.longitude),
      icon: icons['despesa'].icon,
      title: despesa.descricao,
      map: map
    });

    // Ação feita após o click na marcação
    marker.addListener('click', function() {
      // Teste mudando a cor do background da div
      let detalhe_despesa = document.getElementById('detalhe');
      detalhe_despesa.style.backgroundColor = "yellow";
    });

    return marker;
  });

  let markers = markers_inst.concat(markers_orgaos).concat(markers_despesas);

  let markerCluster = new MarkerClusterer(map, markers,{imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}