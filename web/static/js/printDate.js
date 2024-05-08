var date = new Date();
var strDate = "";
switch(date.getDay()) {
	case 0:
		strDate += "ВС, ";
		break;
	case 1:
		strDate += "ПН, ";
		break;
	case 2:
		strDate += "ВТ, ";
		break;
	case 3:
		strDate += "СР, ";
		break;
	case 4:
		strDate += "ЧТ, ";
		break;
	case 5:
		strDate += "ПТ, ";
		break;
	case 6:
		strDate += "СБ, ";
		break;
}
strDate += date.getDate();
switch(date.getMonth()) {
	case 0:
		strDate += " ЯНВАРЬ ";
		break;
	case 1:
		strDate += " ФЕВРАЛЬ ";
		break;
	case 2:
		strDate += " МАРТ ";
		break;
	case 3:
		strDate += " АПРЕЛЬ ";
		break;
	case 4:
		strDate += " МАЙ ";
		break;
	case 5:
		strDate += " ИЮНЬ ";
		break;
	case 6:
		strDate += " ИЮЛЬ ";
		break;
	case 7:
		strDate += " АВГУСТ ";
		break;
	case 8:
		strDate += " СЕНТЯБРЬ ";
		break;
	case 9:
		strDate += " ОКТЯБРЬ ";
		break;
	case 10:
		strDate += " НОЯБРЬ ";
		break;
	case 11:
		strDate += " ДЕКАБРЬ ";
		break;
}
strDate += date.getFullYear();
document.write(strDate);