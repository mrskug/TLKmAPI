graph [
  comment "Created by dottoxml.py"
  directed 1
  IsPlanar 1
  node [
    id 21
    label
    "person (committees)"] [arrowhead=none"
  ]
  node [
    id 11
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> Committee </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">person</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">type</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">year</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">IntegerField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 9
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> Official </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">person</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">type</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">year</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">IntegerField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 2
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> BoardPosition </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">name</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">CharField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 8
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> Board </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">person</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">type</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">year</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">IntegerField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 3
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> CommitteeType </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">name</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">CharField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 1
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> MemberType </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">name</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">CharField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 5
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> MeritType </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">name</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">CharField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 10
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> Merit </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">person</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">type</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">year</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">IntegerField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 7
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> Member </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">person</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">type</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">ForeignKey (id)</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">year</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">IntegerField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 6
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> Person </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">address</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">birthplace</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">city</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">company</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">company_email</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">company_phone</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">country</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">dob</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">DateField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">dod</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">DateField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">email</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">firstname</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">graduated</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">DateField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">joined</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">DateField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">lastname</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">middlenames</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">notes</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">TextField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">phone</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">zip</FONT> </TD><TD ALIGN="LEFT"> <FONT COLOR="#7B7B7B" FACE="Helvetica ">CharField</FONT> </TD></TR> </TABLE> >"
  ]
  node [
    id 4
    label
    "< <TABLE BGCOLOR="palegoldenrod" BORDER="0" CELLBORDER="0" CELLSPACING="0"> <TR><TD COLSPAN="2" CELLPADDING="4" ALIGN="CENTER" BGCOLOR="olivedrab4"> <FONT FACE="Helvetica Bold" COLOR="white"> OfficialType </FONT></TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica Bold">id</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica Bold">AutoField</FONT> </TD></TR> <TR><TD ALIGN="LEFT" BORDER="0"> <FONT FACE="Helvetica ">name</FONT> </TD><TD ALIGN="LEFT"> <FONT FACE="Helvetica ">CharField</FONT> </TD></TR> </TABLE> >"
  ]
  edge [
    source 7
    target 1
    label
    ""
  ]
  edge [
    source 7
    target 6
    label
    ""
  ]
  edge [
    source 8
    target 2
    label
    ""
  ]
  edge [
    source 8
    target 6
    label
    ""
  ]
  edge [
    source 9
    target 4
    label
    ""
  ]
  edge [
    source 9
    target 6
    label
    ""
  ]
  edge [
    source 10
    target 5
    label
    ""
  ]
  edge [
    source 10
    target 6
    label
    ""
  ]
  edge [
    source 11
    target 3
    label
    ""
  ]
  edge [
    source 11
    target 6
    label
    ""
  ]
]
