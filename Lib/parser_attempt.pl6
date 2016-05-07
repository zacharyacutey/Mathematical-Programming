use v6;
@f = 1;
grammar AmplGrammar
{
  rule TOP { (<Line> ;)* }
  
  token ws { (\h | \s)* }
}
