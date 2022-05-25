function validate() {
        //event.preventDefault();
        var objPwd1 = document.getElementById("password");
        var objPwd2 = document.getElementById("passwordCheck");
        var objEmail = document.getElementById("email");
        var objName = document.getElementById("name");
        var objNickname = document.getElementById("nickname");
        var objCellphone = document.getElementById("cellphoneNo");

        //패스워드 값 데이터 정규화 공식
        var regul1 = /^[a-zA-Z0-9]{4,12}$/;
        //이메일 정규화 공식
        var regul2 = /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/;
        //var regul2 = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/;
        //이름 정규화 공식
        var regul3 = /^[가-힣]{2,4}$/;
        //닉네임 정규화 공식
        var regul4 = /^[가-힝a-zA-Z]{2,}$/;
        //전화번호 정규화 공식
        var regul5 = /(\d{3})(\d{4})(\d{4})/;


        //이메일 입력 안했을 경우
        if ((objEmail.value)=="") {
            document.getElementById("emailError").innerHTML="이메일을 입력해주세요.";
            objEmail.focus();
            return false;
        } else { document.getElementById("emailError").innerHTML=""; }
        //이메일이 잘못된 경우
        if (!check(regul2,objEmail)) {
            document.getElementById("emailError").innerHTML="이메일이 올바르지 않습니다.";
            return false;
        } else { document.getElementById("emailError").innerHTML=""; }
        //비밀번호 입력 하지 않았을 경우
        if ((objPwd1.value) == ""){
            document.getElementById("passwordError").innerHTML="비밀번호를 입력해주세요..";
            objPwd1.focus();
            return false;
        //비밀번호 확인을 입력 하지 않았을 경우
        } else { document.getElementById("passwordError").innerHTML=""; }
        if ((objPwd2.value=="")){
            document.getElementById("passwordCheckError").innerHTML="비밀번호 확인을 입력해주세요.";
            objPwd2.focus();
            return false;
        } else { document.getElementById("passwordCheckError").innerHTML="";}
        //비밀번호 유효성 검사
        if (!check(regul1,objPwd1,)) {
            document.getElementById("passwordCheckError").innerHTML="비밀번호는 4~12자의 대소문자와 숫자로만 입력 가능합니다.";
            return false;
        } else { document.getElementById("passwordCheckError").innerHTML="";}

        //비밀번호와 비밀번호 확인이 일치 하지 않을 경우
        if ((objPwd1.value)!=(objPwd2.value)) {
            document.getElementById("passwordCheckError").innerHTML="비밀번호가 일치하지 않습니다.";
            objPwd1.focus();
            objPwd2.focus();
            return false;
        } else { document.getElementById("passwordCheckError").innerHTML="";}
        //이름 입력 안 한 경우
        if ((objName.value)=="") {
            document.getElementById("nameError").innerHTML="이름을 입력해주세요.";
            objName.focus();
            return false;
        } else { document.getElementById("nameError").innerHTML="";}
        //이름에 영어나 특수 문자가 들어 간 경우
        if (!check(regul3,objName,)) {
            document.getElementById("nameError").innerHTML="잘못된 형식의 이름입니다.";
            return false;
        }
        //닉네임 입력 안 한 경우
        if ((objNickname.value)=="") {
            document.getElementById("nicknameError").innerHTML="닉네임을 입력해주세요.";
            objNickname.focus();
            return false;
        } else { document.getElementById("nicknameError").innerHTML="";}
        //닉네임에 특수 문자가 들어간 경우
        if (!check(regul4,objNickname)) {
            document.getElementById("nicknameError").innerHTML="잘못된 형식의 닉네임입니다.";
            return false;
        }
        if ((objCellphone.value)=="") {
            document.getElementById("cellphoneNoError").innerHTML="전화번호를 입력해주세요.";
            objNickname.focus();
            return false;
        } else { document.getElementById("cellphoneNoError").innerHTML="";}
        if (!check(regul5,objCellphone)) {
            document.getElementById("cellphoneNoError").innerHTML="잘못된 형식의 전화번호입니다.";
            return false;
        }
    }

    function check(re,what){//정규화데이터,아이템 id,메세지
        if (re.test(what.value)) {//what의 문자열에 re의 패턴이 있는지 나타내는 함수 test
        //만약 내가 입력한 곳의 값이 정규화 데이터를 썼다면 true를 반환해서 호출 된 곳으로 리턴됨
            return true;
        }
        //alert(message);
        what.value = "";
        what.focus();
    }