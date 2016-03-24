class HomeController {
  constructor($http) {
    'ngInject'
    this.$http = $http;
    this.name = 'home';
    this.url = 'http://testurl.ru/';
  }

  go(url) {
    this.$http({
      url: "/api/tiny/",
      method: "POST",
      data: JSON.stringify({link:url}),
      headers: { 'Content-Type': 'application/json;charset=utf-8' },
    }).success((data, status, headers, config) => {
      this.tinyId = data.tinyId;
    })
  }
}

export default HomeController;
