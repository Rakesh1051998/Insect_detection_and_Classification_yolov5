window.onload = () => {
  $("#sendbutton").click(() => {
    imagebox = $("#imagebox");
    previewimagebox = $("#previewimagebox");
    previewimagebox.attr("src", "static/loading3.gif");

    link = $("#link");
    input = $("#imageinput")[0];
    if (input.files && input.files[0]) {
      let formData = new FormData();
      formData.append("video", input.files[0]);
      $.ajax({
        url: "/detect", // fix this to your liking
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
          previewimagebox.attr("src", "static/error.gif");

        },
        success: function (data) {
          console.log(data);
          var json = $.parseJSON(data);
               console.log(json);
           data=json;
          // bytestring = data["status"];
          // image = bytestring.split("'")[1];
          $("#link").css("visibility", "visible");
          $("#download").attr("href", "static/finalimage/" + data.name);
          var classname = "Inscet Not found";
          var per =0;
          var classcode = -1;
          const myArray = data.result.split("|");
          if(myArray[2]==0)
          {
            classname = "Beetel insect";
          }
          if(myArray[2]==1)
          {
            classname = "Greenleaf_hopper";
          }
          if(myArray[2]==2)
          {
            classname = "Horn_caterpillar";
          }
          if(myArray[2]==3)
          {
            classname = "Spiny_beetle";
          }
          per = (myArray[1] * 100)+"%";
          $("#final").text(classname+"  "+per);
          //$("#percentage").text(per);
          previewimagebox.attr("src", "static/finalimage/" + data.name);
          console.log(data);
        },
      });
    }
  });
  $("#opencam").click(() => {
    console.log("evoked openCam");
    $.ajax({
      url: "/opencam",
      type: "GET",
      error: function (data) {
        console.log("upload error", data);
      },
      success: function (data) {
        console.log(data);
      }
    });
  })
};

function readUrl(input) {
  imagebox = $("#imagebox");
  console.log(imagebox);
  console.log("evoked readUrl");
  $("#final").text("")
  previewimagebox.attr("src", "");
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      console.log(e.target);

      imagebox.attr("src", e.target.result);
        // imagebox.height(500);
        // imagebox.width(800);
    };
    reader.readAsDataURL(input.files[0]);
  }
}


function openCam(e){
  console.log("evoked openCam");
  e.preventDefault();
  console.log("evoked openCam");
  console.log(e);
}