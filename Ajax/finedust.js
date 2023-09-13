function q1() {
  $.ajax({
    type: "GET",
    url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
    data: {},
    success: function (response) {
      $("#names-q1").empty(); //화면에 출력 전에 지워주는 코드
      let mise = response["RealtimeCityAir"]["row"];
      for (let i = 0; i < mise.length; i++) {
        let gu_name = mise[i]["MSRSTE_NM"];
        let gu_mise = mise[i]["IDEX_MVL"];
        if (gu_mise < 70) {
          let str_mise = `<li>${gu_name} : ${gu_mise}</li>`;
          $("#names-q1").append(str_mise);
        }
      }
      console.log(response);
    },
  });
}
