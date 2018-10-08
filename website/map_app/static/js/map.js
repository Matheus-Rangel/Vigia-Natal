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

  xhttp2.open("GET", "api/orgaos", false);
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
    console.log(instituicao.localizacao)
    let marker = new google.maps.Marker({
      position: new google.maps.LatLng(instituicao.localizacao.latitude, instituicao.localizacao.longitude),
      icon: icons['instituicao'].icon,
      title: instituicao.nome,
      map: map
    });

    marker.addListener('click', function() {
      //Pega a div principal e mostra ela caso estivesse escondida
      let detalhe_despesa = document.getElementById('detalhe');
      if (detalhe_despesa.style.display == "none") {
        detalhe_despesa.style.display = "block";
      }

      //Recupera cada campo a ser modificado
      let nome_inst = document.getElementById('nome');
      let email_inst = document.getElementById('email');
      let site_inst = document.getElementById('site');
      let telefone_inst = document.getElementById('telefone');
      
      //Seta as informações da Instituição em questão
      nome_inst.innerHTML = (instituicao.nome != "") ? instituicao.nome : 'Não informado';
      email_inst.innerHTML = (instituicao.email != "") ? instituicao.email : 'Não informado';
      site_inst.innerHTML = (instituicao.site != "") ? instituicao.site : 'Não informado';
      telefone_inst.innerHTML = (instituicao.telefone != "") ? instituicao.telefone : 'Não informado';

      //Setar informações das despesas da instituição na div despesa
    });

    return marker;
  });

  // Adiciona todas as marcações de orgãos
  let markers_orgaos = orgaos.map(function(orgao, i) {
    if (orgao.localizacao != null) {
      let marker = new google.maps.Marker({
        position: new google.maps.LatLng(orgao.localizacao.latitude, orgao.localizacao.longitude),
        icon: icons['orgao'].icon,
        title: orgao.nome,
        map: map
      });
      
      marker.addListener('click', function() {
        //Pega a div principal e mostra ela caso estivesse escondida
        let detalhe_despesa = document.getElementById('detalhe');
        if (detalhe_despesa.style.display == "none") {
          detalhe_despesa.style.display = "block";
        }
  
        //Recupera cada campo a ser modificado
        let nome_orgao = document.getElementById('nome');
        let email_orgao = document.getElementById('email');
        let site_orgao = document.getElementById('site');
        let telefone_orgao = document.getElementById('telefone');
        
        //Seta as informações do Orgão em questão
        nome_orgao.innerHTML = (orgao.nome != "") ? orgao.nome : 'Não informado';
        email_orgao.innerHTML = (orgao.email != "") ? orgao.email : 'Não informado';
        site_orgao.innerHTML = (orgao.site != "") ? orgao.site : 'Não informado';
        telefone_orgao.innerHTML = (orgao.telefone != "") ? orgao.telefone : 'Não informado';
  
        //Setar informações das despesas do Orgão na div despesa
      });
  
      return marker;
    } else {
      return null;
    }
    
  });

  // Adiciona todas as marcações das despesas
  let markers_despesas = despesas.map(function(despesa, i) {
    let marker = new google.maps.Marker({
      position: new google.maps.LatLng(despesa.localizacao.latitude, despesa.localizacao.longitude),
      icon: icons['despesa'].icon,
      title: despesa.descricao,
      map: map
    });

    marker.addListener('click', function() {
      //Pega a div principal e mostra ela caso estivesse escondida
      let detalhe_despesa = document.getElementById('detalhe');
      if (detalhe_despesa.style.display == "none") {
        detalhe_despesa.style.display = "block";
      }

      //Recupera cada campo a ser modificado
      let nome = document.getElementById('nome');
      let email = document.getElementById('email');
      let site = document.getElementById('site');
      let telefoneo = document.getElementById('telefone');
      
      //Seta as informações do Orgão da despesa em questão
      nome.innerHTML = (despesa.orgao.nome != "") ? despesa.orgao.nome : 'Não informado';
      email.innerHTML = (despesa.orgao.email != "") ? despesa.orgao.email : 'Não informado';
      site.innerHTML = (despesa.orgao.site != "") ? despesa.orgao.site : 'Não informado';
      telefone.innerHTML = (despesa.orgao.telefone != "") ? despesa.orgao.telefone : 'Não informado';

      //Setar informações da despesa na div despesa
    });

    return marker;
  });
}
