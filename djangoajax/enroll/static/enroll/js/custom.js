$("#btnsave").click(function(){
    console.log("Clicked")
    name = $("#nameid").val()
    email = $("#emailid").val()
    password = $("#passwordid").val()
    if(name==''){
        console.log("Name should not be empty")
    }else if(email==''){
        console.log("Email should not be empty")
    }else if(password==''){
        console.log("Password should not be empty")
    }
    else{
        console.log(name)
        console.log(email)
        console.log(password)
    }
})