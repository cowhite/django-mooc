$(function(){
  var newCourseAdded = function(data) {
    console.log(data);
  }
  $(document).on("newCourse-submitted", function(e, data){
    console.log("newCourse-submitted");
    console.log(e);
    console.log(data);

  })
  onLoad();

});
