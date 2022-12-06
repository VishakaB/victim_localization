<!DOCTYPE html>
<!-- saved from url=(0042)https://codeocean.com/capsule/0614176/tree -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><!--<base href="/">--><base href="."><title>Vishaka | Code Ocean</title><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"><link rel="icon" href="https://codeocean.com/fav-prime.png"><link rel="apple-touch-icon" href="https://codeocean.com/fav-prime.png"><link href="./mvla_files/css" rel="stylesheet"><style>body{margin:0}.appWrapper{height:100%;display:flex;flex-direction:column}#codeoceanApp,#codeoceanApp>div{display:flex;flex-direction:column;flex:1;overflow:auto}</style><style data-styled="active" data-styled-version="5.2.1"></style><meta name="twitter:card" content="summary" data-rh="true"><meta property="og:type" content="website" data-rh="true"><meta property="og:title" content="Code Ocean | Discover &amp; Run Scientific Code" data-rh="true"><meta property="og:image" content="https://s3.amazonaws.com/codeocean-assets/logo/header.jpg" data-rh="true"><meta property="og:description" content="Code Ocean is a cloud-based executable research platform. Discover, run and share scientific code." data-rh="true"><script type="text/javascript" async="" src="./mvla_files/analytics.js.download"></script><script type="text/javascript" async="" src="./mvla_files/gtm.js.download"></script><script type="text/javascript" async="" src="./mvla_files/t6819744"></script><script type="text/javascript" async="" src="./mvla_files/analytics.js.download"></script><script type="text/javascript" src="./mvla_files/commons.3495c86769f191d6894f.js.gz" async="" status="loaded"></script><script type="text/javascript" src="./mvla_files/commons.dddbd6a06577f22e5c7f.js.gz" async="" status="loaded"></script><script type="text/javascript" src="./mvla_files/commons.54701049fd6fb8497e9e.js.gz" async="" status="loaded"></script><script type="text/javascript" src="./mvla_files/google-tag-manager.dynamic.js.gz" async="" status="loaded"></script><script type="text/javascript" src="./mvla_files/intercom.dynamic.js.gz" async="" status="loaded"></script><script type="text/javascript" src="./mvla_files/google-analytics.dynamic.js.gz" async="" status="loaded"></script><meta name="description" content="Code Ocean is a cloud-based executable research platform that provides researchers and developers with an easy way to share, discover and run code published in academic journals and conferences." data-rh="true"><style>/* stylelint-disable font-family-no-missing-generic-family-keyword */
@font-face {
  font-family: 'KaTeX_AMS';
  src: url(assets/fonts/KaTeX_AMS-Regular.d4531c.woff2) format('woff2'), url(assets/fonts/KaTeX_AMS-Regular.b1489d.woff) format('woff'), url(assets/fonts/KaTeX_AMS-Regular.f80d9e.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Caligraphic';
  src: url(assets/fonts/KaTeX_Caligraphic-Bold.f046a3.woff2) format('woff2'), url(assets/fonts/KaTeX_Caligraphic-Bold.7ce763.woff) format('woff'), url(assets/fonts/KaTeX_Caligraphic-Bold.0c96bc.ttf) format('truetype');
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Caligraphic';
  src: url(assets/fonts/KaTeX_Caligraphic-Regular.4519ba.woff2) format('woff2'), url(assets/fonts/KaTeX_Caligraphic-Regular.4a559f.woff) format('woff'), url(assets/fonts/KaTeX_Caligraphic-Regular.35f3c9.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Fraktur';
  src: url(assets/fonts/KaTeX_Fraktur-Bold.5b8749.woff2) format('woff2'), url(assets/fonts/KaTeX_Fraktur-Bold.2ea391.woff) format('woff'), url(assets/fonts/KaTeX_Fraktur-Bold.069514.ttf) format('truetype');
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Fraktur';
  src: url(assets/fonts/KaTeX_Fraktur-Regular.2c629b.woff2) format('woff2'), url(assets/fonts/KaTeX_Fraktur-Regular.0d9011.woff) format('woff'), url(assets/fonts/KaTeX_Fraktur-Regular.96556d.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Main';
  src: url(assets/fonts/KaTeX_Main-Bold.20b90c.woff2) format('woff2'), url(assets/fonts/KaTeX_Main-Bold.a9cdbc.woff) format('woff'), url(assets/fonts/KaTeX_Main-Bold.07e762.ttf) format('truetype');
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Main';
  src: url(assets/fonts/KaTeX_Main-BoldItalic.b345de.woff2) format('woff2'), url(assets/fonts/KaTeX_Main-BoldItalic.7649d5.woff) format('woff'), url(assets/fonts/KaTeX_Main-BoldItalic.bc8d96.ttf) format('truetype');
  font-weight: bold;
  font-style: italic;
}
@font-face {
  font-family: 'KaTeX_Main';
  src: url(assets/fonts/KaTeX_Main-Italic.ab751a.woff2) format('woff2'), url(assets/fonts/KaTeX_Main-Italic.e3954f.woff) format('woff'), url(assets/fonts/KaTeX_Main-Italic.44a32a.ttf) format('truetype');
  font-weight: normal;
  font-style: italic;
}
@font-face {
  font-family: 'KaTeX_Main';
  src: url(assets/fonts/KaTeX_Main-Regular.13b3f8.woff2) format('woff2'), url(assets/fonts/KaTeX_Main-Regular.9e75cd.woff) format('woff'), url(assets/fonts/KaTeX_Main-Regular.af7fc7.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Math';
  src: url(assets/fonts/KaTeX_Math-BoldItalic.d5d35e.woff2) format('woff2'), url(assets/fonts/KaTeX_Math-BoldItalic.94810f.woff) format('woff'), url(assets/fonts/KaTeX_Math-BoldItalic.4d6241.ttf) format('truetype');
  font-weight: bold;
  font-style: italic;
}
@font-face {
  font-family: 'KaTeX_Math';
  src: url(assets/fonts/KaTeX_Math-Italic.ffda88.woff2) format('woff2'), url(assets/fonts/KaTeX_Math-Italic.11278d.woff) format('woff'), url(assets/fonts/KaTeX_Math-Italic.cae7ea.ttf) format('truetype');
  font-weight: normal;
  font-style: italic;
}
@font-face {
  font-family: 'KaTeX_SansSerif';
  src: url(assets/fonts/KaTeX_SansSerif-Bold.5a20a4.woff2) format('woff2'), url(assets/fonts/KaTeX_SansSerif-Bold.2946bd.woff) format('woff'), url(assets/fonts/KaTeX_SansSerif-Bold.f0ad0a.ttf) format('truetype');
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_SansSerif';
  src: url(assets/fonts/KaTeX_SansSerif-Italic.e5fc2a.woff2) format('woff2'), url(assets/fonts/KaTeX_SansSerif-Italic.c834ba.woff) format('woff'), url(assets/fonts/KaTeX_SansSerif-Italic.c7feac.ttf) format('truetype');
  font-weight: normal;
  font-style: italic;
}
@font-face {
  font-family: 'KaTeX_SansSerif';
  src: url(assets/fonts/KaTeX_SansSerif-Regular.5bf289.woff2) format('woff2'), url(assets/fonts/KaTeX_SansSerif-Regular.a4fd05.woff) format('woff'), url(assets/fonts/KaTeX_SansSerif-Regular.5af9e1.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Script';
  src: url(assets/fonts/KaTeX_Script-Regular.a1c159.woff2) format('woff2'), url(assets/fonts/KaTeX_Script-Regular.cd3b06.woff) format('woff'), url(assets/fonts/KaTeX_Script-Regular.dd0db7.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Size1';
  src: url(assets/fonts/KaTeX_Size1-Regular.187636.woff2) format('woff2'), url(assets/fonts/KaTeX_Size1-Regular.c4ae0d.woff) format('woff'), url(assets/fonts/KaTeX_Size1-Regular.bbd955.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Size2';
  src: url(assets/fonts/KaTeX_Size2-Regular.f516b7.woff2) format('woff2'), url(assets/fonts/KaTeX_Size2-Regular.635e93.woff) format('woff'), url(assets/fonts/KaTeX_Size2-Regular.d1e8ff.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Size3';
  src: url(assets/fonts/KaTeX_Size3-Regular.1ef7ad.woff2) format('woff2'), url(assets/fonts/KaTeX_Size3-Regular.f32a9f.woff) format('woff'), url(assets/fonts/KaTeX_Size3-Regular.5d6322.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Size4';
  src: url(assets/fonts/KaTeX_Size4-Regular.4f012d.woff2) format('woff2'), url(assets/fonts/KaTeX_Size4-Regular.f668d5.woff) format('woff'), url(assets/fonts/KaTeX_Size4-Regular.1d1325.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'KaTeX_Typewriter';
  src: url(assets/fonts/KaTeX_Typewriter-Regular.4f31d0.woff2) format('woff2'), url(assets/fonts/KaTeX_Typewriter-Regular.d3c8e6.woff) format('woff'), url(assets/fonts/KaTeX_Typewriter-Regular.b1d1af.ttf) format('truetype');
  font-weight: normal;
  font-style: normal;
}
.katex {
  font: normal 1.21em KaTeX_Main, Times New Roman, serif;
  line-height: 1.2;
  text-indent: 0;
  text-rendering: auto;
}
.katex * {
  -ms-high-contrast-adjust: none !important;
}
.katex .katex-version::after {
  content: "0.11.1";
}
.katex .katex-mathml {
  position: absolute;
  clip: rect(1px, 1px, 1px, 1px);
  padding: 0;
  border: 0;
  height: 1px;
  width: 1px;
  overflow: hidden;
}
.katex .katex-html {
  /* \newline is an empty block at top level, between .base elements */
}
.katex .katex-html > .newline {
  display: block;
}
.katex .base {
  position: relative;
  display: inline-block;
  white-space: nowrap;
  width: min-content;
}
.katex .strut {
  display: inline-block;
}
.katex .textbf {
  font-weight: bold;
}
.katex .textit {
  font-style: italic;
}
.katex .textrm {
  font-family: KaTeX_Main;
}
.katex .textsf {
  font-family: KaTeX_SansSerif;
}
.katex .texttt {
  font-family: KaTeX_Typewriter;
}
.katex .mathdefault {
  font-family: KaTeX_Math;
  font-style: italic;
}
.katex .mathit {
  font-family: KaTeX_Main;
  font-style: italic;
}
.katex .mathrm {
  font-style: normal;
}
.katex .mathbf {
  font-family: KaTeX_Main;
  font-weight: bold;
}
.katex .boldsymbol {
  font-family: KaTeX_Math;
  font-weight: bold;
  font-style: italic;
}
.katex .amsrm {
  font-family: KaTeX_AMS;
}
.katex .mathbb,
.katex .textbb {
  font-family: KaTeX_AMS;
}
.katex .mathcal {
  font-family: KaTeX_Caligraphic;
}
.katex .mathfrak,
.katex .textfrak {
  font-family: KaTeX_Fraktur;
}
.katex .mathtt {
  font-family: KaTeX_Typewriter;
}
.katex .mathscr,
.katex .textscr {
  font-family: KaTeX_Script;
}
.katex .mathsf,
.katex .textsf {
  font-family: KaTeX_SansSerif;
}
.katex .mathboldsf,
.katex .textboldsf {
  font-family: KaTeX_SansSerif;
  font-weight: bold;
}
.katex .mathitsf,
.katex .textitsf {
  font-family: KaTeX_SansSerif;
  font-style: italic;
}
.katex .mainrm {
  font-family: KaTeX_Main;
  font-style: normal;
}
.katex .vlist-t {
  display: inline-table;
  table-layout: fixed;
}
.katex .vlist-r {
  display: table-row;
}
.katex .vlist {
  display: table-cell;
  vertical-align: bottom;
  position: relative;
}
.katex .vlist > span {
  display: block;
  height: 0;
  position: relative;
}
.katex .vlist > span > span {
  display: inline-block;
}
.katex .vlist > span > .pstrut {
  overflow: hidden;
  width: 0;
}
.katex .vlist-t2 {
  margin-right: -2px;
}
.katex .vlist-s {
  display: table-cell;
  vertical-align: bottom;
  font-size: 1px;
  width: 2px;
  min-width: 2px;
}
.katex .msupsub {
  text-align: left;
}
.katex .mfrac > span > span {
  text-align: center;
}
.katex .mfrac .frac-line {
  display: inline-block;
  width: 100%;
  border-bottom-style: solid;
}
.katex .mfrac .frac-line,
.katex .overline .overline-line,
.katex .underline .underline-line,
.katex .hline,
.katex .hdashline,
.katex .rule {
  min-height: 1px;
}
.katex .mspace {
  display: inline-block;
}
.katex .llap,
.katex .rlap,
.katex .clap {
  width: 0;
  position: relative;
}
.katex .llap > .inner,
.katex .rlap > .inner,
.katex .clap > .inner {
  position: absolute;
}
.katex .llap > .fix,
.katex .rlap > .fix,
.katex .clap > .fix {
  display: inline-block;
}
.katex .llap > .inner {
  right: 0;
}
.katex .rlap > .inner,
.katex .clap > .inner {
  left: 0;
}
.katex .clap > .inner > span {
  margin-left: -50%;
  margin-right: 50%;
}
.katex .rule {
  display: inline-block;
  border: solid 0;
  position: relative;
}
.katex .overline .overline-line,
.katex .underline .underline-line,
.katex .hline {
  display: inline-block;
  width: 100%;
  border-bottom-style: solid;
}
.katex .hdashline {
  display: inline-block;
  width: 100%;
  border-bottom-style: dashed;
}
.katex .sqrt > .root {
  margin-left: 0.27777778em;
  margin-right: -0.55555556em;
}
.katex .sizing.reset-size1.size1,
.katex .fontsize-ensurer.reset-size1.size1 {
  font-size: 1em;
}
.katex .sizing.reset-size1.size2,
.katex .fontsize-ensurer.reset-size1.size2 {
  font-size: 1.2em;
}
.katex .sizing.reset-size1.size3,
.katex .fontsize-ensurer.reset-size1.size3 {
  font-size: 1.4em;
}
.katex .sizing.reset-size1.size4,
.katex .fontsize-ensurer.reset-size1.size4 {
  font-size: 1.6em;
}
.katex .sizing.reset-size1.size5,
.katex .fontsize-ensurer.reset-size1.size5 {
  font-size: 1.8em;
}
.katex .sizing.reset-size1.size6,
.katex .fontsize-ensurer.reset-size1.size6 {
  font-size: 2em;
}
.katex .sizing.reset-size1.size7,
.katex .fontsize-ensurer.reset-size1.size7 {
  font-size: 2.4em;
}
.katex .sizing.reset-size1.size8,
.katex .fontsize-ensurer.reset-size1.size8 {
  font-size: 2.88em;
}
.katex .sizing.reset-size1.size9,
.katex .fontsize-ensurer.reset-size1.size9 {
  font-size: 3.456em;
}
.katex .sizing.reset-size1.size10,
.katex .fontsize-ensurer.reset-size1.size10 {
  font-size: 4.148em;
}
.katex .sizing.reset-size1.size11,
.katex .fontsize-ensurer.reset-size1.size11 {
  font-size: 4.976em;
}
.katex .sizing.reset-size2.size1,
.katex .fontsize-ensurer.reset-size2.size1 {
  font-size: 0.83333333em;
}
.katex .sizing.reset-size2.size2,
.katex .fontsize-ensurer.reset-size2.size2 {
  font-size: 1em;
}
.katex .sizing.reset-size2.size3,
.katex .fontsize-ensurer.reset-size2.size3 {
  font-size: 1.16666667em;
}
.katex .sizing.reset-size2.size4,
.katex .fontsize-ensurer.reset-size2.size4 {
  font-size: 1.33333333em;
}
.katex .sizing.reset-size2.size5,
.katex .fontsize-ensurer.reset-size2.size5 {
  font-size: 1.5em;
}
.katex .sizing.reset-size2.size6,
.katex .fontsize-ensurer.reset-size2.size6 {
  font-size: 1.66666667em;
}
.katex .sizing.reset-size2.size7,
.katex .fontsize-ensurer.reset-size2.size7 {
  font-size: 2em;
}
.katex .sizing.reset-size2.size8,
.katex .fontsize-ensurer.reset-size2.size8 {
  font-size: 2.4em;
}
.katex .sizing.reset-size2.size9,
.katex .fontsize-ensurer.reset-size2.size9 {
  font-size: 2.88em;
}
.katex .sizing.reset-size2.size10,
.katex .fontsize-ensurer.reset-size2.size10 {
  font-size: 3.45666667em;
}
.katex .sizing.reset-size2.size11,
.katex .fontsize-ensurer.reset-size2.size11 {
  font-size: 4.14666667em;
}
.katex .sizing.reset-size3.size1,
.katex .fontsize-ensurer.reset-size3.size1 {
  font-size: 0.71428571em;
}
.katex .sizing.reset-size3.size2,
.katex .fontsize-ensurer.reset-size3.size2 {
  font-size: 0.85714286em;
}
.katex .sizing.reset-size3.size3,
.katex .fontsize-ensurer.reset-size3.size3 {
  font-size: 1em;
}
.katex .sizing.reset-size3.size4,
.katex .fontsize-ensurer.reset-size3.size4 {
  font-size: 1.14285714em;
}
.katex .sizing.reset-size3.size5,
.katex .fontsize-ensurer.reset-size3.size5 {
  font-size: 1.28571429em;
}
.katex .sizing.reset-size3.size6,
.katex .fontsize-ensurer.reset-size3.size6 {
  font-size: 1.42857143em;
}
.katex .sizing.reset-size3.size7,
.katex .fontsize-ensurer.reset-size3.size7 {
  font-size: 1.71428571em;
}
.katex .sizing.reset-size3.size8,
.katex .fontsize-ensurer.reset-size3.size8 {
  font-size: 2.05714286em;
}
.katex .sizing.reset-size3.size9,
.katex .fontsize-ensurer.reset-size3.size9 {
  font-size: 2.46857143em;
}
.katex .sizing.reset-size3.size10,
.katex .fontsize-ensurer.reset-size3.size10 {
  font-size: 2.96285714em;
}
.katex .sizing.reset-size3.size11,
.katex .fontsize-ensurer.reset-size3.size11 {
  font-size: 3.55428571em;
}
.katex .sizing.reset-size4.size1,
.katex .fontsize-ensurer.reset-size4.size1 {
  font-size: 0.625em;
}
.katex .sizing.reset-size4.size2,
.katex .fontsize-ensurer.reset-size4.size2 {
  font-size: 0.75em;
}
.katex .sizing.reset-size4.size3,
.katex .fontsize-ensurer.reset-size4.size3 {
  font-size: 0.875em;
}
.katex .sizing.reset-size4.size4,
.katex .fontsize-ensurer.reset-size4.size4 {
  font-size: 1em;
}
.katex .sizing.reset-size4.size5,
.katex .fontsize-ensurer.reset-size4.size5 {
  font-size: 1.125em;
}
.katex .sizing.reset-size4.size6,
.katex .fontsize-ensurer.reset-size4.size6 {
  font-size: 1.25em;
}
.katex .sizing.reset-size4.size7,
.katex .fontsize-ensurer.reset-size4.size7 {
  font-size: 1.5em;
}
.katex .sizing.reset-size4.size8,
.katex .fontsize-ensurer.reset-size4.size8 {
  font-size: 1.8em;
}
.katex .sizing.reset-size4.size9,
.katex .fontsize-ensurer.reset-size4.size9 {
  font-size: 2.16em;
}
.katex .sizing.reset-size4.size10,
.katex .fontsize-ensurer.reset-size4.size10 {
  font-size: 2.5925em;
}
.katex .sizing.reset-size4.size11,
.katex .fontsize-ensurer.reset-size4.size11 {
  font-size: 3.11em;
}
.katex .sizing.reset-size5.size1,
.katex .fontsize-ensurer.reset-size5.size1 {
  font-size: 0.55555556em;
}
.katex .sizing.reset-size5.size2,
.katex .fontsize-ensurer.reset-size5.size2 {
  font-size: 0.66666667em;
}
.katex .sizing.reset-size5.size3,
.katex .fontsize-ensurer.reset-size5.size3 {
  font-size: 0.77777778em;
}
.katex .sizing.reset-size5.size4,
.katex .fontsize-ensurer.reset-size5.size4 {
  font-size: 0.88888889em;
}
.katex .sizing.reset-size5.size5,
.katex .fontsize-ensurer.reset-size5.size5 {
  font-size: 1em;
}
.katex .sizing.reset-size5.size6,
.katex .fontsize-ensurer.reset-size5.size6 {
  font-size: 1.11111111em;
}
.katex .sizing.reset-size5.size7,
.katex .fontsize-ensurer.reset-size5.size7 {
  font-size: 1.33333333em;
}
.katex .sizing.reset-size5.size8,
.katex .fontsize-ensurer.reset-size5.size8 {
  font-size: 1.6em;
}
.katex .sizing.reset-size5.size9,
.katex .fontsize-ensurer.reset-size5.size9 {
  font-size: 1.92em;
}
.katex .sizing.reset-size5.size10,
.katex .fontsize-ensurer.reset-size5.size10 {
  font-size: 2.30444444em;
}
.katex .sizing.reset-size5.size11,
.katex .fontsize-ensurer.reset-size5.size11 {
  font-size: 2.76444444em;
}
.katex .sizing.reset-size6.size1,
.katex .fontsize-ensurer.reset-size6.size1 {
  font-size: 0.5em;
}
.katex .sizing.reset-size6.size2,
.katex .fontsize-ensurer.reset-size6.size2 {
  font-size: 0.6em;
}
.katex .sizing.reset-size6.size3,
.katex .fontsize-ensurer.reset-size6.size3 {
  font-size: 0.7em;
}
.katex .sizing.reset-size6.size4,
.katex .fontsize-ensurer.reset-size6.size4 {
  font-size: 0.8em;
}
.katex .sizing.reset-size6.size5,
.katex .fontsize-ensurer.reset-size6.size5 {
  font-size: 0.9em;
}
.katex .sizing.reset-size6.size6,
.katex .fontsize-ensurer.reset-size6.size6 {
  font-size: 1em;
}
.katex .sizing.reset-size6.size7,
.katex .fontsize-ensurer.reset-size6.size7 {
  font-size: 1.2em;
}
.katex .sizing.reset-size6.size8,
.katex .fontsize-ensurer.reset-size6.size8 {
  font-size: 1.44em;
}
.katex .sizing.reset-size6.size9,
.katex .fontsize-ensurer.reset-size6.size9 {
  font-size: 1.728em;
}
.katex .sizing.reset-size6.size10,
.katex .fontsize-ensurer.reset-size6.size10 {
  font-size: 2.074em;
}
.katex .sizing.reset-size6.size11,
.katex .fontsize-ensurer.reset-size6.size11 {
  font-size: 2.488em;
}
.katex .sizing.reset-size7.size1,
.katex .fontsize-ensurer.reset-size7.size1 {
  font-size: 0.41666667em;
}
.katex .sizing.reset-size7.size2,
.katex .fontsize-ensurer.reset-size7.size2 {
  font-size: 0.5em;
}
.katex .sizing.reset-size7.size3,
.katex .fontsize-ensurer.reset-size7.size3 {
  font-size: 0.58333333em;
}
.katex .sizing.reset-size7.size4,
.katex .fontsize-ensurer.reset-size7.size4 {
  font-size: 0.66666667em;
}
.katex .sizing.reset-size7.size5,
.katex .fontsize-ensurer.reset-size7.size5 {
  font-size: 0.75em;
}
.katex .sizing.reset-size7.size6,
.katex .fontsize-ensurer.reset-size7.size6 {
  font-size: 0.83333333em;
}
.katex .sizing.reset-size7.size7,
.katex .fontsize-ensurer.reset-size7.size7 {
  font-size: 1em;
}
.katex .sizing.reset-size7.size8,
.katex .fontsize-ensurer.reset-size7.size8 {
  font-size: 1.2em;
}
.katex .sizing.reset-size7.size9,
.katex .fontsize-ensurer.reset-size7.size9 {
  font-size: 1.44em;
}
.katex .sizing.reset-size7.size10,
.katex .fontsize-ensurer.reset-size7.size10 {
  font-size: 1.72833333em;
}
.katex .sizing.reset-size7.size11,
.katex .fontsize-ensurer.reset-size7.size11 {
  font-size: 2.07333333em;
}
.katex .sizing.reset-size8.size1,
.katex .fontsize-ensurer.reset-size8.size1 {
  font-size: 0.34722222em;
}
.katex .sizing.reset-size8.size2,
.katex .fontsize-ensurer.reset-size8.size2 {
  font-size: 0.41666667em;
}
.katex .sizing.reset-size8.size3,
.katex .fontsize-ensurer.reset-size8.size3 {
  font-size: 0.48611111em;
}
.katex .sizing.reset-size8.size4,
.katex .fontsize-ensurer.reset-size8.size4 {
  font-size: 0.55555556em;
}
.katex .sizing.reset-size8.size5,
.katex .fontsize-ensurer.reset-size8.size5 {
  font-size: 0.625em;
}
.katex .sizing.reset-size8.size6,
.katex .fontsize-ensurer.reset-size8.size6 {
  font-size: 0.69444444em;
}
.katex .sizing.reset-size8.size7,
.katex .fontsize-ensurer.reset-size8.size7 {
  font-size: 0.83333333em;
}
.katex .sizing.reset-size8.size8,
.katex .fontsize-ensurer.reset-size8.size8 {
  font-size: 1em;
}
.katex .sizing.reset-size8.size9,
.katex .fontsize-ensurer.reset-size8.size9 {
  font-size: 1.2em;
}
.katex .sizing.reset-size8.size10,
.katex .fontsize-ensurer.reset-size8.size10 {
  font-size: 1.44027778em;
}
.katex .sizing.reset-size8.size11,
.katex .fontsize-ensurer.reset-size8.size11 {
  font-size: 1.72777778em;
}
.katex .sizing.reset-size9.size1,
.katex .fontsize-ensurer.reset-size9.size1 {
  font-size: 0.28935185em;
}
.katex .sizing.reset-size9.size2,
.katex .fontsize-ensurer.reset-size9.size2 {
  font-size: 0.34722222em;
}
.katex .sizing.reset-size9.size3,
.katex .fontsize-ensurer.reset-size9.size3 {
  font-size: 0.40509259em;
}
.katex .sizing.reset-size9.size4,
.katex .fontsize-ensurer.reset-size9.size4 {
  font-size: 0.46296296em;
}
.katex .sizing.reset-size9.size5,
.katex .fontsize-ensurer.reset-size9.size5 {
  font-size: 0.52083333em;
}
.katex .sizing.reset-size9.size6,
.katex .fontsize-ensurer.reset-size9.size6 {
  font-size: 0.5787037em;
}
.katex .sizing.reset-size9.size7,
.katex .fontsize-ensurer.reset-size9.size7 {
  font-size: 0.69444444em;
}
.katex .sizing.reset-size9.size8,
.katex .fontsize-ensurer.reset-size9.size8 {
  font-size: 0.83333333em;
}
.katex .sizing.reset-size9.size9,
.katex .fontsize-ensurer.reset-size9.size9 {
  font-size: 1em;
}
.katex .sizing.reset-size9.size10,
.katex .fontsize-ensurer.reset-size9.size10 {
  font-size: 1.20023148em;
}
.katex .sizing.reset-size9.size11,
.katex .fontsize-ensurer.reset-size9.size11 {
  font-size: 1.43981481em;
}
.katex .sizing.reset-size10.size1,
.katex .fontsize-ensurer.reset-size10.size1 {
  font-size: 0.24108004em;
}
.katex .sizing.reset-size10.size2,
.katex .fontsize-ensurer.reset-size10.size2 {
  font-size: 0.28929605em;
}
.katex .sizing.reset-size10.size3,
.katex .fontsize-ensurer.reset-size10.size3 {
  font-size: 0.33751205em;
}
.katex .sizing.reset-size10.size4,
.katex .fontsize-ensurer.reset-size10.size4 {
  font-size: 0.38572806em;
}
.katex .sizing.reset-size10.size5,
.katex .fontsize-ensurer.reset-size10.size5 {
  font-size: 0.43394407em;
}
.katex .sizing.reset-size10.size6,
.katex .fontsize-ensurer.reset-size10.size6 {
  font-size: 0.48216008em;
}
.katex .sizing.reset-size10.size7,
.katex .fontsize-ensurer.reset-size10.size7 {
  font-size: 0.57859209em;
}
.katex .sizing.reset-size10.size8,
.katex .fontsize-ensurer.reset-size10.size8 {
  font-size: 0.69431051em;
}
.katex .sizing.reset-size10.size9,
.katex .fontsize-ensurer.reset-size10.size9 {
  font-size: 0.83317261em;
}
.katex .sizing.reset-size10.size10,
.katex .fontsize-ensurer.reset-size10.size10 {
  font-size: 1em;
}
.katex .sizing.reset-size10.size11,
.katex .fontsize-ensurer.reset-size10.size11 {
  font-size: 1.19961427em;
}
.katex .sizing.reset-size11.size1,
.katex .fontsize-ensurer.reset-size11.size1 {
  font-size: 0.20096463em;
}
.katex .sizing.reset-size11.size2,
.katex .fontsize-ensurer.reset-size11.size2 {
  font-size: 0.24115756em;
}
.katex .sizing.reset-size11.size3,
.katex .fontsize-ensurer.reset-size11.size3 {
  font-size: 0.28135048em;
}
.katex .sizing.reset-size11.size4,
.katex .fontsize-ensurer.reset-size11.size4 {
  font-size: 0.32154341em;
}
.katex .sizing.reset-size11.size5,
.katex .fontsize-ensurer.reset-size11.size5 {
  font-size: 0.36173633em;
}
.katex .sizing.reset-size11.size6,
.katex .fontsize-ensurer.reset-size11.size6 {
  font-size: 0.40192926em;
}
.katex .sizing.reset-size11.size7,
.katex .fontsize-ensurer.reset-size11.size7 {
  font-size: 0.48231511em;
}
.katex .sizing.reset-size11.size8,
.katex .fontsize-ensurer.reset-size11.size8 {
  font-size: 0.57877814em;
}
.katex .sizing.reset-size11.size9,
.katex .fontsize-ensurer.reset-size11.size9 {
  font-size: 0.69453376em;
}
.katex .sizing.reset-size11.size10,
.katex .fontsize-ensurer.reset-size11.size10 {
  font-size: 0.83360129em;
}
.katex .sizing.reset-size11.size11,
.katex .fontsize-ensurer.reset-size11.size11 {
  font-size: 1em;
}
.katex .delimsizing.size1 {
  font-family: KaTeX_Size1;
}
.katex .delimsizing.size2 {
  font-family: KaTeX_Size2;
}
.katex .delimsizing.size3 {
  font-family: KaTeX_Size3;
}
.katex .delimsizing.size4 {
  font-family: KaTeX_Size4;
}
.katex .delimsizing.mult .delim-size1 > span {
  font-family: KaTeX_Size1;
}
.katex .delimsizing.mult .delim-size4 > span {
  font-family: KaTeX_Size4;
}
.katex .nulldelimiter {
  display: inline-block;
  width: 0.12em;
}
.katex .delimcenter {
  position: relative;
}
.katex .op-symbol {
  position: relative;
}
.katex .op-symbol.small-op {
  font-family: KaTeX_Size1;
}
.katex .op-symbol.large-op {
  font-family: KaTeX_Size2;
}
.katex .op-limits > .vlist-t {
  text-align: center;
}
.katex .accent > .vlist-t {
  text-align: center;
}
.katex .accent .accent-body {
  position: relative;
}
.katex .accent .accent-body:not(.accent-full) {
  width: 0;
}
.katex .overlay {
  display: block;
}
.katex .mtable .vertical-separator {
  display: inline-block;
  min-width: 1px;
}
.katex .mtable .arraycolsep {
  display: inline-block;
}
.katex .mtable .col-align-c > .vlist-t {
  text-align: center;
}
.katex .mtable .col-align-l > .vlist-t {
  text-align: left;
}
.katex .mtable .col-align-r > .vlist-t {
  text-align: right;
}
.katex .svg-align {
  text-align: left;
}
.katex svg {
  display: block;
  position: absolute;
  width: 100%;
  height: inherit;
  fill: currentColor;
  stroke: currentColor;
  fill-rule: nonzero;
  fill-opacity: 1;
  stroke-width: 1;
  stroke-linecap: butt;
  stroke-linejoin: miter;
  stroke-miterlimit: 4;
  stroke-dasharray: none;
  stroke-dashoffset: 0;
  stroke-opacity: 1;
}
.katex svg path {
  stroke: none;
}
.katex img {
  border-style: none;
  min-width: 0;
  min-height: 0;
  max-width: none;
  max-height: none;
}
.katex .stretchy {
  width: 100%;
  display: block;
  position: relative;
  overflow: hidden;
}
.katex .stretchy::before,
.katex .stretchy::after {
  content: "";
}
.katex .hide-tail {
  width: 100%;
  position: relative;
  overflow: hidden;
}
.katex .halfarrow-left {
  position: absolute;
  left: 0;
  width: 50.2%;
  overflow: hidden;
}
.katex .halfarrow-right {
  position: absolute;
  right: 0;
  width: 50.2%;
  overflow: hidden;
}
.katex .brace-left {
  position: absolute;
  left: 0;
  width: 25.1%;
  overflow: hidden;
}
.katex .brace-center {
  position: absolute;
  left: 25%;
  width: 50%;
  overflow: hidden;
}
.katex .brace-right {
  position: absolute;
  right: 0;
  width: 25.1%;
  overflow: hidden;
}
.katex .x-arrow-pad {
  padding: 0 0.5em;
}
.katex .x-arrow,
.katex .mover,
.katex .munder {
  text-align: center;
}
.katex .boxpad {
  padding: 0 0.3em 0 0.3em;
}
.katex .fbox,
.katex .fcolorbox {
  box-sizing: border-box;
  border: 0.04em solid;
}
.katex .cancel-pad {
  padding: 0 0.2em 0 0.2em;
}
.katex .cancel-lap {
  margin-left: -0.2em;
  margin-right: -0.2em;
}
.katex .sout {
  border-bottom-style: solid;
  border-bottom-width: 0.08em;
}
.katex-display {
  display: block;
  margin: 1em 0;
  text-align: center;
}
.katex-display > .katex {
  display: block;
  text-align: center;
  white-space: nowrap;
}
.katex-display > .katex > .katex-html {
  display: block;
  position: relative;
}
.katex-display > .katex > .katex-html > .tag {
  position: absolute;
  right: 0;
}
.katex-display.leqno > .katex > .katex-html > .tag {
  left: 0;
  right: auto;
}
.katex-display.fleqn > .katex {
  text-align: left;
}


/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9rYXRleC9kaXN0L2thdGV4LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQSxvRUFBb0U7QUFDcEU7RUFDRSx3QkFBd0I7RUFDeEIsZ0xBQThKO0VBQzlKLG1CQUFtQjtFQUNuQixrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLGdDQUFnQztFQUNoQyxnTEFBNks7RUFDN0ssaUJBQWlCO0VBQ2pCLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UsZ0NBQWdDO0VBQ2hDLGdMQUFzTDtFQUN0TCxtQkFBbUI7RUFDbkIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSw0QkFBNEI7RUFDNUIsa0xBQWlLO0VBQ2pLLGlCQUFpQjtFQUNqQixrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLDRCQUE0QjtFQUM1QixtTEFBMEs7RUFDMUssbUJBQW1CO0VBQ25CLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UseUJBQXlCO0VBQ3pCLG1MQUF3SjtFQUN4SixpQkFBaUI7RUFDakIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSx5QkFBeUI7RUFDekIsbUxBQTBLO0VBQzFLLGlCQUFpQjtFQUNqQixrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLHlCQUF5QjtFQUN6QixtTEFBOEo7RUFDOUosbUJBQW1CO0VBQ25CLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UseUJBQXlCO0VBQ3pCLG1MQUFpSztFQUNqSyxtQkFBbUI7RUFDbkIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSx5QkFBeUI7RUFDekIsbUxBQTBLO0VBQzFLLGlCQUFpQjtFQUNqQixrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLHlCQUF5QjtFQUN6QixtTEFBOEo7RUFDOUosbUJBQW1CO0VBQ25CLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UsOEJBQThCO0VBQzlCLG1MQUF1SztFQUN2SyxpQkFBaUI7RUFDakIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSw4QkFBOEI7RUFDOUIsbUxBQTZLO0VBQzdLLG1CQUFtQjtFQUNuQixrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLDhCQUE4QjtFQUM5QixtTEFBZ0w7RUFDaEwsbUJBQW1CO0VBQ25CLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UsMkJBQTJCO0VBQzNCLG1MQUF1SztFQUN2SyxtQkFBbUI7RUFDbkIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSwwQkFBMEI7RUFDMUIsbUxBQW9LO0VBQ3BLLG1CQUFtQjtFQUNuQixrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLDBCQUEwQjtFQUMxQixtTEFBb0s7RUFDcEssbUJBQW1CO0VBQ25CLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UsMEJBQTBCO0VBQzFCLG1MQUFvSztFQUNwSyxtQkFBbUI7RUFDbkIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSwwQkFBMEI7RUFDMUIsbUxBQW9LO0VBQ3BLLG1CQUFtQjtFQUNuQixrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLCtCQUErQjtFQUMvQixtTEFBbUw7RUFDbkwsbUJBQW1CO0VBQ25CLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0Usc0RBQXNEO0VBQ3RELGdCQUFnQjtFQUNoQixjQUFjO0VBQ2Qsb0JBQW9CO0FBQ3RCO0FBQ0E7RUFDRSx5Q0FBeUM7QUFDM0M7QUFDQTtFQUNFLGlCQUFpQjtBQUNuQjtBQUNBO0VBQ0Usa0JBQWtCO0VBQ2xCLDhCQUE4QjtFQUM5QixVQUFVO0VBQ1YsU0FBUztFQUNULFdBQVc7RUFDWCxVQUFVO0VBQ1YsZ0JBQWdCO0FBQ2xCO0FBQ0E7RUFDRSxvRUFBb0U7QUFDdEU7QUFDQTtFQUNFLGNBQWM7QUFDaEI7QUFDQTtFQUNFLGtCQUFrQjtFQUNsQixxQkFBcUI7RUFDckIsbUJBQW1CO0VBQ25CLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UscUJBQXFCO0FBQ3ZCO0FBQ0E7RUFDRSxpQkFBaUI7QUFDbkI7QUFDQTtFQUNFLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UsdUJBQXVCO0FBQ3pCO0FBQ0E7RUFDRSw0QkFBNEI7QUFDOUI7QUFDQTtFQUNFLDZCQUE2QjtBQUMvQjtBQUNBO0VBQ0UsdUJBQXVCO0VBQ3ZCLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UsdUJBQXVCO0VBQ3ZCLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0Usa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSx1QkFBdUI7RUFDdkIsaUJBQWlCO0FBQ25CO0FBQ0E7RUFDRSx1QkFBdUI7RUFDdkIsaUJBQWlCO0VBQ2pCLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0Usc0JBQXNCO0FBQ3hCO0FBQ0E7O0VBRUUsc0JBQXNCO0FBQ3hCO0FBQ0E7RUFDRSw4QkFBOEI7QUFDaEM7QUFDQTs7RUFFRSwwQkFBMEI7QUFDNUI7QUFDQTtFQUNFLDZCQUE2QjtBQUMvQjtBQUNBOztFQUVFLHlCQUF5QjtBQUMzQjtBQUNBOztFQUVFLDRCQUE0QjtBQUM5QjtBQUNBOztFQUVFLDRCQUE0QjtFQUM1QixpQkFBaUI7QUFDbkI7QUFDQTs7RUFFRSw0QkFBNEI7RUFDNUIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSx1QkFBdUI7RUFDdkIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSxxQkFBcUI7RUFDckIsbUJBQW1CO0FBQ3JCO0FBQ0E7RUFDRSxrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLG1CQUFtQjtFQUNuQixzQkFBc0I7RUFDdEIsa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSxjQUFjO0VBQ2QsU0FBUztFQUNULGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UscUJBQXFCO0FBQ3ZCO0FBQ0E7RUFDRSxnQkFBZ0I7RUFDaEIsUUFBUTtBQUNWO0FBQ0E7RUFDRSxrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLG1CQUFtQjtFQUNuQixzQkFBc0I7RUFDdEIsY0FBYztFQUNkLFVBQVU7RUFDVixjQUFjO0FBQ2hCO0FBQ0E7RUFDRSxnQkFBZ0I7QUFDbEI7QUFDQTtFQUNFLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UscUJBQXFCO0VBQ3JCLFdBQVc7RUFDWCwwQkFBMEI7QUFDNUI7QUFDQTs7Ozs7O0VBTUUsZUFBZTtBQUNqQjtBQUNBO0VBQ0UscUJBQXFCO0FBQ3ZCO0FBQ0E7OztFQUdFLFFBQVE7RUFDUixrQkFBa0I7QUFDcEI7QUFDQTs7O0VBR0Usa0JBQWtCO0FBQ3BCO0FBQ0E7OztFQUdFLHFCQUFxQjtBQUN2QjtBQUNBO0VBQ0UsUUFBUTtBQUNWO0FBQ0E7O0VBRUUsT0FBTztBQUNUO0FBQ0E7RUFDRSxpQkFBaUI7RUFDakIsaUJBQWlCO0FBQ25CO0FBQ0E7RUFDRSxxQkFBcUI7RUFDckIsZUFBZTtFQUNmLGtCQUFrQjtBQUNwQjtBQUNBOzs7RUFHRSxxQkFBcUI7RUFDckIsV0FBVztFQUNYLDBCQUEwQjtBQUM1QjtBQUNBO0VBQ0UscUJBQXFCO0VBQ3JCLFdBQVc7RUFDWCwyQkFBMkI7QUFDN0I7QUFDQTtFQUNFLHlCQUF5QjtFQUN6QiwyQkFBMkI7QUFDN0I7QUFDQTs7RUFFRSxjQUFjO0FBQ2hCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsY0FBYztBQUNoQjtBQUNBOztFQUVFLGdCQUFnQjtBQUNsQjtBQUNBOztFQUVFLGlCQUFpQjtBQUNuQjtBQUNBOztFQUVFLGtCQUFrQjtBQUNwQjtBQUNBOztFQUVFLGtCQUFrQjtBQUNwQjtBQUNBOztFQUVFLGtCQUFrQjtBQUNwQjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLGNBQWM7QUFDaEI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSxnQkFBZ0I7QUFDbEI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSxjQUFjO0FBQ2hCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsaUJBQWlCO0FBQ25CO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsY0FBYztBQUNoQjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLGtCQUFrQjtBQUNwQjtBQUNBOztFQUVFLGlCQUFpQjtBQUNuQjtBQUNBOztFQUVFLGtCQUFrQjtBQUNwQjtBQUNBOztFQUVFLGNBQWM7QUFDaEI7QUFDQTs7RUFFRSxrQkFBa0I7QUFDcEI7QUFDQTs7RUFFRSxpQkFBaUI7QUFDbkI7QUFDQTs7RUFFRSxnQkFBZ0I7QUFDbEI7QUFDQTs7RUFFRSxnQkFBZ0I7QUFDbEI7QUFDQTs7RUFFRSxpQkFBaUI7QUFDbkI7QUFDQTs7RUFFRSxtQkFBbUI7QUFDckI7QUFDQTs7RUFFRSxpQkFBaUI7QUFDbkI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSxjQUFjO0FBQ2hCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsaUJBQWlCO0FBQ25CO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsY0FBYztBQUNoQjtBQUNBOztFQUVFLGdCQUFnQjtBQUNsQjtBQUNBOztFQUVFLGlCQUFpQjtBQUNuQjtBQUNBOztFQUVFLGtCQUFrQjtBQUNwQjtBQUNBOztFQUVFLGtCQUFrQjtBQUNwQjtBQUNBOztFQUVFLGtCQUFrQjtBQUNwQjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLGdCQUFnQjtBQUNsQjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLGlCQUFpQjtBQUNuQjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLGNBQWM7QUFDaEI7QUFDQTs7RUFFRSxnQkFBZ0I7QUFDbEI7QUFDQTs7RUFFRSxpQkFBaUI7QUFDbkI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSxrQkFBa0I7QUFDcEI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSxjQUFjO0FBQ2hCO0FBQ0E7O0VBRUUsZ0JBQWdCO0FBQ2xCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsc0JBQXNCO0FBQ3hCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsdUJBQXVCO0FBQ3pCO0FBQ0E7O0VBRUUsY0FBYztBQUNoQjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLHVCQUF1QjtBQUN6QjtBQUNBOztFQUVFLGNBQWM7QUFDaEI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSx1QkFBdUI7QUFDekI7QUFDQTs7RUFFRSxjQUFjO0FBQ2hCO0FBQ0E7RUFDRSx3QkFBd0I7QUFDMUI7QUFDQTtFQUNFLHdCQUF3QjtBQUMxQjtBQUNBO0VBQ0Usd0JBQXdCO0FBQzFCO0FBQ0E7RUFDRSx3QkFBd0I7QUFDMUI7QUFDQTtFQUNFLHdCQUF3QjtBQUMxQjtBQUNBO0VBQ0Usd0JBQXdCO0FBQzFCO0FBQ0E7RUFDRSxxQkFBcUI7RUFDckIsYUFBYTtBQUNmO0FBQ0E7RUFDRSxrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0Usd0JBQXdCO0FBQzFCO0FBQ0E7RUFDRSx3QkFBd0I7QUFDMUI7QUFDQTtFQUNFLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0Usa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSxrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLFFBQVE7QUFDVjtBQUNBO0VBQ0UsY0FBYztBQUNoQjtBQUNBO0VBQ0UscUJBQXFCO0VBQ3JCLGNBQWM7QUFDaEI7QUFDQTtFQUNFLHFCQUFxQjtBQUN2QjtBQUNBO0VBQ0Usa0JBQWtCO0FBQ3BCO0FBQ0E7RUFDRSxnQkFBZ0I7QUFDbEI7QUFDQTtFQUNFLGlCQUFpQjtBQUNuQjtBQUNBO0VBQ0UsZ0JBQWdCO0FBQ2xCO0FBQ0E7RUFDRSxjQUFjO0VBQ2Qsa0JBQWtCO0VBQ2xCLFdBQVc7RUFDWCxlQUFlO0VBQ2Ysa0JBQWtCO0VBQ2xCLG9CQUFvQjtFQUNwQixrQkFBa0I7RUFDbEIsZUFBZTtFQUNmLGVBQWU7RUFDZixvQkFBb0I7RUFDcEIsc0JBQXNCO0VBQ3RCLG9CQUFvQjtFQUNwQixzQkFBc0I7RUFDdEIsb0JBQW9CO0VBQ3BCLGlCQUFpQjtBQUNuQjtBQUNBO0VBQ0UsWUFBWTtBQUNkO0FBQ0E7RUFDRSxrQkFBa0I7RUFDbEIsWUFBWTtFQUNaLGFBQWE7RUFDYixlQUFlO0VBQ2YsZ0JBQWdCO0FBQ2xCO0FBQ0E7RUFDRSxXQUFXO0VBQ1gsY0FBYztFQUNkLGtCQUFrQjtFQUNsQixnQkFBZ0I7QUFDbEI7QUFDQTs7RUFFRSxXQUFXO0FBQ2I7QUFDQTtFQUNFLFdBQVc7RUFDWCxrQkFBa0I7RUFDbEIsZ0JBQWdCO0FBQ2xCO0FBQ0E7RUFDRSxrQkFBa0I7RUFDbEIsT0FBTztFQUNQLFlBQVk7RUFDWixnQkFBZ0I7QUFDbEI7QUFDQTtFQUNFLGtCQUFrQjtFQUNsQixRQUFRO0VBQ1IsWUFBWTtFQUNaLGdCQUFnQjtBQUNsQjtBQUNBO0VBQ0Usa0JBQWtCO0VBQ2xCLE9BQU87RUFDUCxZQUFZO0VBQ1osZ0JBQWdCO0FBQ2xCO0FBQ0E7RUFDRSxrQkFBa0I7RUFDbEIsU0FBUztFQUNULFVBQVU7RUFDVixnQkFBZ0I7QUFDbEI7QUFDQTtFQUNFLGtCQUFrQjtFQUNsQixRQUFRO0VBQ1IsWUFBWTtFQUNaLGdCQUFnQjtBQUNsQjtBQUNBO0VBQ0UsZ0JBQWdCO0FBQ2xCO0FBQ0E7OztFQUdFLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0Usd0JBQXdCO0FBQzFCO0FBQ0E7O0VBRUUsc0JBQXNCO0VBQ3RCLG9CQUFvQjtBQUN0QjtBQUNBO0VBQ0Usd0JBQXdCO0FBQzFCO0FBQ0E7RUFDRSxtQkFBbUI7RUFDbkIsb0JBQW9CO0FBQ3RCO0FBQ0E7RUFDRSwwQkFBMEI7RUFDMUIsMkJBQTJCO0FBQzdCO0FBQ0E7RUFDRSxjQUFjO0VBQ2QsYUFBYTtFQUNiLGtCQUFrQjtBQUNwQjtBQUNBO0VBQ0UsY0FBYztFQUNkLGtCQUFrQjtFQUNsQixtQkFBbUI7QUFDckI7QUFDQTtFQUNFLGNBQWM7RUFDZCxrQkFBa0I7QUFDcEI7QUFDQTtFQUNFLGtCQUFrQjtFQUNsQixRQUFRO0FBQ1Y7QUFDQTtFQUNFLE9BQU87RUFDUCxXQUFXO0FBQ2I7QUFDQTtFQUNFLGdCQUFnQjtBQUNsQiIsInNvdXJjZXNDb250ZW50IjpbIi8qIHN0eWxlbGludC1kaXNhYmxlIGZvbnQtZmFtaWx5LW5vLW1pc3NpbmctZ2VuZXJpYy1mYW1pbHkta2V5d29yZCAqL1xuQGZvbnQtZmFjZSB7XG4gIGZvbnQtZmFtaWx5OiAnS2FUZVhfQU1TJztcbiAgc3JjOiB1cmwoZm9udHMvS2FUZVhfQU1TLVJlZ3VsYXIud29mZjIpIGZvcm1hdCgnd29mZjInKSwgdXJsKGZvbnRzL0thVGVYX0FNUy1SZWd1bGFyLndvZmYpIGZvcm1hdCgnd29mZicpLCB1cmwoZm9udHMvS2FUZVhfQU1TLVJlZ3VsYXIudHRmKSBmb3JtYXQoJ3RydWV0eXBlJyk7XG4gIGZvbnQtd2VpZ2h0OiBub3JtYWw7XG4gIGZvbnQtc3R5bGU6IG5vcm1hbDtcbn1cbkBmb250LWZhY2Uge1xuICBmb250LWZhbWlseTogJ0thVGVYX0NhbGlncmFwaGljJztcbiAgc3JjOiB1cmwoZm9udHMvS2FUZVhfQ2FsaWdyYXBoaWMtQm9sZC53b2ZmMikgZm9ybWF0KCd3b2ZmMicpLCB1cmwoZm9udHMvS2FUZVhfQ2FsaWdyYXBoaWMtQm9sZC53b2ZmKSBmb3JtYXQoJ3dvZmYnKSwgdXJsKGZvbnRzL0thVGVYX0NhbGlncmFwaGljLUJvbGQudHRmKSBmb3JtYXQoJ3RydWV0eXBlJyk7XG4gIGZvbnQtd2VpZ2h0OiBib2xkO1xuICBmb250LXN0eWxlOiBub3JtYWw7XG59XG5AZm9udC1mYWNlIHtcbiAgZm9udC1mYW1pbHk6ICdLYVRlWF9DYWxpZ3JhcGhpYyc7XG4gIHNyYzogdXJsKGZvbnRzL0thVGVYX0NhbGlncmFwaGljLVJlZ3VsYXIud29mZjIpIGZvcm1hdCgnd29mZjInKSwgdXJsKGZvbnRzL0thVGVYX0NhbGlncmFwaGljLVJlZ3VsYXIud29mZikgZm9ybWF0KCd3b2ZmJyksIHVybChmb250cy9LYVRlWF9DYWxpZ3JhcGhpYy1SZWd1bGFyLnR0ZikgZm9ybWF0KCd0cnVldHlwZScpO1xuICBmb250LXdlaWdodDogbm9ybWFsO1xuICBmb250LXN0eWxlOiBub3JtYWw7XG59XG5AZm9udC1mYWNlIHtcbiAgZm9udC1mYW1pbHk6ICdLYVRlWF9GcmFrdHVyJztcbiAgc3JjOiB1cmwoZm9udHMvS2FUZVhfRnJha3R1ci1Cb2xkLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9GcmFrdHVyLUJvbGQud29mZikgZm9ybWF0KCd3b2ZmJyksIHVybChmb250cy9LYVRlWF9GcmFrdHVyLUJvbGQudHRmKSBmb3JtYXQoJ3RydWV0eXBlJyk7XG4gIGZvbnQtd2VpZ2h0OiBib2xkO1xuICBmb250LXN0eWxlOiBub3JtYWw7XG59XG5AZm9udC1mYWNlIHtcbiAgZm9udC1mYW1pbHk6ICdLYVRlWF9GcmFrdHVyJztcbiAgc3JjOiB1cmwoZm9udHMvS2FUZVhfRnJha3R1ci1SZWd1bGFyLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9GcmFrdHVyLVJlZ3VsYXIud29mZikgZm9ybWF0KCd3b2ZmJyksIHVybChmb250cy9LYVRlWF9GcmFrdHVyLVJlZ3VsYXIudHRmKSBmb3JtYXQoJ3RydWV0eXBlJyk7XG4gIGZvbnQtd2VpZ2h0OiBub3JtYWw7XG4gIGZvbnQtc3R5bGU6IG5vcm1hbDtcbn1cbkBmb250LWZhY2Uge1xuICBmb250LWZhbWlseTogJ0thVGVYX01haW4nO1xuICBzcmM6IHVybChmb250cy9LYVRlWF9NYWluLUJvbGQud29mZjIpIGZvcm1hdCgnd29mZjInKSwgdXJsKGZvbnRzL0thVGVYX01haW4tQm9sZC53b2ZmKSBmb3JtYXQoJ3dvZmYnKSwgdXJsKGZvbnRzL0thVGVYX01haW4tQm9sZC50dGYpIGZvcm1hdCgndHJ1ZXR5cGUnKTtcbiAgZm9udC13ZWlnaHQ6IGJvbGQ7XG4gIGZvbnQtc3R5bGU6IG5vcm1hbDtcbn1cbkBmb250LWZhY2Uge1xuICBmb250LWZhbWlseTogJ0thVGVYX01haW4nO1xuICBzcmM6IHVybChmb250cy9LYVRlWF9NYWluLUJvbGRJdGFsaWMud29mZjIpIGZvcm1hdCgnd29mZjInKSwgdXJsKGZvbnRzL0thVGVYX01haW4tQm9sZEl0YWxpYy53b2ZmKSBmb3JtYXQoJ3dvZmYnKSwgdXJsKGZvbnRzL0thVGVYX01haW4tQm9sZEl0YWxpYy50dGYpIGZvcm1hdCgndHJ1ZXR5cGUnKTtcbiAgZm9udC13ZWlnaHQ6IGJvbGQ7XG4gIGZvbnQtc3R5bGU6IGl0YWxpYztcbn1cbkBmb250LWZhY2Uge1xuICBmb250LWZhbWlseTogJ0thVGVYX01haW4nO1xuICBzcmM6IHVybChmb250cy9LYVRlWF9NYWluLUl0YWxpYy53b2ZmMikgZm9ybWF0KCd3b2ZmMicpLCB1cmwoZm9udHMvS2FUZVhfTWFpbi1JdGFsaWMud29mZikgZm9ybWF0KCd3b2ZmJyksIHVybChmb250cy9LYVRlWF9NYWluLUl0YWxpYy50dGYpIGZvcm1hdCgndHJ1ZXR5cGUnKTtcbiAgZm9udC13ZWlnaHQ6IG5vcm1hbDtcbiAgZm9udC1zdHlsZTogaXRhbGljO1xufVxuQGZvbnQtZmFjZSB7XG4gIGZvbnQtZmFtaWx5OiAnS2FUZVhfTWFpbic7XG4gIHNyYzogdXJsKGZvbnRzL0thVGVYX01haW4tUmVndWxhci53b2ZmMikgZm9ybWF0KCd3b2ZmMicpLCB1cmwoZm9udHMvS2FUZVhfTWFpbi1SZWd1bGFyLndvZmYpIGZvcm1hdCgnd29mZicpLCB1cmwoZm9udHMvS2FUZVhfTWFpbi1SZWd1bGFyLnR0ZikgZm9ybWF0KCd0cnVldHlwZScpO1xuICBmb250LXdlaWdodDogbm9ybWFsO1xuICBmb250LXN0eWxlOiBub3JtYWw7XG59XG5AZm9udC1mYWNlIHtcbiAgZm9udC1mYW1pbHk6ICdLYVRlWF9NYXRoJztcbiAgc3JjOiB1cmwoZm9udHMvS2FUZVhfTWF0aC1Cb2xkSXRhbGljLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9NYXRoLUJvbGRJdGFsaWMud29mZikgZm9ybWF0KCd3b2ZmJyksIHVybChmb250cy9LYVRlWF9NYXRoLUJvbGRJdGFsaWMudHRmKSBmb3JtYXQoJ3RydWV0eXBlJyk7XG4gIGZvbnQtd2VpZ2h0OiBib2xkO1xuICBmb250LXN0eWxlOiBpdGFsaWM7XG59XG5AZm9udC1mYWNlIHtcbiAgZm9udC1mYW1pbHk6ICdLYVRlWF9NYXRoJztcbiAgc3JjOiB1cmwoZm9udHMvS2FUZVhfTWF0aC1JdGFsaWMud29mZjIpIGZvcm1hdCgnd29mZjInKSwgdXJsKGZvbnRzL0thVGVYX01hdGgtSXRhbGljLndvZmYpIGZvcm1hdCgnd29mZicpLCB1cmwoZm9udHMvS2FUZVhfTWF0aC1JdGFsaWMudHRmKSBmb3JtYXQoJ3RydWV0eXBlJyk7XG4gIGZvbnQtd2VpZ2h0OiBub3JtYWw7XG4gIGZvbnQtc3R5bGU6IGl0YWxpYztcbn1cbkBmb250LWZhY2Uge1xuICBmb250LWZhbWlseTogJ0thVGVYX1NhbnNTZXJpZic7XG4gIHNyYzogdXJsKGZvbnRzL0thVGVYX1NhbnNTZXJpZi1Cb2xkLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9TYW5zU2VyaWYtQm9sZC53b2ZmKSBmb3JtYXQoJ3dvZmYnKSwgdXJsKGZvbnRzL0thVGVYX1NhbnNTZXJpZi1Cb2xkLnR0ZikgZm9ybWF0KCd0cnVldHlwZScpO1xuICBmb250LXdlaWdodDogYm9sZDtcbiAgZm9udC1zdHlsZTogbm9ybWFsO1xufVxuQGZvbnQtZmFjZSB7XG4gIGZvbnQtZmFtaWx5OiAnS2FUZVhfU2Fuc1NlcmlmJztcbiAgc3JjOiB1cmwoZm9udHMvS2FUZVhfU2Fuc1NlcmlmLUl0YWxpYy53b2ZmMikgZm9ybWF0KCd3b2ZmMicpLCB1cmwoZm9udHMvS2FUZVhfU2Fuc1NlcmlmLUl0YWxpYy53b2ZmKSBmb3JtYXQoJ3dvZmYnKSwgdXJsKGZvbnRzL0thVGVYX1NhbnNTZXJpZi1JdGFsaWMudHRmKSBmb3JtYXQoJ3RydWV0eXBlJyk7XG4gIGZvbnQtd2VpZ2h0OiBub3JtYWw7XG4gIGZvbnQtc3R5bGU6IGl0YWxpYztcbn1cbkBmb250LWZhY2Uge1xuICBmb250LWZhbWlseTogJ0thVGVYX1NhbnNTZXJpZic7XG4gIHNyYzogdXJsKGZvbnRzL0thVGVYX1NhbnNTZXJpZi1SZWd1bGFyLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9TYW5zU2VyaWYtUmVndWxhci53b2ZmKSBmb3JtYXQoJ3dvZmYnKSwgdXJsKGZvbnRzL0thVGVYX1NhbnNTZXJpZi1SZWd1bGFyLnR0ZikgZm9ybWF0KCd0cnVldHlwZScpO1xuICBmb250LXdlaWdodDogbm9ybWFsO1xuICBmb250LXN0eWxlOiBub3JtYWw7XG59XG5AZm9udC1mYWNlIHtcbiAgZm9udC1mYW1pbHk6ICdLYVRlWF9TY3JpcHQnO1xuICBzcmM6IHVybChmb250cy9LYVRlWF9TY3JpcHQtUmVndWxhci53b2ZmMikgZm9ybWF0KCd3b2ZmMicpLCB1cmwoZm9udHMvS2FUZVhfU2NyaXB0LVJlZ3VsYXIud29mZikgZm9ybWF0KCd3b2ZmJyksIHVybChmb250cy9LYVRlWF9TY3JpcHQtUmVndWxhci50dGYpIGZvcm1hdCgndHJ1ZXR5cGUnKTtcbiAgZm9udC13ZWlnaHQ6IG5vcm1hbDtcbiAgZm9udC1zdHlsZTogbm9ybWFsO1xufVxuQGZvbnQtZmFjZSB7XG4gIGZvbnQtZmFtaWx5OiAnS2FUZVhfU2l6ZTEnO1xuICBzcmM6IHVybChmb250cy9LYVRlWF9TaXplMS1SZWd1bGFyLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9TaXplMS1SZWd1bGFyLndvZmYpIGZvcm1hdCgnd29mZicpLCB1cmwoZm9udHMvS2FUZVhfU2l6ZTEtUmVndWxhci50dGYpIGZvcm1hdCgndHJ1ZXR5cGUnKTtcbiAgZm9udC13ZWlnaHQ6IG5vcm1hbDtcbiAgZm9udC1zdHlsZTogbm9ybWFsO1xufVxuQGZvbnQtZmFjZSB7XG4gIGZvbnQtZmFtaWx5OiAnS2FUZVhfU2l6ZTInO1xuICBzcmM6IHVybChmb250cy9LYVRlWF9TaXplMi1SZWd1bGFyLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9TaXplMi1SZWd1bGFyLndvZmYpIGZvcm1hdCgnd29mZicpLCB1cmwoZm9udHMvS2FUZVhfU2l6ZTItUmVndWxhci50dGYpIGZvcm1hdCgndHJ1ZXR5cGUnKTtcbiAgZm9udC13ZWlnaHQ6IG5vcm1hbDtcbiAgZm9udC1zdHlsZTogbm9ybWFsO1xufVxuQGZvbnQtZmFjZSB7XG4gIGZvbnQtZmFtaWx5OiAnS2FUZVhfU2l6ZTMnO1xuICBzcmM6IHVybChmb250cy9LYVRlWF9TaXplMy1SZWd1bGFyLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9TaXplMy1SZWd1bGFyLndvZmYpIGZvcm1hdCgnd29mZicpLCB1cmwoZm9udHMvS2FUZVhfU2l6ZTMtUmVndWxhci50dGYpIGZvcm1hdCgndHJ1ZXR5cGUnKTtcbiAgZm9udC13ZWlnaHQ6IG5vcm1hbDtcbiAgZm9udC1zdHlsZTogbm9ybWFsO1xufVxuQGZvbnQtZmFjZSB7XG4gIGZvbnQtZmFtaWx5OiAnS2FUZVhfU2l6ZTQnO1xuICBzcmM6IHVybChmb250cy9LYVRlWF9TaXplNC1SZWd1bGFyLndvZmYyKSBmb3JtYXQoJ3dvZmYyJyksIHVybChmb250cy9LYVRlWF9TaXplNC1SZWd1bGFyLndvZmYpIGZvcm1hdCgnd29mZicpLCB1cmwoZm9udHMvS2FUZVhfU2l6ZTQtUmVndWxhci50dGYpIGZvcm1hdCgndHJ1ZXR5cGUnKTtcbiAgZm9udC13ZWlnaHQ6IG5vcm1hbDtcbiAgZm9udC1zdHlsZTogbm9ybWFsO1xufVxuQGZvbnQtZmFjZSB7XG4gIGZvbnQtZmFtaWx5OiAnS2FUZVhfVHlwZXdyaXRlcic7XG4gIHNyYzogdXJsKGZvbnRzL0thVGVYX1R5cGV3cml0ZXItUmVndWxhci53b2ZmMikgZm9ybWF0KCd3b2ZmMicpLCB1cmwoZm9udHMvS2FUZVhfVHlwZXdyaXRlci1SZWd1bGFyLndvZmYpIGZvcm1hdCgnd29mZicpLCB1cmwoZm9udHMvS2FUZVhfVHlwZXdyaXRlci1SZWd1bGFyLnR0ZikgZm9ybWF0KCd0cnVldHlwZScpO1xuICBmb250LXdlaWdodDogbm9ybWFsO1xuICBmb250LXN0eWxlOiBub3JtYWw7XG59XG4ua2F0ZXgge1xuICBmb250OiBub3JtYWwgMS4yMWVtIEthVGVYX01haW4sIFRpbWVzIE5ldyBSb21hbiwgc2VyaWY7XG4gIGxpbmUtaGVpZ2h0OiAxLjI7XG4gIHRleHQtaW5kZW50OiAwO1xuICB0ZXh0LXJlbmRlcmluZzogYXV0bztcbn1cbi5rYXRleCAqIHtcbiAgLW1zLWhpZ2gtY29udHJhc3QtYWRqdXN0OiBub25lICFpbXBvcnRhbnQ7XG59XG4ua2F0ZXggLmthdGV4LXZlcnNpb246OmFmdGVyIHtcbiAgY29udGVudDogXCIwLjExLjFcIjtcbn1cbi5rYXRleCAua2F0ZXgtbWF0aG1sIHtcbiAgcG9zaXRpb246IGFic29sdXRlO1xuICBjbGlwOiByZWN0KDFweCwgMXB4LCAxcHgsIDFweCk7XG4gIHBhZGRpbmc6IDA7XG4gIGJvcmRlcjogMDtcbiAgaGVpZ2h0OiAxcHg7XG4gIHdpZHRoOiAxcHg7XG4gIG92ZXJmbG93OiBoaWRkZW47XG59XG4ua2F0ZXggLmthdGV4LWh0bWwge1xuICAvKiBcXG5ld2xpbmUgaXMgYW4gZW1wdHkgYmxvY2sgYXQgdG9wIGxldmVsLCBiZXR3ZWVuIC5iYXNlIGVsZW1lbnRzICovXG59XG4ua2F0ZXggLmthdGV4LWh0bWwgPiAubmV3bGluZSB7XG4gIGRpc3BsYXk6IGJsb2NrO1xufVxuLmthdGV4IC5iYXNlIHtcbiAgcG9zaXRpb246IHJlbGF0aXZlO1xuICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG4gIHdoaXRlLXNwYWNlOiBub3dyYXA7XG4gIHdpZHRoOiBtaW4tY29udGVudDtcbn1cbi5rYXRleCAuc3RydXQge1xuICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG59XG4ua2F0ZXggLnRleHRiZiB7XG4gIGZvbnQtd2VpZ2h0OiBib2xkO1xufVxuLmthdGV4IC50ZXh0aXQge1xuICBmb250LXN0eWxlOiBpdGFsaWM7XG59XG4ua2F0ZXggLnRleHRybSB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9NYWluO1xufVxuLmthdGV4IC50ZXh0c2Yge1xuICBmb250LWZhbWlseTogS2FUZVhfU2Fuc1NlcmlmO1xufVxuLmthdGV4IC50ZXh0dHQge1xuICBmb250LWZhbWlseTogS2FUZVhfVHlwZXdyaXRlcjtcbn1cbi5rYXRleCAubWF0aGRlZmF1bHQge1xuICBmb250LWZhbWlseTogS2FUZVhfTWF0aDtcbiAgZm9udC1zdHlsZTogaXRhbGljO1xufVxuLmthdGV4IC5tYXRoaXQge1xuICBmb250LWZhbWlseTogS2FUZVhfTWFpbjtcbiAgZm9udC1zdHlsZTogaXRhbGljO1xufVxuLmthdGV4IC5tYXRocm0ge1xuICBmb250LXN0eWxlOiBub3JtYWw7XG59XG4ua2F0ZXggLm1hdGhiZiB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9NYWluO1xuICBmb250LXdlaWdodDogYm9sZDtcbn1cbi5rYXRleCAuYm9sZHN5bWJvbCB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9NYXRoO1xuICBmb250LXdlaWdodDogYm9sZDtcbiAgZm9udC1zdHlsZTogaXRhbGljO1xufVxuLmthdGV4IC5hbXNybSB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9BTVM7XG59XG4ua2F0ZXggLm1hdGhiYixcbi5rYXRleCAudGV4dGJiIHtcbiAgZm9udC1mYW1pbHk6IEthVGVYX0FNUztcbn1cbi5rYXRleCAubWF0aGNhbCB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9DYWxpZ3JhcGhpYztcbn1cbi5rYXRleCAubWF0aGZyYWssXG4ua2F0ZXggLnRleHRmcmFrIHtcbiAgZm9udC1mYW1pbHk6IEthVGVYX0ZyYWt0dXI7XG59XG4ua2F0ZXggLm1hdGh0dCB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9UeXBld3JpdGVyO1xufVxuLmthdGV4IC5tYXRoc2NyLFxuLmthdGV4IC50ZXh0c2NyIHtcbiAgZm9udC1mYW1pbHk6IEthVGVYX1NjcmlwdDtcbn1cbi5rYXRleCAubWF0aHNmLFxuLmthdGV4IC50ZXh0c2Yge1xuICBmb250LWZhbWlseTogS2FUZVhfU2Fuc1NlcmlmO1xufVxuLmthdGV4IC5tYXRoYm9sZHNmLFxuLmthdGV4IC50ZXh0Ym9sZHNmIHtcbiAgZm9udC1mYW1pbHk6IEthVGVYX1NhbnNTZXJpZjtcbiAgZm9udC13ZWlnaHQ6IGJvbGQ7XG59XG4ua2F0ZXggLm1hdGhpdHNmLFxuLmthdGV4IC50ZXh0aXRzZiB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9TYW5zU2VyaWY7XG4gIGZvbnQtc3R5bGU6IGl0YWxpYztcbn1cbi5rYXRleCAubWFpbnJtIHtcbiAgZm9udC1mYW1pbHk6IEthVGVYX01haW47XG4gIGZvbnQtc3R5bGU6IG5vcm1hbDtcbn1cbi5rYXRleCAudmxpc3QtdCB7XG4gIGRpc3BsYXk6IGlubGluZS10YWJsZTtcbiAgdGFibGUtbGF5b3V0OiBmaXhlZDtcbn1cbi5rYXRleCAudmxpc3QtciB7XG4gIGRpc3BsYXk6IHRhYmxlLXJvdztcbn1cbi5rYXRleCAudmxpc3Qge1xuICBkaXNwbGF5OiB0YWJsZS1jZWxsO1xuICB2ZXJ0aWNhbC1hbGlnbjogYm90dG9tO1xuICBwb3NpdGlvbjogcmVsYXRpdmU7XG59XG4ua2F0ZXggLnZsaXN0ID4gc3BhbiB7XG4gIGRpc3BsYXk6IGJsb2NrO1xuICBoZWlnaHQ6IDA7XG4gIHBvc2l0aW9uOiByZWxhdGl2ZTtcbn1cbi5rYXRleCAudmxpc3QgPiBzcGFuID4gc3BhbiB7XG4gIGRpc3BsYXk6IGlubGluZS1ibG9jaztcbn1cbi5rYXRleCAudmxpc3QgPiBzcGFuID4gLnBzdHJ1dCB7XG4gIG92ZXJmbG93OiBoaWRkZW47XG4gIHdpZHRoOiAwO1xufVxuLmthdGV4IC52bGlzdC10MiB7XG4gIG1hcmdpbi1yaWdodDogLTJweDtcbn1cbi5rYXRleCAudmxpc3QtcyB7XG4gIGRpc3BsYXk6IHRhYmxlLWNlbGw7XG4gIHZlcnRpY2FsLWFsaWduOiBib3R0b207XG4gIGZvbnQtc2l6ZTogMXB4O1xuICB3aWR0aDogMnB4O1xuICBtaW4td2lkdGg6IDJweDtcbn1cbi5rYXRleCAubXN1cHN1YiB7XG4gIHRleHQtYWxpZ246IGxlZnQ7XG59XG4ua2F0ZXggLm1mcmFjID4gc3BhbiA+IHNwYW4ge1xuICB0ZXh0LWFsaWduOiBjZW50ZXI7XG59XG4ua2F0ZXggLm1mcmFjIC5mcmFjLWxpbmUge1xuICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG4gIHdpZHRoOiAxMDAlO1xuICBib3JkZXItYm90dG9tLXN0eWxlOiBzb2xpZDtcbn1cbi5rYXRleCAubWZyYWMgLmZyYWMtbGluZSxcbi5rYXRleCAub3ZlcmxpbmUgLm92ZXJsaW5lLWxpbmUsXG4ua2F0ZXggLnVuZGVybGluZSAudW5kZXJsaW5lLWxpbmUsXG4ua2F0ZXggLmhsaW5lLFxuLmthdGV4IC5oZGFzaGxpbmUsXG4ua2F0ZXggLnJ1bGUge1xuICBtaW4taGVpZ2h0OiAxcHg7XG59XG4ua2F0ZXggLm1zcGFjZSB7XG4gIGRpc3BsYXk6IGlubGluZS1ibG9jaztcbn1cbi5rYXRleCAubGxhcCxcbi5rYXRleCAucmxhcCxcbi5rYXRleCAuY2xhcCB7XG4gIHdpZHRoOiAwO1xuICBwb3NpdGlvbjogcmVsYXRpdmU7XG59XG4ua2F0ZXggLmxsYXAgPiAuaW5uZXIsXG4ua2F0ZXggLnJsYXAgPiAuaW5uZXIsXG4ua2F0ZXggLmNsYXAgPiAuaW5uZXIge1xuICBwb3NpdGlvbjogYWJzb2x1dGU7XG59XG4ua2F0ZXggLmxsYXAgPiAuZml4LFxuLmthdGV4IC5ybGFwID4gLmZpeCxcbi5rYXRleCAuY2xhcCA+IC5maXgge1xuICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG59XG4ua2F0ZXggLmxsYXAgPiAuaW5uZXIge1xuICByaWdodDogMDtcbn1cbi5rYXRleCAucmxhcCA+IC5pbm5lcixcbi5rYXRleCAuY2xhcCA+IC5pbm5lciB7XG4gIGxlZnQ6IDA7XG59XG4ua2F0ZXggLmNsYXAgPiAuaW5uZXIgPiBzcGFuIHtcbiAgbWFyZ2luLWxlZnQ6IC01MCU7XG4gIG1hcmdpbi1yaWdodDogNTAlO1xufVxuLmthdGV4IC5ydWxlIHtcbiAgZGlzcGxheTogaW5saW5lLWJsb2NrO1xuICBib3JkZXI6IHNvbGlkIDA7XG4gIHBvc2l0aW9uOiByZWxhdGl2ZTtcbn1cbi5rYXRleCAub3ZlcmxpbmUgLm92ZXJsaW5lLWxpbmUsXG4ua2F0ZXggLnVuZGVybGluZSAudW5kZXJsaW5lLWxpbmUsXG4ua2F0ZXggLmhsaW5lIHtcbiAgZGlzcGxheTogaW5saW5lLWJsb2NrO1xuICB3aWR0aDogMTAwJTtcbiAgYm9yZGVyLWJvdHRvbS1zdHlsZTogc29saWQ7XG59XG4ua2F0ZXggLmhkYXNobGluZSB7XG4gIGRpc3BsYXk6IGlubGluZS1ibG9jaztcbiAgd2lkdGg6IDEwMCU7XG4gIGJvcmRlci1ib3R0b20tc3R5bGU6IGRhc2hlZDtcbn1cbi5rYXRleCAuc3FydCA+IC5yb290IHtcbiAgbWFyZ2luLWxlZnQ6IDAuMjc3Nzc3NzhlbTtcbiAgbWFyZ2luLXJpZ2h0OiAtMC41NTU1NTU1NmVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTEuc2l6ZTEsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTEuc2l6ZTEge1xuICBmb250LXNpemU6IDFlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxLnNpemUyLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUxLnNpemUyIHtcbiAgZm9udC1zaXplOiAxLjJlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxLnNpemUzLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUxLnNpemUzIHtcbiAgZm9udC1zaXplOiAxLjRlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxLnNpemU0LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUxLnNpemU0IHtcbiAgZm9udC1zaXplOiAxLjZlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxLnNpemU1LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUxLnNpemU1IHtcbiAgZm9udC1zaXplOiAxLjhlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxLnNpemU2LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUxLnNpemU2IHtcbiAgZm9udC1zaXplOiAyZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMS5zaXplNyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMS5zaXplNyB7XG4gIGZvbnQtc2l6ZTogMi40ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMS5zaXplOCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMS5zaXplOCB7XG4gIGZvbnQtc2l6ZTogMi44OGVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTEuc2l6ZTksXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTEuc2l6ZTkge1xuICBmb250LXNpemU6IDMuNDU2ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMS5zaXplMTAsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTEuc2l6ZTEwIHtcbiAgZm9udC1zaXplOiA0LjE0OGVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTEuc2l6ZTExLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUxLnNpemUxMSB7XG4gIGZvbnQtc2l6ZTogNC45NzZlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUyLnNpemUxLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUyLnNpemUxIHtcbiAgZm9udC1zaXplOiAwLjgzMzMzMzMzZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMi5zaXplMixcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMi5zaXplMiB7XG4gIGZvbnQtc2l6ZTogMWVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTIuc2l6ZTMsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTIuc2l6ZTMge1xuICBmb250LXNpemU6IDEuMTY2NjY2NjdlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUyLnNpemU0LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUyLnNpemU0IHtcbiAgZm9udC1zaXplOiAxLjMzMzMzMzMzZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMi5zaXplNSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMi5zaXplNSB7XG4gIGZvbnQtc2l6ZTogMS41ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMi5zaXplNixcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMi5zaXplNiB7XG4gIGZvbnQtc2l6ZTogMS42NjY2NjY2N2VtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTIuc2l6ZTcsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTIuc2l6ZTcge1xuICBmb250LXNpemU6IDJlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUyLnNpemU4LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUyLnNpemU4IHtcbiAgZm9udC1zaXplOiAyLjRlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUyLnNpemU5LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUyLnNpemU5IHtcbiAgZm9udC1zaXplOiAyLjg4ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMi5zaXplMTAsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTIuc2l6ZTEwIHtcbiAgZm9udC1zaXplOiAzLjQ1NjY2NjY3ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMi5zaXplMTEsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTIuc2l6ZTExIHtcbiAgZm9udC1zaXplOiA0LjE0NjY2NjY3ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMy5zaXplMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMy5zaXplMSB7XG4gIGZvbnQtc2l6ZTogMC43MTQyODU3MWVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTMuc2l6ZTIsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTMuc2l6ZTIge1xuICBmb250LXNpemU6IDAuODU3MTQyODZlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUzLnNpemUzLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUzLnNpemUzIHtcbiAgZm9udC1zaXplOiAxZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMy5zaXplNCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMy5zaXplNCB7XG4gIGZvbnQtc2l6ZTogMS4xNDI4NTcxNGVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTMuc2l6ZTUsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTMuc2l6ZTUge1xuICBmb250LXNpemU6IDEuMjg1NzE0MjllbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUzLnNpemU2LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUzLnNpemU2IHtcbiAgZm9udC1zaXplOiAxLjQyODU3MTQzZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMy5zaXplNyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMy5zaXplNyB7XG4gIGZvbnQtc2l6ZTogMS43MTQyODU3MWVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTMuc2l6ZTgsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTMuc2l6ZTgge1xuICBmb250LXNpemU6IDIuMDU3MTQyODZlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUzLnNpemU5LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUzLnNpemU5IHtcbiAgZm9udC1zaXplOiAyLjQ2ODU3MTQzZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMy5zaXplMTAsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTMuc2l6ZTEwIHtcbiAgZm9udC1zaXplOiAyLjk2Mjg1NzE0ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMy5zaXplMTEsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTMuc2l6ZTExIHtcbiAgZm9udC1zaXplOiAzLjU1NDI4NTcxZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNC5zaXplMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNC5zaXplMSB7XG4gIGZvbnQtc2l6ZTogMC42MjVlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU0LnNpemUyLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU0LnNpemUyIHtcbiAgZm9udC1zaXplOiAwLjc1ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNC5zaXplMyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNC5zaXplMyB7XG4gIGZvbnQtc2l6ZTogMC44NzVlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU0LnNpemU0LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU0LnNpemU0IHtcbiAgZm9udC1zaXplOiAxZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNC5zaXplNSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNC5zaXplNSB7XG4gIGZvbnQtc2l6ZTogMS4xMjVlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU0LnNpemU2LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU0LnNpemU2IHtcbiAgZm9udC1zaXplOiAxLjI1ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNC5zaXplNyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNC5zaXplNyB7XG4gIGZvbnQtc2l6ZTogMS41ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNC5zaXplOCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNC5zaXplOCB7XG4gIGZvbnQtc2l6ZTogMS44ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNC5zaXplOSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNC5zaXplOSB7XG4gIGZvbnQtc2l6ZTogMi4xNmVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTQuc2l6ZTEwLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU0LnNpemUxMCB7XG4gIGZvbnQtc2l6ZTogMi41OTI1ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNC5zaXplMTEsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTQuc2l6ZTExIHtcbiAgZm9udC1zaXplOiAzLjExZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNS5zaXplMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNS5zaXplMSB7XG4gIGZvbnQtc2l6ZTogMC41NTU1NTU1NmVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTUuc2l6ZTIsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTUuc2l6ZTIge1xuICBmb250LXNpemU6IDAuNjY2NjY2NjdlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU1LnNpemUzLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU1LnNpemUzIHtcbiAgZm9udC1zaXplOiAwLjc3Nzc3Nzc4ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNS5zaXplNCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNS5zaXplNCB7XG4gIGZvbnQtc2l6ZTogMC44ODg4ODg4OWVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTUuc2l6ZTUsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTUuc2l6ZTUge1xuICBmb250LXNpemU6IDFlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU1LnNpemU2LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU1LnNpemU2IHtcbiAgZm9udC1zaXplOiAxLjExMTExMTExZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNS5zaXplNyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNS5zaXplNyB7XG4gIGZvbnQtc2l6ZTogMS4zMzMzMzMzM2VtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTUuc2l6ZTgsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTUuc2l6ZTgge1xuICBmb250LXNpemU6IDEuNmVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTUuc2l6ZTksXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTUuc2l6ZTkge1xuICBmb250LXNpemU6IDEuOTJlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU1LnNpemUxMCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNS5zaXplMTAge1xuICBmb250LXNpemU6IDIuMzA0NDQ0NDRlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU1LnNpemUxMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNS5zaXplMTEge1xuICBmb250LXNpemU6IDIuNzY0NDQ0NDRlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU2LnNpemUxLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU2LnNpemUxIHtcbiAgZm9udC1zaXplOiAwLjVlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU2LnNpemUyLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU2LnNpemUyIHtcbiAgZm9udC1zaXplOiAwLjZlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU2LnNpemUzLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU2LnNpemUzIHtcbiAgZm9udC1zaXplOiAwLjdlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU2LnNpemU0LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU2LnNpemU0IHtcbiAgZm9udC1zaXplOiAwLjhlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU2LnNpemU1LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU2LnNpemU1IHtcbiAgZm9udC1zaXplOiAwLjllbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU2LnNpemU2LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU2LnNpemU2IHtcbiAgZm9udC1zaXplOiAxZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNi5zaXplNyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNi5zaXplNyB7XG4gIGZvbnQtc2l6ZTogMS4yZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNi5zaXplOCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNi5zaXplOCB7XG4gIGZvbnQtc2l6ZTogMS40NGVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTYuc2l6ZTksXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTYuc2l6ZTkge1xuICBmb250LXNpemU6IDEuNzI4ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNi5zaXplMTAsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTYuc2l6ZTEwIHtcbiAgZm9udC1zaXplOiAyLjA3NGVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTYuc2l6ZTExLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU2LnNpemUxMSB7XG4gIGZvbnQtc2l6ZTogMi40ODhlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU3LnNpemUxLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU3LnNpemUxIHtcbiAgZm9udC1zaXplOiAwLjQxNjY2NjY3ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNy5zaXplMixcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNy5zaXplMiB7XG4gIGZvbnQtc2l6ZTogMC41ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNy5zaXplMyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNy5zaXplMyB7XG4gIGZvbnQtc2l6ZTogMC41ODMzMzMzM2VtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTcuc2l6ZTQsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTcuc2l6ZTQge1xuICBmb250LXNpemU6IDAuNjY2NjY2NjdlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU3LnNpemU1LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU3LnNpemU1IHtcbiAgZm9udC1zaXplOiAwLjc1ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNy5zaXplNixcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplNy5zaXplNiB7XG4gIGZvbnQtc2l6ZTogMC44MzMzMzMzM2VtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTcuc2l6ZTcsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTcuc2l6ZTcge1xuICBmb250LXNpemU6IDFlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU3LnNpemU4LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU3LnNpemU4IHtcbiAgZm9udC1zaXplOiAxLjJlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU3LnNpemU5LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU3LnNpemU5IHtcbiAgZm9udC1zaXplOiAxLjQ0ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNy5zaXplMTAsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTcuc2l6ZTEwIHtcbiAgZm9udC1zaXplOiAxLjcyODMzMzMzZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplNy5zaXplMTEsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTcuc2l6ZTExIHtcbiAgZm9udC1zaXplOiAyLjA3MzMzMzMzZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOC5zaXplMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOC5zaXplMSB7XG4gIGZvbnQtc2l6ZTogMC4zNDcyMjIyMmVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTguc2l6ZTIsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTguc2l6ZTIge1xuICBmb250LXNpemU6IDAuNDE2NjY2NjdlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU4LnNpemUzLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU4LnNpemUzIHtcbiAgZm9udC1zaXplOiAwLjQ4NjExMTExZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOC5zaXplNCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOC5zaXplNCB7XG4gIGZvbnQtc2l6ZTogMC41NTU1NTU1NmVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTguc2l6ZTUsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTguc2l6ZTUge1xuICBmb250LXNpemU6IDAuNjI1ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOC5zaXplNixcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOC5zaXplNiB7XG4gIGZvbnQtc2l6ZTogMC42OTQ0NDQ0NGVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTguc2l6ZTcsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTguc2l6ZTcge1xuICBmb250LXNpemU6IDAuODMzMzMzMzNlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU4LnNpemU4LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU4LnNpemU4IHtcbiAgZm9udC1zaXplOiAxZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOC5zaXplOSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOC5zaXplOSB7XG4gIGZvbnQtc2l6ZTogMS4yZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOC5zaXplMTAsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTguc2l6ZTEwIHtcbiAgZm9udC1zaXplOiAxLjQ0MDI3Nzc4ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOC5zaXplMTEsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTguc2l6ZTExIHtcbiAgZm9udC1zaXplOiAxLjcyNzc3Nzc4ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOS5zaXplMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOS5zaXplMSB7XG4gIGZvbnQtc2l6ZTogMC4yODkzNTE4NWVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTkuc2l6ZTIsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTkuc2l6ZTIge1xuICBmb250LXNpemU6IDAuMzQ3MjIyMjJlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU5LnNpemUzLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU5LnNpemUzIHtcbiAgZm9udC1zaXplOiAwLjQwNTA5MjU5ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOS5zaXplNCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOS5zaXplNCB7XG4gIGZvbnQtc2l6ZTogMC40NjI5NjI5NmVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTkuc2l6ZTUsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTkuc2l6ZTUge1xuICBmb250LXNpemU6IDAuNTIwODMzMzNlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU5LnNpemU2LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU5LnNpemU2IHtcbiAgZm9udC1zaXplOiAwLjU3ODcwMzdlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU5LnNpemU3LFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemU5LnNpemU3IHtcbiAgZm9udC1zaXplOiAwLjY5NDQ0NDQ0ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplOS5zaXplOCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOS5zaXplOCB7XG4gIGZvbnQtc2l6ZTogMC44MzMzMzMzM2VtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTkuc2l6ZTksXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTkuc2l6ZTkge1xuICBmb250LXNpemU6IDFlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU5LnNpemUxMCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOS5zaXplMTAge1xuICBmb250LXNpemU6IDEuMjAwMjMxNDhlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemU5LnNpemUxMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplOS5zaXplMTEge1xuICBmb250LXNpemU6IDEuNDM5ODE0ODFlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTEge1xuICBmb250LXNpemU6IDAuMjQxMDgwMDRlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplMixcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTIge1xuICBmb250LXNpemU6IDAuMjg5Mjk2MDVlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplMyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTMge1xuICBmb250LXNpemU6IDAuMzM3NTEyMDVlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplNCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTQge1xuICBmb250LXNpemU6IDAuMzg1NzI4MDZlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplNSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTUge1xuICBmb250LXNpemU6IDAuNDMzOTQ0MDdlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplNixcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTYge1xuICBmb250LXNpemU6IDAuNDgyMTYwMDhlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplNyxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTcge1xuICBmb250LXNpemU6IDAuNTc4NTkyMDllbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplOCxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTgge1xuICBmb250LXNpemU6IDAuNjk0MzEwNTFlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplOSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTkge1xuICBmb250LXNpemU6IDAuODMzMTcyNjFlbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMC5zaXplMTAsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTEwLnNpemUxMCB7XG4gIGZvbnQtc2l6ZTogMWVtO1xufVxuLmthdGV4IC5zaXppbmcucmVzZXQtc2l6ZTEwLnNpemUxMSxcbi5rYXRleCAuZm9udHNpemUtZW5zdXJlci5yZXNldC1zaXplMTAuc2l6ZTExIHtcbiAgZm9udC1zaXplOiAxLjE5OTYxNDI3ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTEsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemUxIHtcbiAgZm9udC1zaXplOiAwLjIwMDk2NDYzZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTIsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemUyIHtcbiAgZm9udC1zaXplOiAwLjI0MTE1NzU2ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTMsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemUzIHtcbiAgZm9udC1zaXplOiAwLjI4MTM1MDQ4ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTQsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemU0IHtcbiAgZm9udC1zaXplOiAwLjMyMTU0MzQxZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTUsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemU1IHtcbiAgZm9udC1zaXplOiAwLjM2MTczNjMzZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTYsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemU2IHtcbiAgZm9udC1zaXplOiAwLjQwMTkyOTI2ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTcsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemU3IHtcbiAgZm9udC1zaXplOiAwLjQ4MjMxNTExZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTgsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemU4IHtcbiAgZm9udC1zaXplOiAwLjU3ODc3ODE0ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTksXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemU5IHtcbiAgZm9udC1zaXplOiAwLjY5NDUzMzc2ZW07XG59XG4ua2F0ZXggLnNpemluZy5yZXNldC1zaXplMTEuc2l6ZTEwLFxuLmthdGV4IC5mb250c2l6ZS1lbnN1cmVyLnJlc2V0LXNpemUxMS5zaXplMTAge1xuICBmb250LXNpemU6IDAuODMzNjAxMjllbTtcbn1cbi5rYXRleCAuc2l6aW5nLnJlc2V0LXNpemUxMS5zaXplMTEsXG4ua2F0ZXggLmZvbnRzaXplLWVuc3VyZXIucmVzZXQtc2l6ZTExLnNpemUxMSB7XG4gIGZvbnQtc2l6ZTogMWVtO1xufVxuLmthdGV4IC5kZWxpbXNpemluZy5zaXplMSB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9TaXplMTtcbn1cbi5rYXRleCAuZGVsaW1zaXppbmcuc2l6ZTIge1xuICBmb250LWZhbWlseTogS2FUZVhfU2l6ZTI7XG59XG4ua2F0ZXggLmRlbGltc2l6aW5nLnNpemUzIHtcbiAgZm9udC1mYW1pbHk6IEthVGVYX1NpemUzO1xufVxuLmthdGV4IC5kZWxpbXNpemluZy5zaXplNCB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9TaXplNDtcbn1cbi5rYXRleCAuZGVsaW1zaXppbmcubXVsdCAuZGVsaW0tc2l6ZTEgPiBzcGFuIHtcbiAgZm9udC1mYW1pbHk6IEthVGVYX1NpemUxO1xufVxuLmthdGV4IC5kZWxpbXNpemluZy5tdWx0IC5kZWxpbS1zaXplNCA+IHNwYW4ge1xuICBmb250LWZhbWlseTogS2FUZVhfU2l6ZTQ7XG59XG4ua2F0ZXggLm51bGxkZWxpbWl0ZXIge1xuICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG4gIHdpZHRoOiAwLjEyZW07XG59XG4ua2F0ZXggLmRlbGltY2VudGVyIHtcbiAgcG9zaXRpb246IHJlbGF0aXZlO1xufVxuLmthdGV4IC5vcC1zeW1ib2wge1xuICBwb3NpdGlvbjogcmVsYXRpdmU7XG59XG4ua2F0ZXggLm9wLXN5bWJvbC5zbWFsbC1vcCB7XG4gIGZvbnQtZmFtaWx5OiBLYVRlWF9TaXplMTtcbn1cbi5rYXRleCAub3Atc3ltYm9sLmxhcmdlLW9wIHtcbiAgZm9udC1mYW1pbHk6IEthVGVYX1NpemUyO1xufVxuLmthdGV4IC5vcC1saW1pdHMgPiAudmxpc3QtdCB7XG4gIHRleHQtYWxpZ246IGNlbnRlcjtcbn1cbi5rYXRleCAuYWNjZW50ID4gLnZsaXN0LXQge1xuICB0ZXh0LWFsaWduOiBjZW50ZXI7XG59XG4ua2F0ZXggLmFjY2VudCAuYWNjZW50LWJvZHkge1xuICBwb3NpdGlvbjogcmVsYXRpdmU7XG59XG4ua2F0ZXggLmFjY2VudCAuYWNjZW50LWJvZHk6bm90KC5hY2NlbnQtZnVsbCkge1xuICB3aWR0aDogMDtcbn1cbi5rYXRleCAub3ZlcmxheSB7XG4gIGRpc3BsYXk6IGJsb2NrO1xufVxuLmthdGV4IC5tdGFibGUgLnZlcnRpY2FsLXNlcGFyYXRvciB7XG4gIGRpc3BsYXk6IGlubGluZS1ibG9jaztcbiAgbWluLXdpZHRoOiAxcHg7XG59XG4ua2F0ZXggLm10YWJsZSAuYXJyYXljb2xzZXAge1xuICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG59XG4ua2F0ZXggLm10YWJsZSAuY29sLWFsaWduLWMgPiAudmxpc3QtdCB7XG4gIHRleHQtYWxpZ246IGNlbnRlcjtcbn1cbi5rYXRleCAubXRhYmxlIC5jb2wtYWxpZ24tbCA+IC52bGlzdC10IHtcbiAgdGV4dC1hbGlnbjogbGVmdDtcbn1cbi5rYXRleCAubXRhYmxlIC5jb2wtYWxpZ24tciA+IC52bGlzdC10IHtcbiAgdGV4dC1hbGlnbjogcmlnaHQ7XG59XG4ua2F0ZXggLnN2Zy1hbGlnbiB7XG4gIHRleHQtYWxpZ246IGxlZnQ7XG59XG4ua2F0ZXggc3ZnIHtcbiAgZGlzcGxheTogYmxvY2s7XG4gIHBvc2l0aW9uOiBhYnNvbHV0ZTtcbiAgd2lkdGg6IDEwMCU7XG4gIGhlaWdodDogaW5oZXJpdDtcbiAgZmlsbDogY3VycmVudENvbG9yO1xuICBzdHJva2U6IGN1cnJlbnRDb2xvcjtcbiAgZmlsbC1ydWxlOiBub256ZXJvO1xuICBmaWxsLW9wYWNpdHk6IDE7XG4gIHN0cm9rZS13aWR0aDogMTtcbiAgc3Ryb2tlLWxpbmVjYXA6IGJ1dHQ7XG4gIHN0cm9rZS1saW5lam9pbjogbWl0ZXI7XG4gIHN0cm9rZS1taXRlcmxpbWl0OiA0O1xuICBzdHJva2UtZGFzaGFycmF5OiBub25lO1xuICBzdHJva2UtZGFzaG9mZnNldDogMDtcbiAgc3Ryb2tlLW9wYWNpdHk6IDE7XG59XG4ua2F0ZXggc3ZnIHBhdGgge1xuICBzdHJva2U6IG5vbmU7XG59XG4ua2F0ZXggaW1nIHtcbiAgYm9yZGVyLXN0eWxlOiBub25lO1xuICBtaW4td2lkdGg6IDA7XG4gIG1pbi1oZWlnaHQ6IDA7XG4gIG1heC13aWR0aDogbm9uZTtcbiAgbWF4LWhlaWdodDogbm9uZTtcbn1cbi5rYXRleCAuc3RyZXRjaHkge1xuICB3aWR0aDogMTAwJTtcbiAgZGlzcGxheTogYmxvY2s7XG4gIHBvc2l0aW9uOiByZWxhdGl2ZTtcbiAgb3ZlcmZsb3c6IGhpZGRlbjtcbn1cbi5rYXRleCAuc3RyZXRjaHk6OmJlZm9yZSxcbi5rYXRleCAuc3RyZXRjaHk6OmFmdGVyIHtcbiAgY29udGVudDogXCJcIjtcbn1cbi5rYXRleCAuaGlkZS10YWlsIHtcbiAgd2lkdGg6IDEwMCU7XG4gIHBvc2l0aW9uOiByZWxhdGl2ZTtcbiAgb3ZlcmZsb3c6IGhpZGRlbjtcbn1cbi5rYXRleCAuaGFsZmFycm93LWxlZnQge1xuICBwb3NpdGlvbjogYWJzb2x1dGU7XG4gIGxlZnQ6IDA7XG4gIHdpZHRoOiA1MC4yJTtcbiAgb3ZlcmZsb3c6IGhpZGRlbjtcbn1cbi5rYXRleCAuaGFsZmFycm93LXJpZ2h0IHtcbiAgcG9zaXRpb246IGFic29sdXRlO1xuICByaWdodDogMDtcbiAgd2lkdGg6IDUwLjIlO1xuICBvdmVyZmxvdzogaGlkZGVuO1xufVxuLmthdGV4IC5icmFjZS1sZWZ0IHtcbiAgcG9zaXRpb246IGFic29sdXRlO1xuICBsZWZ0OiAwO1xuICB3aWR0aDogMjUuMSU7XG4gIG92ZXJmbG93OiBoaWRkZW47XG59XG4ua2F0ZXggLmJyYWNlLWNlbnRlciB7XG4gIHBvc2l0aW9uOiBhYnNvbHV0ZTtcbiAgbGVmdDogMjUlO1xuICB3aWR0aDogNTAlO1xuICBvdmVyZmxvdzogaGlkZGVuO1xufVxuLmthdGV4IC5icmFjZS1yaWdodCB7XG4gIHBvc2l0aW9uOiBhYnNvbHV0ZTtcbiAgcmlnaHQ6IDA7XG4gIHdpZHRoOiAyNS4xJTtcbiAgb3ZlcmZsb3c6IGhpZGRlbjtcbn1cbi5rYXRleCAueC1hcnJvdy1wYWQge1xuICBwYWRkaW5nOiAwIDAuNWVtO1xufVxuLmthdGV4IC54LWFycm93LFxuLmthdGV4IC5tb3Zlcixcbi5rYXRleCAubXVuZGVyIHtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xufVxuLmthdGV4IC5ib3hwYWQge1xuICBwYWRkaW5nOiAwIDAuM2VtIDAgMC4zZW07XG59XG4ua2F0ZXggLmZib3gsXG4ua2F0ZXggLmZjb2xvcmJveCB7XG4gIGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG4gIGJvcmRlcjogMC4wNGVtIHNvbGlkO1xufVxuLmthdGV4IC5jYW5jZWwtcGFkIHtcbiAgcGFkZGluZzogMCAwLjJlbSAwIDAuMmVtO1xufVxuLmthdGV4IC5jYW5jZWwtbGFwIHtcbiAgbWFyZ2luLWxlZnQ6IC0wLjJlbTtcbiAgbWFyZ2luLXJpZ2h0OiAtMC4yZW07XG59XG4ua2F0ZXggLnNvdXQge1xuICBib3JkZXItYm90dG9tLXN0eWxlOiBzb2xpZDtcbiAgYm9yZGVyLWJvdHRvbS13aWR0aDogMC4wOGVtO1xufVxuLmthdGV4LWRpc3BsYXkge1xuICBkaXNwbGF5OiBibG9jaztcbiAgbWFyZ2luOiAxZW0gMDtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xufVxuLmthdGV4LWRpc3BsYXkgPiAua2F0ZXgge1xuICBkaXNwbGF5OiBibG9jaztcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xuICB3aGl0ZS1zcGFjZTogbm93cmFwO1xufVxuLmthdGV4LWRpc3BsYXkgPiAua2F0ZXggPiAua2F0ZXgtaHRtbCB7XG4gIGRpc3BsYXk6IGJsb2NrO1xuICBwb3NpdGlvbjogcmVsYXRpdmU7XG59XG4ua2F0ZXgtZGlzcGxheSA+IC5rYXRleCA+IC5rYXRleC1odG1sID4gLnRhZyB7XG4gIHBvc2l0aW9uOiBhYnNvbHV0ZTtcbiAgcmlnaHQ6IDA7XG59XG4ua2F0ZXgtZGlzcGxheS5sZXFubyA+IC5rYXRleCA+IC5rYXRleC1odG1sID4gLnRhZyB7XG4gIGxlZnQ6IDA7XG4gIHJpZ2h0OiBhdXRvO1xufVxuLmthdGV4LWRpc3BsYXkuZmxlcW4gPiAua2F0ZXgge1xuICB0ZXh0LWFsaWduOiBsZWZ0O1xufVxuXG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><link rel="prefetch" as="script" href="https://codeocean.com/code-viewer.a2fcd1.chunk.js"><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .selection-anchor {
	background-color: #007ACC;
	width: 2px !important;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvY29udHJpYi9hbmNob3JTZWxlY3QvYW5jaG9yU2VsZWN0LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyx5QkFBeUI7Q0FDekIscUJBQXFCO0FBQ3RCIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5tb25hY28tZWRpdG9yIC5zZWxlY3Rpb24tYW5jaG9yIHtcblx0YmFja2dyb3VuZC1jb2xvcjogIzAwN0FDQztcblx0d2lkdGg6IDJweCAhaW1wb3J0YW50O1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-aria-container {
	position: absolute; /* try to hide from window but not from screen readers */
	left:-999em;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvYXJpYS9hcmlhLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxrQkFBa0IsRUFBRSx3REFBd0Q7Q0FDNUUsV0FBVztBQUNaIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5tb25hY28tYXJpYS1jb250YWluZXIge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7IC8qIHRyeSB0byBoaWRlIGZyb20gd2luZG93IGJ1dCBub3QgZnJvbSBzY3JlZW4gcmVhZGVycyAqL1xuXHRsZWZ0Oi05OTllbTtcbn0iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-custom-checkbox {
	margin-left: 2px;
	float: left;
	cursor: pointer;
	overflow: hidden;
	opacity: 0.7;
	width: 20px;
	height: 20px;
	border: 1px solid transparent;
	padding: 1px;
	box-sizing:	border-box;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-custom-checkbox:hover,
.monaco-custom-checkbox.checked {
	opacity: 1;
}

.hc-black .monaco-custom-checkbox {
	background: none;
}

.hc-black .monaco-custom-checkbox:hover {
	background: none;
}

.monaco-custom-checkbox.monaco-simple-checkbox {
	height: 18px;
	width: 18px;
	border: 1px solid transparent;
	border-radius: 3px;
	margin-right: 9px;
	margin-left: 0px;
	padding: 0px;
	opacity: 1;
	background-size: 16px !important;
}

/* hide check when unchecked */
.monaco-custom-checkbox.monaco-simple-checkbox.unchecked:not(.checked)::before {
	visibility: hidden;;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvY2hlY2tib3gvY2hlY2tib3guY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLGdCQUFnQjtDQUNoQixXQUFXO0NBQ1gsZUFBZTtDQUNmLGdCQUFnQjtDQUNoQixZQUFZO0NBQ1osV0FBVztDQUNYLFlBQVk7Q0FDWiw2QkFBNkI7Q0FDN0IsWUFBWTtDQUNaLHNCQUFzQjtDQUN0QixpQkFBaUI7Q0FDakIseUJBQXlCO0NBQ3pCLHFCQUFxQjtBQUN0Qjs7QUFFQTs7Q0FFQyxVQUFVO0FBQ1g7O0FBRUE7Q0FDQyxnQkFBZ0I7QUFDakI7O0FBRUE7Q0FDQyxnQkFBZ0I7QUFDakI7O0FBRUE7Q0FDQyxZQUFZO0NBQ1osV0FBVztDQUNYLDZCQUE2QjtDQUM3QixrQkFBa0I7Q0FDbEIsaUJBQWlCO0NBQ2pCLGdCQUFnQjtDQUNoQixZQUFZO0NBQ1osVUFBVTtDQUNWLGdDQUFnQztBQUNqQzs7QUFFQSw4QkFBOEI7QUFDOUI7Q0FDQyxrQkFBa0I7QUFDbkIiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLm1vbmFjby1jdXN0b20tY2hlY2tib3gge1xuXHRtYXJnaW4tbGVmdDogMnB4O1xuXHRmbG9hdDogbGVmdDtcblx0Y3Vyc29yOiBwb2ludGVyO1xuXHRvdmVyZmxvdzogaGlkZGVuO1xuXHRvcGFjaXR5OiAwLjc7XG5cdHdpZHRoOiAyMHB4O1xuXHRoZWlnaHQ6IDIwcHg7XG5cdGJvcmRlcjogMXB4IHNvbGlkIHRyYW5zcGFyZW50O1xuXHRwYWRkaW5nOiAxcHg7XG5cdGJveC1zaXppbmc6XHRib3JkZXItYm94O1xuXHR1c2VyLXNlbGVjdDogbm9uZTtcblx0LXdlYmtpdC11c2VyLXNlbGVjdDogbm9uZTtcblx0LW1zLXVzZXItc2VsZWN0OiBub25lO1xufVxuXG4ubW9uYWNvLWN1c3RvbS1jaGVja2JveDpob3Zlcixcbi5tb25hY28tY3VzdG9tLWNoZWNrYm94LmNoZWNrZWQge1xuXHRvcGFjaXR5OiAxO1xufVxuXG4uaGMtYmxhY2sgLm1vbmFjby1jdXN0b20tY2hlY2tib3gge1xuXHRiYWNrZ3JvdW5kOiBub25lO1xufVxuXG4uaGMtYmxhY2sgLm1vbmFjby1jdXN0b20tY2hlY2tib3g6aG92ZXIge1xuXHRiYWNrZ3JvdW5kOiBub25lO1xufVxuXG4ubW9uYWNvLWN1c3RvbS1jaGVja2JveC5tb25hY28tc2ltcGxlLWNoZWNrYm94IHtcblx0aGVpZ2h0OiAxOHB4O1xuXHR3aWR0aDogMThweDtcblx0Ym9yZGVyOiAxcHggc29saWQgdHJhbnNwYXJlbnQ7XG5cdGJvcmRlci1yYWRpdXM6IDNweDtcblx0bWFyZ2luLXJpZ2h0OiA5cHg7XG5cdG1hcmdpbi1sZWZ0OiAwcHg7XG5cdHBhZGRpbmc6IDBweDtcblx0b3BhY2l0eTogMTtcblx0YmFja2dyb3VuZC1zaXplOiAxNnB4ICFpbXBvcnRhbnQ7XG59XG5cbi8qIGhpZGUgY2hlY2sgd2hlbiB1bmNoZWNrZWQgKi9cbi5tb25hY28tY3VzdG9tLWNoZWNrYm94Lm1vbmFjby1zaW1wbGUtY2hlY2tib3gudW5jaGVja2VkOm5vdCguY2hlY2tlZCk6OmJlZm9yZSB7XG5cdHZpc2liaWxpdHk6IGhpZGRlbjs7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Find widget */
.monaco-editor .find-widget {
	position: absolute;
	z-index: 50;
	height: 33px;
	overflow: hidden;
	line-height: 19px;
	transition: transform 200ms linear;
	padding: 0 4px;
	box-sizing: border-box;
	transform: translateY(calc(-100% - 10px)); /* shadow (10px) */
}

.monaco-editor .find-widget textarea {
	margin: 0px;
}

.monaco-editor .find-widget.hiddenEditor {
	display: none;
}

/* Find widget when replace is toggled on */
.monaco-editor .find-widget.replaceToggled > .replace-part {
	display: flex;
}

.monaco-editor .find-widget.visible  {
	transform: translateY(0);
}

.monaco-editor .find-widget .monaco-inputbox.synthetic-focus {
	outline: 1px solid -webkit-focus-ring-color;
	outline-offset: -1px;
}

.monaco-editor .find-widget .monaco-inputbox .input {
	background-color: transparent;
	min-height: 0;
}

.monaco-editor .find-widget .monaco-findInput .input {
	font-size: 13px;
}

.monaco-editor .find-widget > .find-part,
.monaco-editor .find-widget > .replace-part {
	margin: 4px 0 0 17px;
	font-size: 12px;
	display: flex;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox,
.monaco-editor .find-widget > .replace-part .monaco-inputbox {
	min-height: 25px;
}


.monaco-editor .find-widget > .replace-part .monaco-inputbox > .wrapper > .mirror {
	padding-right: 22px;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox > .wrapper > .input,
.monaco-editor .find-widget > .find-part .monaco-inputbox > .wrapper > .mirror,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .wrapper > .input,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .wrapper > .mirror {
	padding-top: 2px;
	padding-bottom: 2px;
}

.monaco-editor .find-widget > .find-part .find-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget > .replace-part .replace-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget .monaco-findInput {
	vertical-align: middle;
	display: flex;
	flex:1;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element {
	/* Make sure textarea inherits the width correctly */
	width: 100%;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element .scrollbar.vertical {
	/* Hide vertical scrollbar */
	opacity: 0;
}

.monaco-editor .find-widget .matchesCount {
	display: flex;
	flex: initial;
	margin: 0 0 0 3px;
	padding: 2px 0 0 2px;
	height: 25px;
	vertical-align: middle;
	box-sizing: border-box;
	text-align: center;
	line-height: 23px;
}

.monaco-editor .find-widget .button {
	width: 20px;
	height: 20px;
	display: flex;
	flex: initial;
	margin-left: 3px;
	background-position: center center;
	background-repeat: no-repeat;
	cursor: pointer;
	display: flex;
	align-items: center;
	justify-content: center;
}

.monaco-editor .find-widget .button.left {
	margin-left: 0;
	margin-right: 3px;
}

.monaco-editor .find-widget .button.wide {
	width: auto;
	padding: 1px 6px;
	top: -1px;
}

.monaco-editor .find-widget .button.toggle {
	position: absolute;
	top: 0;
	left: 3px;
	width: 18px;
	height: 100%;
	box-sizing: border-box;
}

.monaco-editor .find-widget .button.toggle.disabled {
	display: none;
}

.monaco-editor .find-widget .disabled {
	opacity: 0.3;
	cursor: default;
}

.monaco-editor .find-widget > .replace-part {
	display: none;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput {
	position: relative;
	display: flex;
	vertical-align: middle;
	flex: auto;
	flex-grow: 0;
	flex-shrink: 0;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

/* REDUCED */
.monaco-editor .find-widget.reduced-find-widget .matchesCount {
	display:none;
}

/* NARROW (SMALLER THAN REDUCED) */
.monaco-editor .find-widget.narrow-find-widget {
	max-width: 257px !important;
}

/* COLLAPSED (SMALLER THAN NARROW) */
.monaco-editor .find-widget.collapsed-find-widget {
	max-width: 170px !important;
}

.monaco-editor .find-widget.collapsed-find-widget .button.previous,
.monaco-editor .find-widget.collapsed-find-widget .button.next,
.monaco-editor .find-widget.collapsed-find-widget .button.replace,
.monaco-editor .find-widget.collapsed-find-widget .button.replace-all,
.monaco-editor .find-widget.collapsed-find-widget > .find-part .monaco-findInput .controls {
	display:none;
}

.monaco-editor .findMatch {
	animation-duration: 0;
	animation-name: inherit !important;
}

.monaco-editor .find-widget .monaco-sash {
	left: 0 !important;
}

.monaco-editor.hc-black .find-widget .button:before {
	position: relative;
	top: 1px;
	left: 2px;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvY29udHJpYi9maW5kL2ZpbmRXaWRnZXQuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRixnQkFBZ0I7QUFDaEI7Q0FDQyxrQkFBa0I7Q0FDbEIsV0FBVztDQUNYLFlBQVk7Q0FDWixnQkFBZ0I7Q0FDaEIsaUJBQWlCO0NBQ2pCLGtDQUFrQztDQUNsQyxjQUFjO0NBQ2Qsc0JBQXNCO0NBQ3RCLHlDQUF5QyxFQUFFLGtCQUFrQjtBQUM5RDs7QUFFQTtDQUNDLFdBQVc7QUFDWjs7QUFFQTtDQUNDLGFBQWE7QUFDZDs7QUFFQSwyQ0FBMkM7QUFDM0M7Q0FDQyxhQUFhO0FBQ2Q7O0FBRUE7Q0FDQyx3QkFBd0I7QUFDekI7O0FBRUE7Q0FDQywyQ0FBMkM7Q0FDM0Msb0JBQW9CO0FBQ3JCOztBQUVBO0NBQ0MsNkJBQTZCO0NBQzdCLGFBQWE7QUFDZDs7QUFFQTtDQUNDLGVBQWU7QUFDaEI7O0FBRUE7O0NBRUMsb0JBQW9CO0NBQ3BCLGVBQWU7Q0FDZixhQUFhO0FBQ2Q7O0FBRUE7O0NBRUMsZ0JBQWdCO0FBQ2pCOzs7QUFHQTtDQUNDLG1CQUFtQjtBQUNwQjs7QUFFQTs7OztDQUlDLGdCQUFnQjtDQUNoQixtQkFBbUI7QUFDcEI7O0FBRUE7Q0FDQyxZQUFZO0NBQ1osYUFBYTtDQUNiLG1CQUFtQjtBQUNwQjs7QUFFQTtDQUNDLFlBQVk7Q0FDWixhQUFhO0NBQ2IsbUJBQW1CO0FBQ3BCOztBQUVBO0NBQ0Msc0JBQXNCO0NBQ3RCLGFBQWE7Q0FDYixNQUFNO0FBQ1A7O0FBRUE7Q0FDQyxvREFBb0Q7Q0FDcEQsV0FBVztBQUNaOztBQUVBO0NBQ0MsNEJBQTRCO0NBQzVCLFVBQVU7QUFDWDs7QUFFQTtDQUNDLGFBQWE7Q0FDYixhQUFhO0NBQ2IsaUJBQWlCO0NBQ2pCLG9CQUFvQjtDQUNwQixZQUFZO0NBQ1osc0JBQXNCO0NBQ3RCLHNCQUFzQjtDQUN0QixrQkFBa0I7Q0FDbEIsaUJBQWlCO0FBQ2xCOztBQUVBO0NBQ0MsV0FBVztDQUNYLFlBQVk7Q0FDWixhQUFhO0NBQ2IsYUFBYTtDQUNiLGdCQUFnQjtDQUNoQixrQ0FBa0M7Q0FDbEMsNEJBQTRCO0NBQzVCLGVBQWU7Q0FDZixhQUFhO0NBQ2IsbUJBQW1CO0NBQ25CLHVCQUF1QjtBQUN4Qjs7QUFFQTtDQUNDLGNBQWM7Q0FDZCxpQkFBaUI7QUFDbEI7O0FBRUE7Q0FDQyxXQUFXO0NBQ1gsZ0JBQWdCO0NBQ2hCLFNBQVM7QUFDVjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixNQUFNO0NBQ04sU0FBUztDQUNULFdBQVc7Q0FDWCxZQUFZO0NBQ1osc0JBQXNCO0FBQ3ZCOztBQUVBO0NBQ0MsYUFBYTtBQUNkOztBQUVBO0NBQ0MsWUFBWTtDQUNaLGVBQWU7QUFDaEI7O0FBRUE7Q0FDQyxhQUFhO0FBQ2Q7O0FBRUE7Q0FDQyxrQkFBa0I7Q0FDbEIsYUFBYTtDQUNiLHNCQUFzQjtDQUN0QixVQUFVO0NBQ1YsWUFBWTtDQUNaLGNBQWM7QUFDZjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixRQUFRO0NBQ1IsVUFBVTtBQUNYOztBQUVBLFlBQVk7QUFDWjtDQUNDLFlBQVk7QUFDYjs7QUFFQSxrQ0FBa0M7QUFDbEM7Q0FDQywyQkFBMkI7QUFDNUI7O0FBRUEsb0NBQW9DO0FBQ3BDO0NBQ0MsMkJBQTJCO0FBQzVCOztBQUVBOzs7OztDQUtDLFlBQVk7QUFDYjs7QUFFQTtDQUNDLHFCQUFxQjtDQUNyQixrQ0FBa0M7QUFDbkM7O0FBRUE7Q0FDQyxrQkFBa0I7QUFDbkI7O0FBRUE7Q0FDQyxrQkFBa0I7Q0FDbEIsUUFBUTtDQUNSLFNBQVM7QUFDViIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4vKiBGaW5kIHdpZGdldCAqL1xuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0IHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHR6LWluZGV4OiA1MDtcblx0aGVpZ2h0OiAzM3B4O1xuXHRvdmVyZmxvdzogaGlkZGVuO1xuXHRsaW5lLWhlaWdodDogMTlweDtcblx0dHJhbnNpdGlvbjogdHJhbnNmb3JtIDIwMG1zIGxpbmVhcjtcblx0cGFkZGluZzogMCA0cHg7XG5cdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG5cdHRyYW5zZm9ybTogdHJhbnNsYXRlWShjYWxjKC0xMDAlIC0gMTBweCkpOyAvKiBzaGFkb3cgKDEwcHgpICovXG59XG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCB0ZXh0YXJlYSB7XG5cdG1hcmdpbjogMHB4O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQuaGlkZGVuRWRpdG9yIHtcblx0ZGlzcGxheTogbm9uZTtcbn1cblxuLyogRmluZCB3aWRnZXQgd2hlbiByZXBsYWNlIGlzIHRvZ2dsZWQgb24gKi9cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldC5yZXBsYWNlVG9nZ2xlZCA+IC5yZXBsYWNlLXBhcnQge1xuXHRkaXNwbGF5OiBmbGV4O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQudmlzaWJsZSAge1xuXHR0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoMCk7XG59XG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCAubW9uYWNvLWlucHV0Ym94LnN5bnRoZXRpYy1mb2N1cyB7XG5cdG91dGxpbmU6IDFweCBzb2xpZCAtd2Via2l0LWZvY3VzLXJpbmctY29sb3I7XG5cdG91dGxpbmUtb2Zmc2V0OiAtMXB4O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgLm1vbmFjby1pbnB1dGJveCAuaW5wdXQge1xuXHRiYWNrZ3JvdW5kLWNvbG9yOiB0cmFuc3BhcmVudDtcblx0bWluLWhlaWdodDogMDtcbn1cblxuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0IC5tb25hY28tZmluZElucHV0IC5pbnB1dCB7XG5cdGZvbnQtc2l6ZTogMTNweDtcbn1cblxuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0ID4gLmZpbmQtcGFydCxcbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCA+IC5yZXBsYWNlLXBhcnQge1xuXHRtYXJnaW46IDRweCAwIDAgMTdweDtcblx0Zm9udC1zaXplOiAxMnB4O1xuXHRkaXNwbGF5OiBmbGV4O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgPiAuZmluZC1wYXJ0IC5tb25hY28taW5wdXRib3gsXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgPiAucmVwbGFjZS1wYXJ0IC5tb25hY28taW5wdXRib3gge1xuXHRtaW4taGVpZ2h0OiAyNXB4O1xufVxuXG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCA+IC5yZXBsYWNlLXBhcnQgLm1vbmFjby1pbnB1dGJveCA+IC53cmFwcGVyID4gLm1pcnJvciB7XG5cdHBhZGRpbmctcmlnaHQ6IDIycHg7XG59XG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCA+IC5maW5kLXBhcnQgLm1vbmFjby1pbnB1dGJveCA+IC53cmFwcGVyID4gLmlucHV0LFxuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0ID4gLmZpbmQtcGFydCAubW9uYWNvLWlucHV0Ym94ID4gLndyYXBwZXIgPiAubWlycm9yLFxuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0ID4gLnJlcGxhY2UtcGFydCAubW9uYWNvLWlucHV0Ym94ID4gLndyYXBwZXIgPiAuaW5wdXQsXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgPiAucmVwbGFjZS1wYXJ0IC5tb25hY28taW5wdXRib3ggPiAud3JhcHBlciA+IC5taXJyb3Ige1xuXHRwYWRkaW5nLXRvcDogMnB4O1xuXHRwYWRkaW5nLWJvdHRvbTogMnB4O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgPiAuZmluZC1wYXJ0IC5maW5kLWFjdGlvbnMge1xuXHRoZWlnaHQ6IDI1cHg7XG5cdGRpc3BsYXk6IGZsZXg7XG5cdGFsaWduLWl0ZW1zOiBjZW50ZXI7XG59XG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCA+IC5yZXBsYWNlLXBhcnQgLnJlcGxhY2UtYWN0aW9ucyB7XG5cdGhlaWdodDogMjVweDtcblx0ZGlzcGxheTogZmxleDtcblx0YWxpZ24taXRlbXM6IGNlbnRlcjtcbn1cblxuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0IC5tb25hY28tZmluZElucHV0IHtcblx0dmVydGljYWwtYWxpZ246IG1pZGRsZTtcblx0ZGlzcGxheTogZmxleDtcblx0ZmxleDoxO1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgLm1vbmFjby1maW5kSW5wdXQgLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQge1xuXHQvKiBNYWtlIHN1cmUgdGV4dGFyZWEgaW5oZXJpdHMgdGhlIHdpZHRoIGNvcnJlY3RseSAqL1xuXHR3aWR0aDogMTAwJTtcbn1cblxuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0IC5tb25hY28tZmluZElucHV0IC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50IC5zY3JvbGxiYXIudmVydGljYWwge1xuXHQvKiBIaWRlIHZlcnRpY2FsIHNjcm9sbGJhciAqL1xuXHRvcGFjaXR5OiAwO1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgLm1hdGNoZXNDb3VudCB7XG5cdGRpc3BsYXk6IGZsZXg7XG5cdGZsZXg6IGluaXRpYWw7XG5cdG1hcmdpbjogMCAwIDAgM3B4O1xuXHRwYWRkaW5nOiAycHggMCAwIDJweDtcblx0aGVpZ2h0OiAyNXB4O1xuXHR2ZXJ0aWNhbC1hbGlnbjogbWlkZGxlO1xuXHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xuXHR0ZXh0LWFsaWduOiBjZW50ZXI7XG5cdGxpbmUtaGVpZ2h0OiAyM3B4O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgLmJ1dHRvbiB7XG5cdHdpZHRoOiAyMHB4O1xuXHRoZWlnaHQ6IDIwcHg7XG5cdGRpc3BsYXk6IGZsZXg7XG5cdGZsZXg6IGluaXRpYWw7XG5cdG1hcmdpbi1sZWZ0OiAzcHg7XG5cdGJhY2tncm91bmQtcG9zaXRpb246IGNlbnRlciBjZW50ZXI7XG5cdGJhY2tncm91bmQtcmVwZWF0OiBuby1yZXBlYXQ7XG5cdGN1cnNvcjogcG9pbnRlcjtcblx0ZGlzcGxheTogZmxleDtcblx0YWxpZ24taXRlbXM6IGNlbnRlcjtcblx0anVzdGlmeS1jb250ZW50OiBjZW50ZXI7XG59XG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCAuYnV0dG9uLmxlZnQge1xuXHRtYXJnaW4tbGVmdDogMDtcblx0bWFyZ2luLXJpZ2h0OiAzcHg7XG59XG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCAuYnV0dG9uLndpZGUge1xuXHR3aWR0aDogYXV0bztcblx0cGFkZGluZzogMXB4IDZweDtcblx0dG9wOiAtMXB4O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgLmJ1dHRvbi50b2dnbGUge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdHRvcDogMDtcblx0bGVmdDogM3B4O1xuXHR3aWR0aDogMThweDtcblx0aGVpZ2h0OiAxMDAlO1xuXHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgLmJ1dHRvbi50b2dnbGUuZGlzYWJsZWQge1xuXHRkaXNwbGF5OiBub25lO1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgLmRpc2FibGVkIHtcblx0b3BhY2l0eTogMC4zO1xuXHRjdXJzb3I6IGRlZmF1bHQ7XG59XG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCA+IC5yZXBsYWNlLXBhcnQge1xuXHRkaXNwbGF5OiBub25lO1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgPiAucmVwbGFjZS1wYXJ0ID4gLm1vbmFjby1maW5kSW5wdXQge1xuXHRwb3NpdGlvbjogcmVsYXRpdmU7XG5cdGRpc3BsYXk6IGZsZXg7XG5cdHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7XG5cdGZsZXg6IGF1dG87XG5cdGZsZXgtZ3JvdzogMDtcblx0ZmxleC1zaHJpbms6IDA7XG59XG5cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldCA+IC5yZXBsYWNlLXBhcnQgPiAubW9uYWNvLWZpbmRJbnB1dCA+IC5jb250cm9scyB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0dG9wOiAzcHg7XG5cdHJpZ2h0OiAycHg7XG59XG5cbi8qIFJFRFVDRUQgKi9cbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldC5yZWR1Y2VkLWZpbmQtd2lkZ2V0IC5tYXRjaGVzQ291bnQge1xuXHRkaXNwbGF5Om5vbmU7XG59XG5cbi8qIE5BUlJPVyAoU01BTExFUiBUSEFOIFJFRFVDRUQpICovXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQubmFycm93LWZpbmQtd2lkZ2V0IHtcblx0bWF4LXdpZHRoOiAyNTdweCAhaW1wb3J0YW50O1xufVxuXG4vKiBDT0xMQVBTRUQgKFNNQUxMRVIgVEhBTiBOQVJST1cpICovXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQuY29sbGFwc2VkLWZpbmQtd2lkZ2V0IHtcblx0bWF4LXdpZHRoOiAxNzBweCAhaW1wb3J0YW50O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQuY29sbGFwc2VkLWZpbmQtd2lkZ2V0IC5idXR0b24ucHJldmlvdXMsXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQuY29sbGFwc2VkLWZpbmQtd2lkZ2V0IC5idXR0b24ubmV4dCxcbi5tb25hY28tZWRpdG9yIC5maW5kLXdpZGdldC5jb2xsYXBzZWQtZmluZC13aWRnZXQgLmJ1dHRvbi5yZXBsYWNlLFxuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0LmNvbGxhcHNlZC1maW5kLXdpZGdldCAuYnV0dG9uLnJlcGxhY2UtYWxsLFxuLm1vbmFjby1lZGl0b3IgLmZpbmQtd2lkZ2V0LmNvbGxhcHNlZC1maW5kLXdpZGdldCA+IC5maW5kLXBhcnQgLm1vbmFjby1maW5kSW5wdXQgLmNvbnRyb2xzIHtcblx0ZGlzcGxheTpub25lO1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZE1hdGNoIHtcblx0YW5pbWF0aW9uLWR1cmF0aW9uOiAwO1xuXHRhbmltYXRpb24tbmFtZTogaW5oZXJpdCAhaW1wb3J0YW50O1xufVxuXG4ubW9uYWNvLWVkaXRvciAuZmluZC13aWRnZXQgLm1vbmFjby1zYXNoIHtcblx0bGVmdDogMCAhaW1wb3J0YW50O1xufVxuXG4ubW9uYWNvLWVkaXRvci5oYy1ibGFjayAuZmluZC13aWRnZXQgLmJ1dHRvbjpiZWZvcmUge1xuXHRwb3NpdGlvbjogcmVsYXRpdmU7XG5cdHRvcDogMXB4O1xuXHRsZWZ0OiAycHg7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-sash {
	position: absolute;
	z-index: 35;
	touch-action: none;
}

.monaco-sash.disabled {
	pointer-events: none;
}

.monaco-sash.mac.vertical {
	cursor: col-resize;
}

.monaco-sash.vertical.minimum {
	cursor: e-resize;
}

.monaco-sash.vertical.maximum {
	cursor: w-resize;
}

.monaco-sash.mac.horizontal {
	cursor: row-resize;
}

.monaco-sash.horizontal.minimum {
	cursor: s-resize;
}

.monaco-sash.horizontal.maximum {
	cursor: n-resize;
}

.monaco-sash.disabled {
	cursor: default !important;
	pointer-events: none !important;
}

/** Debug **/

.monaco-sash.debug {
	background: cyan;
}

.monaco-sash.debug.disabled {
	background: rgba(0, 255, 255, 0.2);
}

.monaco-sash.debug:not(.disabled).orthogonal-start::before,
.monaco-sash.debug:not(.disabled).orthogonal-end::after {
	background: red;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvc2FzaC9zYXNoLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxrQkFBa0I7Q0FDbEIsV0FBVztDQUNYLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLG9CQUFvQjtBQUNyQjs7QUFFQTtDQUNDLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLDBCQUEwQjtDQUMxQiwrQkFBK0I7QUFDaEM7O0FBRUEsWUFBWTs7QUFFWjtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGtDQUFrQztBQUNuQzs7QUFFQTs7Q0FFQyxlQUFlO0FBQ2hCIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5tb25hY28tc2FzaCB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0ei1pbmRleDogMzU7XG5cdHRvdWNoLWFjdGlvbjogbm9uZTtcbn1cblxuLm1vbmFjby1zYXNoLmRpc2FibGVkIHtcblx0cG9pbnRlci1ldmVudHM6IG5vbmU7XG59XG5cbi5tb25hY28tc2FzaC5tYWMudmVydGljYWwge1xuXHRjdXJzb3I6IGNvbC1yZXNpemU7XG59XG5cbi5tb25hY28tc2FzaC52ZXJ0aWNhbC5taW5pbXVtIHtcblx0Y3Vyc29yOiBlLXJlc2l6ZTtcbn1cblxuLm1vbmFjby1zYXNoLnZlcnRpY2FsLm1heGltdW0ge1xuXHRjdXJzb3I6IHctcmVzaXplO1xufVxuXG4ubW9uYWNvLXNhc2gubWFjLmhvcml6b250YWwge1xuXHRjdXJzb3I6IHJvdy1yZXNpemU7XG59XG5cbi5tb25hY28tc2FzaC5ob3Jpem9udGFsLm1pbmltdW0ge1xuXHRjdXJzb3I6IHMtcmVzaXplO1xufVxuXG4ubW9uYWNvLXNhc2guaG9yaXpvbnRhbC5tYXhpbXVtIHtcblx0Y3Vyc29yOiBuLXJlc2l6ZTtcbn1cblxuLm1vbmFjby1zYXNoLmRpc2FibGVkIHtcblx0Y3Vyc29yOiBkZWZhdWx0ICFpbXBvcnRhbnQ7XG5cdHBvaW50ZXItZXZlbnRzOiBub25lICFpbXBvcnRhbnQ7XG59XG5cbi8qKiBEZWJ1ZyAqKi9cblxuLm1vbmFjby1zYXNoLmRlYnVnIHtcblx0YmFja2dyb3VuZDogY3lhbjtcbn1cblxuLm1vbmFjby1zYXNoLmRlYnVnLmRpc2FibGVkIHtcblx0YmFja2dyb3VuZDogcmdiYSgwLCAyNTUsIDI1NSwgMC4yKTtcbn1cblxuLm1vbmFjby1zYXNoLmRlYnVnOm5vdCguZGlzYWJsZWQpLm9ydGhvZ29uYWwtc3RhcnQ6OmJlZm9yZSxcbi5tb25hY28tc2FzaC5kZWJ1Zzpub3QoLmRpc2FibGVkKS5vcnRob2dvbmFsLWVuZDo6YWZ0ZXIge1xuXHRiYWNrZ3JvdW5kOiByZWQ7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- Find input ---------- */

.monaco-findInput {
	position: relative;
}

.monaco-findInput .monaco-inputbox {
	font-size: 13px;
	width: 100%;
}

.monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

.vs .monaco-findInput.disabled {
	background-color: #E1E1E1;
}

/* Theming */
.vs-dark .monaco-findInput.disabled {
	background-color: #333;
}

/* Highlighting */
.monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-0 100ms linear 0s;
}
.monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-1 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-0 .controls,
.vs-dark  .monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-dark-0 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-1 .controls,
.vs-dark  .monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-dark-1 100ms linear 0s;
}

@keyframes monaco-findInput-highlight-0 {
	0% { background: rgba(253, 255, 0, 0.8); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-1 {
	0% { background: rgba(253, 255, 0, 0.8); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}

@keyframes monaco-findInput-highlight-dark-0 {
	0% { background: rgba(255, 255, 255, 0.44); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-dark-1 {
	0% { background: rgba(255, 255, 255, 0.44); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvZmluZGlucHV0L2ZpbmRJbnB1dC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7QUFDL0YscUNBQXFDOztBQUVyQztDQUNDLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLGVBQWU7Q0FDZixXQUFXO0FBQ1o7O0FBRUE7Q0FDQyxrQkFBa0I7Q0FDbEIsUUFBUTtDQUNSLFVBQVU7QUFDWDs7QUFFQTtDQUNDLHlCQUF5QjtBQUMxQjs7QUFFQSxZQUFZO0FBQ1o7Q0FDQyxzQkFBc0I7QUFDdkI7O0FBRUEsaUJBQWlCO0FBQ2pCO0NBQ0MsdURBQXVEO0FBQ3hEO0FBQ0E7Q0FDQyx1REFBdUQ7QUFDeEQ7QUFDQTs7Q0FFQyw0REFBNEQ7QUFDN0Q7QUFDQTs7Q0FFQyw0REFBNEQ7QUFDN0Q7O0FBRUE7Q0FDQyxLQUFLLGtDQUFrQyxFQUFFO0NBQ3pDLE9BQU8sdUJBQXVCLEVBQUU7QUFDakM7QUFDQTtDQUNDLEtBQUssa0NBQWtDLEVBQUU7Q0FDekMsa0hBQWtIO0NBQ2xILE1BQU0sdUJBQXVCLEVBQUU7QUFDaEM7O0FBRUE7Q0FDQyxLQUFLLHFDQUFxQyxFQUFFO0NBQzVDLE9BQU8sdUJBQXVCLEVBQUU7QUFDakM7QUFDQTtDQUNDLEtBQUsscUNBQXFDLEVBQUU7Q0FDNUMsa0hBQWtIO0NBQ2xILE1BQU0sdUJBQXVCLEVBQUU7QUFDaEMiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi8qIC0tLS0tLS0tLS0gRmluZCBpbnB1dCAtLS0tLS0tLS0tICovXG5cbi5tb25hY28tZmluZElucHV0IHtcblx0cG9zaXRpb246IHJlbGF0aXZlO1xufVxuXG4ubW9uYWNvLWZpbmRJbnB1dCAubW9uYWNvLWlucHV0Ym94IHtcblx0Zm9udC1zaXplOiAxM3B4O1xuXHR3aWR0aDogMTAwJTtcbn1cblxuLm1vbmFjby1maW5kSW5wdXQgPiAuY29udHJvbHMge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdHRvcDogM3B4O1xuXHRyaWdodDogMnB4O1xufVxuXG4udnMgLm1vbmFjby1maW5kSW5wdXQuZGlzYWJsZWQge1xuXHRiYWNrZ3JvdW5kLWNvbG9yOiAjRTFFMUUxO1xufVxuXG4vKiBUaGVtaW5nICovXG4udnMtZGFyayAubW9uYWNvLWZpbmRJbnB1dC5kaXNhYmxlZCB7XG5cdGJhY2tncm91bmQtY29sb3I6ICMzMzM7XG59XG5cbi8qIEhpZ2hsaWdodGluZyAqL1xuLm1vbmFjby1maW5kSW5wdXQuaGlnaGxpZ2h0LTAgLmNvbnRyb2xzIHtcblx0YW5pbWF0aW9uOiBtb25hY28tZmluZElucHV0LWhpZ2hsaWdodC0wIDEwMG1zIGxpbmVhciAwcztcbn1cbi5tb25hY28tZmluZElucHV0LmhpZ2hsaWdodC0xIC5jb250cm9scyB7XG5cdGFuaW1hdGlvbjogbW9uYWNvLWZpbmRJbnB1dC1oaWdobGlnaHQtMSAxMDBtcyBsaW5lYXIgMHM7XG59XG4uaGMtYmxhY2sgLm1vbmFjby1maW5kSW5wdXQuaGlnaGxpZ2h0LTAgLmNvbnRyb2xzLFxuLnZzLWRhcmsgIC5tb25hY28tZmluZElucHV0LmhpZ2hsaWdodC0wIC5jb250cm9scyB7XG5cdGFuaW1hdGlvbjogbW9uYWNvLWZpbmRJbnB1dC1oaWdobGlnaHQtZGFyay0wIDEwMG1zIGxpbmVhciAwcztcbn1cbi5oYy1ibGFjayAubW9uYWNvLWZpbmRJbnB1dC5oaWdobGlnaHQtMSAuY29udHJvbHMsXG4udnMtZGFyayAgLm1vbmFjby1maW5kSW5wdXQuaGlnaGxpZ2h0LTEgLmNvbnRyb2xzIHtcblx0YW5pbWF0aW9uOiBtb25hY28tZmluZElucHV0LWhpZ2hsaWdodC1kYXJrLTEgMTAwbXMgbGluZWFyIDBzO1xufVxuXG5Aa2V5ZnJhbWVzIG1vbmFjby1maW5kSW5wdXQtaGlnaGxpZ2h0LTAge1xuXHQwJSB7IGJhY2tncm91bmQ6IHJnYmEoMjUzLCAyNTUsIDAsIDAuOCk7IH1cblx0MTAwJSB7IGJhY2tncm91bmQ6IHRyYW5zcGFyZW50OyB9XG59XG5Aa2V5ZnJhbWVzIG1vbmFjby1maW5kSW5wdXQtaGlnaGxpZ2h0LTEge1xuXHQwJSB7IGJhY2tncm91bmQ6IHJnYmEoMjUzLCAyNTUsIDAsIDAuOCk7IH1cblx0LyogTWFkZSBpbnRlbnRpb25hbGx5IGRpZmZlcmVudCBzdWNoIHRoYXQgdGhlIENTUyBtaW5pZmllciBkb2VzIG5vdCBjb2xsYXBzZSB0aGUgdHdvIGFuaW1hdGlvbnMgaW50byBhIHNpbmdsZSBvbmUqL1xuXHQ5OSUgeyBiYWNrZ3JvdW5kOiB0cmFuc3BhcmVudDsgfVxufVxuXG5Aa2V5ZnJhbWVzIG1vbmFjby1maW5kSW5wdXQtaGlnaGxpZ2h0LWRhcmstMCB7XG5cdDAlIHsgYmFja2dyb3VuZDogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjQ0KTsgfVxuXHQxMDAlIHsgYmFja2dyb3VuZDogdHJhbnNwYXJlbnQ7IH1cbn1cbkBrZXlmcmFtZXMgbW9uYWNvLWZpbmRJbnB1dC1oaWdobGlnaHQtZGFyay0xIHtcblx0MCUgeyBiYWNrZ3JvdW5kOiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuNDQpOyB9XG5cdC8qIE1hZGUgaW50ZW50aW9uYWxseSBkaWZmZXJlbnQgc3VjaCB0aGF0IHRoZSBDU1MgbWluaWZpZXIgZG9lcyBub3QgY29sbGFwc2UgdGhlIHR3byBhbmltYXRpb25zIGludG8gYSBzaW5nbGUgb25lKi9cblx0OTklIHsgYmFja2dyb3VuZDogdHJhbnNwYXJlbnQ7IH1cbn0iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-inputbox {
	position: relative;
	display: block;
	padding: 0;
	box-sizing:	border-box;

	/* Customizable */
	font-size: inherit;
}

.monaco-inputbox.idle {
	border: 1px solid transparent;
}

.monaco-inputbox > .wrapper > .input,
.monaco-inputbox > .wrapper > .mirror {

	/* Customizable */
	padding: 4px;
}

.monaco-inputbox > .wrapper {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-inputbox > .wrapper > .input {
	display: inline-block;
	box-sizing:	border-box;
	width: 100%;
	height: 100%;
	line-height: inherit;
	border: none;
	font-family: inherit;
	font-size: inherit;
	resize: none;
	color: inherit;
}

.monaco-inputbox > .wrapper > input {
	text-overflow: ellipsis;
}

.monaco-inputbox > .wrapper > textarea.input {
	display: block;
	-ms-overflow-style: none; /* IE 10+: hide scrollbars */
	scrollbar-width: none; /* Firefox: hide scrollbars */
	outline: none;
}

.monaco-inputbox > .wrapper > textarea.input::-webkit-scrollbar {
	display: none; /* Chrome + Safari: hide scrollbar */
}

.monaco-inputbox > .wrapper > textarea.input.empty {
	white-space: nowrap;
}

.monaco-inputbox > .wrapper > .mirror {
	position: absolute;
	display: inline-block;
	width: 100%;
	top: 0;
	left: 0;
	box-sizing: border-box;
	white-space: pre-wrap;
	visibility: hidden;
	word-wrap: break-word;
}

/* Context view */

.monaco-inputbox-container {
	text-align: right;
}

.monaco-inputbox-container .monaco-inputbox-message {
	display: inline-block;
	overflow: hidden;
	text-align: left;
	width: 100%;
	box-sizing:	border-box;
	padding: 0.4em;
	font-size: 12px;
	line-height: 17px;
	min-height: 34px;
	margin-top: -1px;
	word-wrap: break-word;
}

/* Action bar support */
.monaco-inputbox .monaco-action-bar {
	position: absolute;
	right: 2px;
	top: 4px;
}

.monaco-inputbox .monaco-action-bar .action-item {
	margin-left: 2px;
}

.monaco-inputbox .monaco-action-bar .action-item .codicon {
	background-repeat: no-repeat;
	width: 16px;
	height: 16px;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvaW5wdXRib3gvaW5wdXRCb3guY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLGtCQUFrQjtDQUNsQixjQUFjO0NBQ2QsVUFBVTtDQUNWLHNCQUFzQjs7Q0FFdEIsaUJBQWlCO0NBQ2pCLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLDZCQUE2QjtBQUM5Qjs7QUFFQTs7O0NBR0MsaUJBQWlCO0NBQ2pCLFlBQVk7QUFDYjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixXQUFXO0NBQ1gsWUFBWTtBQUNiOztBQUVBO0NBQ0MscUJBQXFCO0NBQ3JCLHNCQUFzQjtDQUN0QixXQUFXO0NBQ1gsWUFBWTtDQUNaLG9CQUFvQjtDQUNwQixZQUFZO0NBQ1osb0JBQW9CO0NBQ3BCLGtCQUFrQjtDQUNsQixZQUFZO0NBQ1osY0FBYztBQUNmOztBQUVBO0NBQ0MsdUJBQXVCO0FBQ3hCOztBQUVBO0NBQ0MsY0FBYztDQUNkLHdCQUF3QixFQUFFLDRCQUE0QjtDQUN0RCxxQkFBcUIsRUFBRSw2QkFBNkI7Q0FDcEQsYUFBYTtBQUNkOztBQUVBO0NBQ0MsYUFBYSxFQUFFLG9DQUFvQztBQUNwRDs7QUFFQTtDQUNDLG1CQUFtQjtBQUNwQjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixxQkFBcUI7Q0FDckIsV0FBVztDQUNYLE1BQU07Q0FDTixPQUFPO0NBQ1Asc0JBQXNCO0NBQ3RCLHFCQUFxQjtDQUNyQixrQkFBa0I7Q0FDbEIscUJBQXFCO0FBQ3RCOztBQUVBLGlCQUFpQjs7QUFFakI7Q0FDQyxpQkFBaUI7QUFDbEI7O0FBRUE7Q0FDQyxxQkFBcUI7Q0FDckIsZ0JBQWdCO0NBQ2hCLGdCQUFnQjtDQUNoQixXQUFXO0NBQ1gsc0JBQXNCO0NBQ3RCLGNBQWM7Q0FDZCxlQUFlO0NBQ2YsaUJBQWlCO0NBQ2pCLGdCQUFnQjtDQUNoQixnQkFBZ0I7Q0FDaEIscUJBQXFCO0FBQ3RCOztBQUVBLHVCQUF1QjtBQUN2QjtDQUNDLGtCQUFrQjtDQUNsQixVQUFVO0NBQ1YsUUFBUTtBQUNUOztBQUVBO0NBQ0MsZ0JBQWdCO0FBQ2pCOztBQUVBO0NBQ0MsNEJBQTRCO0NBQzVCLFdBQVc7Q0FDWCxZQUFZO0FBQ2IiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLm1vbmFjby1pbnB1dGJveCB7XG5cdHBvc2l0aW9uOiByZWxhdGl2ZTtcblx0ZGlzcGxheTogYmxvY2s7XG5cdHBhZGRpbmc6IDA7XG5cdGJveC1zaXppbmc6XHRib3JkZXItYm94O1xuXG5cdC8qIEN1c3RvbWl6YWJsZSAqL1xuXHRmb250LXNpemU6IGluaGVyaXQ7XG59XG5cbi5tb25hY28taW5wdXRib3guaWRsZSB7XG5cdGJvcmRlcjogMXB4IHNvbGlkIHRyYW5zcGFyZW50O1xufVxuXG4ubW9uYWNvLWlucHV0Ym94ID4gLndyYXBwZXIgPiAuaW5wdXQsXG4ubW9uYWNvLWlucHV0Ym94ID4gLndyYXBwZXIgPiAubWlycm9yIHtcblxuXHQvKiBDdXN0b21pemFibGUgKi9cblx0cGFkZGluZzogNHB4O1xufVxuXG4ubW9uYWNvLWlucHV0Ym94ID4gLndyYXBwZXIge1xuXHRwb3NpdGlvbjogcmVsYXRpdmU7XG5cdHdpZHRoOiAxMDAlO1xuXHRoZWlnaHQ6IDEwMCU7XG59XG5cbi5tb25hY28taW5wdXRib3ggPiAud3JhcHBlciA+IC5pbnB1dCB7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0Ym94LXNpemluZzpcdGJvcmRlci1ib3g7XG5cdHdpZHRoOiAxMDAlO1xuXHRoZWlnaHQ6IDEwMCU7XG5cdGxpbmUtaGVpZ2h0OiBpbmhlcml0O1xuXHRib3JkZXI6IG5vbmU7XG5cdGZvbnQtZmFtaWx5OiBpbmhlcml0O1xuXHRmb250LXNpemU6IGluaGVyaXQ7XG5cdHJlc2l6ZTogbm9uZTtcblx0Y29sb3I6IGluaGVyaXQ7XG59XG5cbi5tb25hY28taW5wdXRib3ggPiAud3JhcHBlciA+IGlucHV0IHtcblx0dGV4dC1vdmVyZmxvdzogZWxsaXBzaXM7XG59XG5cbi5tb25hY28taW5wdXRib3ggPiAud3JhcHBlciA+IHRleHRhcmVhLmlucHV0IHtcblx0ZGlzcGxheTogYmxvY2s7XG5cdC1tcy1vdmVyZmxvdy1zdHlsZTogbm9uZTsgLyogSUUgMTArOiBoaWRlIHNjcm9sbGJhcnMgKi9cblx0c2Nyb2xsYmFyLXdpZHRoOiBub25lOyAvKiBGaXJlZm94OiBoaWRlIHNjcm9sbGJhcnMgKi9cblx0b3V0bGluZTogbm9uZTtcbn1cblxuLm1vbmFjby1pbnB1dGJveCA+IC53cmFwcGVyID4gdGV4dGFyZWEuaW5wdXQ6Oi13ZWJraXQtc2Nyb2xsYmFyIHtcblx0ZGlzcGxheTogbm9uZTsgLyogQ2hyb21lICsgU2FmYXJpOiBoaWRlIHNjcm9sbGJhciAqL1xufVxuXG4ubW9uYWNvLWlucHV0Ym94ID4gLndyYXBwZXIgPiB0ZXh0YXJlYS5pbnB1dC5lbXB0eSB7XG5cdHdoaXRlLXNwYWNlOiBub3dyYXA7XG59XG5cbi5tb25hY28taW5wdXRib3ggPiAud3JhcHBlciA+IC5taXJyb3Ige1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0d2lkdGg6IDEwMCU7XG5cdHRvcDogMDtcblx0bGVmdDogMDtcblx0Ym94LXNpemluZzogYm9yZGVyLWJveDtcblx0d2hpdGUtc3BhY2U6IHByZS13cmFwO1xuXHR2aXNpYmlsaXR5OiBoaWRkZW47XG5cdHdvcmQtd3JhcDogYnJlYWstd29yZDtcbn1cblxuLyogQ29udGV4dCB2aWV3ICovXG5cbi5tb25hY28taW5wdXRib3gtY29udGFpbmVyIHtcblx0dGV4dC1hbGlnbjogcmlnaHQ7XG59XG5cbi5tb25hY28taW5wdXRib3gtY29udGFpbmVyIC5tb25hY28taW5wdXRib3gtbWVzc2FnZSB7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0b3ZlcmZsb3c6IGhpZGRlbjtcblx0dGV4dC1hbGlnbjogbGVmdDtcblx0d2lkdGg6IDEwMCU7XG5cdGJveC1zaXppbmc6XHRib3JkZXItYm94O1xuXHRwYWRkaW5nOiAwLjRlbTtcblx0Zm9udC1zaXplOiAxMnB4O1xuXHRsaW5lLWhlaWdodDogMTdweDtcblx0bWluLWhlaWdodDogMzRweDtcblx0bWFyZ2luLXRvcDogLTFweDtcblx0d29yZC13cmFwOiBicmVhay13b3JkO1xufVxuXG4vKiBBY3Rpb24gYmFyIHN1cHBvcnQgKi9cbi5tb25hY28taW5wdXRib3ggLm1vbmFjby1hY3Rpb24tYmFyIHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHRyaWdodDogMnB4O1xuXHR0b3A6IDRweDtcbn1cblxuLm1vbmFjby1pbnB1dGJveCAubW9uYWNvLWFjdGlvbi1iYXIgLmFjdGlvbi1pdGVtIHtcblx0bWFyZ2luLWxlZnQ6IDJweDtcbn1cblxuLm1vbmFjby1pbnB1dGJveCAubW9uYWNvLWFjdGlvbi1iYXIgLmFjdGlvbi1pdGVtIC5jb2RpY29uIHtcblx0YmFja2dyb3VuZC1yZXBlYXQ6IG5vLXJlcGVhdDtcblx0d2lkdGg6IDE2cHg7XG5cdGhlaWdodDogMTZweDtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar {
	text-align: right;
	white-space: nowrap;
}

.monaco-action-bar .actions-container {
	display: flex;
	margin: 0 auto;
	padding: 0;
	width: 100%;
	justify-content: flex-end;
}

.monaco-action-bar.vertical .actions-container {
	display: inline-block;
}

.monaco-action-bar.reverse .actions-container {
	flex-direction: row-reverse;
}

.monaco-action-bar .action-item {
	cursor: pointer;
	display: inline-block;
	transition: transform 50ms ease;
	position: relative;  /* DO NOT REMOVE - this is the key to preventing the ghosting icon bug in Chrome 42 */
}

.monaco-action-bar .action-item.disabled {
	cursor: default;
}

.monaco-action-bar.animated .action-item.active {
	transform: scale(1.272019649, 1.272019649); /* 1.272019649 = √φ */
}

.monaco-action-bar .action-item .icon,
.monaco-action-bar .action-item .codicon {
	display: inline-block;
}

.monaco-action-bar .action-item .codicon {
	display: flex;
	align-items: center;
}

.monaco-action-bar .action-label {
	font-size: 11px;
	margin-right: 4px;
}

.monaco-action-bar .action-item.disabled .action-label,
.monaco-action-bar .action-item.disabled .action-label:hover {
	opacity: 0.4;
}

/* Vertical actions */

.monaco-action-bar.vertical {
	text-align: left;
}

.monaco-action-bar.vertical .action-item {
	display: block;
}

.monaco-action-bar.vertical .action-label.separator {
	display: block;
	border-bottom: 1px solid #bbb;
	padding-top: 1px;
	margin-left: .8em;
	margin-right: .8em;
}

.monaco-action-bar.animated.vertical .action-item.active {
	transform: translate(5px, 0);
}

.secondary-actions .monaco-action-bar .action-label {
	margin-left: 6px;
}

/* Action Items */
.monaco-action-bar .action-item.select-container {
	overflow: hidden; /* somehow the dropdown overflows its container, we prevent it here to not push */
	flex: 1;
	max-width: 170px;
	min-width: 60px;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-right: 10px;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvYWN0aW9uYmFyL2FjdGlvbmJhci5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GO0NBQ0MsaUJBQWlCO0NBQ2pCLG1CQUFtQjtBQUNwQjs7QUFFQTtDQUNDLGFBQWE7Q0FDYixjQUFjO0NBQ2QsVUFBVTtDQUNWLFdBQVc7Q0FDWCx5QkFBeUI7QUFDMUI7O0FBRUE7Q0FDQyxxQkFBcUI7QUFDdEI7O0FBRUE7Q0FDQywyQkFBMkI7QUFDNUI7O0FBRUE7Q0FDQyxlQUFlO0NBQ2YscUJBQXFCO0NBQ3JCLCtCQUErQjtDQUMvQixrQkFBa0IsR0FBRyxxRkFBcUY7QUFDM0c7O0FBRUE7Q0FDQyxlQUFlO0FBQ2hCOztBQUVBO0NBQ0MsMENBQTBDLEVBQUUscUJBQXFCO0FBQ2xFOztBQUVBOztDQUVDLHFCQUFxQjtBQUN0Qjs7QUFFQTtDQUNDLGFBQWE7Q0FDYixtQkFBbUI7QUFDcEI7O0FBRUE7Q0FDQyxlQUFlO0NBQ2YsaUJBQWlCO0FBQ2xCOztBQUVBOztDQUVDLFlBQVk7QUFDYjs7QUFFQSxxQkFBcUI7O0FBRXJCO0NBQ0MsZ0JBQWdCO0FBQ2pCOztBQUVBO0NBQ0MsY0FBYztBQUNmOztBQUVBO0NBQ0MsY0FBYztDQUNkLDZCQUE2QjtDQUM3QixnQkFBZ0I7Q0FDaEIsaUJBQWlCO0NBQ2pCLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLDRCQUE0QjtBQUM3Qjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQSxpQkFBaUI7QUFDakI7Q0FDQyxnQkFBZ0IsRUFBRSxpRkFBaUY7Q0FDbkcsT0FBTztDQUNQLGdCQUFnQjtDQUNoQixlQUFlO0NBQ2YsYUFBYTtDQUNiLG1CQUFtQjtDQUNuQix1QkFBdUI7Q0FDdkIsa0JBQWtCO0FBQ25CIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5tb25hY28tYWN0aW9uLWJhciB7XG5cdHRleHQtYWxpZ246IHJpZ2h0O1xuXHR3aGl0ZS1zcGFjZTogbm93cmFwO1xufVxuXG4ubW9uYWNvLWFjdGlvbi1iYXIgLmFjdGlvbnMtY29udGFpbmVyIHtcblx0ZGlzcGxheTogZmxleDtcblx0bWFyZ2luOiAwIGF1dG87XG5cdHBhZGRpbmc6IDA7XG5cdHdpZHRoOiAxMDAlO1xuXHRqdXN0aWZ5LWNvbnRlbnQ6IGZsZXgtZW5kO1xufVxuXG4ubW9uYWNvLWFjdGlvbi1iYXIudmVydGljYWwgLmFjdGlvbnMtY29udGFpbmVyIHtcblx0ZGlzcGxheTogaW5saW5lLWJsb2NrO1xufVxuXG4ubW9uYWNvLWFjdGlvbi1iYXIucmV2ZXJzZSAuYWN0aW9ucy1jb250YWluZXIge1xuXHRmbGV4LWRpcmVjdGlvbjogcm93LXJldmVyc2U7XG59XG5cbi5tb25hY28tYWN0aW9uLWJhciAuYWN0aW9uLWl0ZW0ge1xuXHRjdXJzb3I6IHBvaW50ZXI7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0dHJhbnNpdGlvbjogdHJhbnNmb3JtIDUwbXMgZWFzZTtcblx0cG9zaXRpb246IHJlbGF0aXZlOyAgLyogRE8gTk9UIFJFTU9WRSAtIHRoaXMgaXMgdGhlIGtleSB0byBwcmV2ZW50aW5nIHRoZSBnaG9zdGluZyBpY29uIGJ1ZyBpbiBDaHJvbWUgNDIgKi9cbn1cblxuLm1vbmFjby1hY3Rpb24tYmFyIC5hY3Rpb24taXRlbS5kaXNhYmxlZCB7XG5cdGN1cnNvcjogZGVmYXVsdDtcbn1cblxuLm1vbmFjby1hY3Rpb24tYmFyLmFuaW1hdGVkIC5hY3Rpb24taXRlbS5hY3RpdmUge1xuXHR0cmFuc2Zvcm06IHNjYWxlKDEuMjcyMDE5NjQ5LCAxLjI3MjAxOTY0OSk7IC8qIDEuMjcyMDE5NjQ5ID0g4oiaz4YgKi9cbn1cblxuLm1vbmFjby1hY3Rpb24tYmFyIC5hY3Rpb24taXRlbSAuaWNvbixcbi5tb25hY28tYWN0aW9uLWJhciAuYWN0aW9uLWl0ZW0gLmNvZGljb24ge1xuXHRkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG59XG5cbi5tb25hY28tYWN0aW9uLWJhciAuYWN0aW9uLWl0ZW0gLmNvZGljb24ge1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRhbGlnbi1pdGVtczogY2VudGVyO1xufVxuXG4ubW9uYWNvLWFjdGlvbi1iYXIgLmFjdGlvbi1sYWJlbCB7XG5cdGZvbnQtc2l6ZTogMTFweDtcblx0bWFyZ2luLXJpZ2h0OiA0cHg7XG59XG5cbi5tb25hY28tYWN0aW9uLWJhciAuYWN0aW9uLWl0ZW0uZGlzYWJsZWQgLmFjdGlvbi1sYWJlbCxcbi5tb25hY28tYWN0aW9uLWJhciAuYWN0aW9uLWl0ZW0uZGlzYWJsZWQgLmFjdGlvbi1sYWJlbDpob3ZlciB7XG5cdG9wYWNpdHk6IDAuNDtcbn1cblxuLyogVmVydGljYWwgYWN0aW9ucyAqL1xuXG4ubW9uYWNvLWFjdGlvbi1iYXIudmVydGljYWwge1xuXHR0ZXh0LWFsaWduOiBsZWZ0O1xufVxuXG4ubW9uYWNvLWFjdGlvbi1iYXIudmVydGljYWwgLmFjdGlvbi1pdGVtIHtcblx0ZGlzcGxheTogYmxvY2s7XG59XG5cbi5tb25hY28tYWN0aW9uLWJhci52ZXJ0aWNhbCAuYWN0aW9uLWxhYmVsLnNlcGFyYXRvciB7XG5cdGRpc3BsYXk6IGJsb2NrO1xuXHRib3JkZXItYm90dG9tOiAxcHggc29saWQgI2JiYjtcblx0cGFkZGluZy10b3A6IDFweDtcblx0bWFyZ2luLWxlZnQ6IC44ZW07XG5cdG1hcmdpbi1yaWdodDogLjhlbTtcbn1cblxuLm1vbmFjby1hY3Rpb24tYmFyLmFuaW1hdGVkLnZlcnRpY2FsIC5hY3Rpb24taXRlbS5hY3RpdmUge1xuXHR0cmFuc2Zvcm06IHRyYW5zbGF0ZSg1cHgsIDApO1xufVxuXG4uc2Vjb25kYXJ5LWFjdGlvbnMgLm1vbmFjby1hY3Rpb24tYmFyIC5hY3Rpb24tbGFiZWwge1xuXHRtYXJnaW4tbGVmdDogNnB4O1xufVxuXG4vKiBBY3Rpb24gSXRlbXMgKi9cbi5tb25hY28tYWN0aW9uLWJhciAuYWN0aW9uLWl0ZW0uc2VsZWN0LWNvbnRhaW5lciB7XG5cdG92ZXJmbG93OiBoaWRkZW47IC8qIHNvbWVob3cgdGhlIGRyb3Bkb3duIG92ZXJmbG93cyBpdHMgY29udGFpbmVyLCB3ZSBwcmV2ZW50IGl0IGhlcmUgdG8gbm90IHB1c2ggKi9cblx0ZmxleDogMTtcblx0bWF4LXdpZHRoOiAxNzBweDtcblx0bWluLXdpZHRoOiA2MHB4O1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRhbGlnbi1pdGVtczogY2VudGVyO1xuXHRqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcblx0bWFyZ2luLXJpZ2h0OiAxMHB4O1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Arrows */
.monaco-scrollable-element > .scrollbar > .scra {
	cursor: pointer;
	font-size: 11px !important;
}

.monaco-scrollable-element > .visible {
	opacity: 1;

	/* Background rule added for IE9 - to allow clicks on dom node */
	background:rgba(0,0,0,0);

	transition: opacity 100ms linear;
}
.monaco-scrollable-element > .invisible {
	opacity: 0;
	pointer-events: none;
}
.monaco-scrollable-element > .invisible.fade {
	transition: opacity 800ms linear;
}

/* Scrollable Content Inset Shadow */
.monaco-scrollable-element > .shadow {
	position: absolute;
	display: none;
}
.monaco-scrollable-element > .shadow.top {
	display: block;
	top: 0;
	left: 3px;
	height: 3px;
	width: 100%;
	box-shadow: #DDD 0 6px 6px -6px inset;
}
.monaco-scrollable-element > .shadow.left {
	display: block;
	top: 3px;
	left: 0;
	height: 100%;
	width: 3px;
	box-shadow: #DDD 6px 0 6px -6px inset;
}
.monaco-scrollable-element > .shadow.top-left-corner {
	display: block;
	top: 0;
	left: 0;
	height: 3px;
	width: 3px;
}
.monaco-scrollable-element > .shadow.top.left {
	box-shadow: #DDD 6px 6px 6px -6px inset;
}

/* ---------- Default Style ---------- */

.vs .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(100, 100, 100, .4);
}
.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(121, 121, 121, .4);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(111, 195, 223, .6);
}

.monaco-scrollable-element > .scrollbar > .slider:hover {
	background: rgba(100, 100, 100, .7);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider:hover {
	background: rgba(111, 195, 223, .8);
}

.monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(0, 0, 0, .6);
}
.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(191, 191, 191, .4);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(111, 195, 223, 1);
}

.vs-dark .monaco-scrollable-element .shadow.top {
	box-shadow: none;
}

.vs-dark .monaco-scrollable-element .shadow.left {
	box-shadow: #000 6px 0 6px -6px inset;
}

.vs-dark .monaco-scrollable-element .shadow.top.left {
	box-shadow: #000 6px 6px 6px -6px inset;
}

.hc-black .monaco-scrollable-element .shadow.top {
	box-shadow: none;
}

.hc-black .monaco-scrollable-element .shadow.left {
	box-shadow: none;
}

.hc-black .monaco-scrollable-element .shadow.top.left {
	box-shadow: none;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvc2Nyb2xsYmFyL21lZGlhL3Njcm9sbGJhcnMuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRixXQUFXO0FBQ1g7Q0FDQyxlQUFlO0NBQ2YsMEJBQTBCO0FBQzNCOztBQUVBO0NBQ0MsVUFBVTs7Q0FFVixnRUFBZ0U7Q0FDaEUsd0JBQXdCOztDQUV4QixnQ0FBZ0M7QUFDakM7QUFDQTtDQUNDLFVBQVU7Q0FDVixvQkFBb0I7QUFDckI7QUFDQTtDQUNDLGdDQUFnQztBQUNqQzs7QUFFQSxvQ0FBb0M7QUFDcEM7Q0FDQyxrQkFBa0I7Q0FDbEIsYUFBYTtBQUNkO0FBQ0E7Q0FDQyxjQUFjO0NBQ2QsTUFBTTtDQUNOLFNBQVM7Q0FDVCxXQUFXO0NBQ1gsV0FBVztDQUNYLHFDQUFxQztBQUN0QztBQUNBO0NBQ0MsY0FBYztDQUNkLFFBQVE7Q0FDUixPQUFPO0NBQ1AsWUFBWTtDQUNaLFVBQVU7Q0FDVixxQ0FBcUM7QUFDdEM7QUFDQTtDQUNDLGNBQWM7Q0FDZCxNQUFNO0NBQ04sT0FBTztDQUNQLFdBQVc7Q0FDWCxVQUFVO0FBQ1g7QUFDQTtDQUNDLHVDQUF1QztBQUN4Qzs7QUFFQSx3Q0FBd0M7O0FBRXhDO0NBQ0MsbUNBQW1DO0FBQ3BDO0FBQ0E7Q0FDQyxtQ0FBbUM7QUFDcEM7QUFDQTtDQUNDLG1DQUFtQztBQUNwQzs7QUFFQTtDQUNDLG1DQUFtQztBQUNwQztBQUNBO0NBQ0MsbUNBQW1DO0FBQ3BDOztBQUVBO0NBQ0MsNkJBQTZCO0FBQzlCO0FBQ0E7Q0FDQyxtQ0FBbUM7QUFDcEM7QUFDQTtDQUNDLGtDQUFrQztBQUNuQzs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLHFDQUFxQztBQUN0Qzs7QUFFQTtDQUNDLHVDQUF1QztBQUN4Qzs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4vKiBBcnJvd3MgKi9cbi5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50ID4gLnNjcm9sbGJhciA+IC5zY3JhIHtcblx0Y3Vyc29yOiBwb2ludGVyO1xuXHRmb250LXNpemU6IDExcHggIWltcG9ydGFudDtcbn1cblxuLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAudmlzaWJsZSB7XG5cdG9wYWNpdHk6IDE7XG5cblx0LyogQmFja2dyb3VuZCBydWxlIGFkZGVkIGZvciBJRTkgLSB0byBhbGxvdyBjbGlja3Mgb24gZG9tIG5vZGUgKi9cblx0YmFja2dyb3VuZDpyZ2JhKDAsMCwwLDApO1xuXG5cdHRyYW5zaXRpb246IG9wYWNpdHkgMTAwbXMgbGluZWFyO1xufVxuLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuaW52aXNpYmxlIHtcblx0b3BhY2l0eTogMDtcblx0cG9pbnRlci1ldmVudHM6IG5vbmU7XG59XG4ubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCA+IC5pbnZpc2libGUuZmFkZSB7XG5cdHRyYW5zaXRpb246IG9wYWNpdHkgODAwbXMgbGluZWFyO1xufVxuXG4vKiBTY3JvbGxhYmxlIENvbnRlbnQgSW5zZXQgU2hhZG93ICovXG4ubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCA+IC5zaGFkb3cge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdGRpc3BsYXk6IG5vbmU7XG59XG4ubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCA+IC5zaGFkb3cudG9wIHtcblx0ZGlzcGxheTogYmxvY2s7XG5cdHRvcDogMDtcblx0bGVmdDogM3B4O1xuXHRoZWlnaHQ6IDNweDtcblx0d2lkdGg6IDEwMCU7XG5cdGJveC1zaGFkb3c6ICNEREQgMCA2cHggNnB4IC02cHggaW5zZXQ7XG59XG4ubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCA+IC5zaGFkb3cubGVmdCB7XG5cdGRpc3BsYXk6IGJsb2NrO1xuXHR0b3A6IDNweDtcblx0bGVmdDogMDtcblx0aGVpZ2h0OiAxMDAlO1xuXHR3aWR0aDogM3B4O1xuXHRib3gtc2hhZG93OiAjREREIDZweCAwIDZweCAtNnB4IGluc2V0O1xufVxuLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuc2hhZG93LnRvcC1sZWZ0LWNvcm5lciB7XG5cdGRpc3BsYXk6IGJsb2NrO1xuXHR0b3A6IDA7XG5cdGxlZnQ6IDA7XG5cdGhlaWdodDogM3B4O1xuXHR3aWR0aDogM3B4O1xufVxuLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuc2hhZG93LnRvcC5sZWZ0IHtcblx0Ym94LXNoYWRvdzogI0RERCA2cHggNnB4IDZweCAtNnB4IGluc2V0O1xufVxuXG4vKiAtLS0tLS0tLS0tIERlZmF1bHQgU3R5bGUgLS0tLS0tLS0tLSAqL1xuXG4udnMgLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuc2Nyb2xsYmFyID4gLnNsaWRlciB7XG5cdGJhY2tncm91bmQ6IHJnYmEoMTAwLCAxMDAsIDEwMCwgLjQpO1xufVxuLnZzLWRhcmsgLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuc2Nyb2xsYmFyID4gLnNsaWRlciB7XG5cdGJhY2tncm91bmQ6IHJnYmEoMTIxLCAxMjEsIDEyMSwgLjQpO1xufVxuLmhjLWJsYWNrIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50ID4gLnNjcm9sbGJhciA+IC5zbGlkZXIge1xuXHRiYWNrZ3JvdW5kOiByZ2JhKDExMSwgMTk1LCAyMjMsIC42KTtcbn1cblxuLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuc2Nyb2xsYmFyID4gLnNsaWRlcjpob3ZlciB7XG5cdGJhY2tncm91bmQ6IHJnYmEoMTAwLCAxMDAsIDEwMCwgLjcpO1xufVxuLmhjLWJsYWNrIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50ID4gLnNjcm9sbGJhciA+IC5zbGlkZXI6aG92ZXIge1xuXHRiYWNrZ3JvdW5kOiByZ2JhKDExMSwgMTk1LCAyMjMsIC44KTtcbn1cblxuLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuc2Nyb2xsYmFyID4gLnNsaWRlci5hY3RpdmUge1xuXHRiYWNrZ3JvdW5kOiByZ2JhKDAsIDAsIDAsIC42KTtcbn1cbi52cy1kYXJrIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50ID4gLnNjcm9sbGJhciA+IC5zbGlkZXIuYWN0aXZlIHtcblx0YmFja2dyb3VuZDogcmdiYSgxOTEsIDE5MSwgMTkxLCAuNCk7XG59XG4uaGMtYmxhY2sgLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuc2Nyb2xsYmFyID4gLnNsaWRlci5hY3RpdmUge1xuXHRiYWNrZ3JvdW5kOiByZ2JhKDExMSwgMTk1LCAyMjMsIDEpO1xufVxuXG4udnMtZGFyayAubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCAuc2hhZG93LnRvcCB7XG5cdGJveC1zaGFkb3c6IG5vbmU7XG59XG5cbi52cy1kYXJrIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50IC5zaGFkb3cubGVmdCB7XG5cdGJveC1zaGFkb3c6ICMwMDAgNnB4IDAgNnB4IC02cHggaW5zZXQ7XG59XG5cbi52cy1kYXJrIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50IC5zaGFkb3cudG9wLmxlZnQge1xuXHRib3gtc2hhZG93OiAjMDAwIDZweCA2cHggNnB4IC02cHggaW5zZXQ7XG59XG5cbi5oYy1ibGFjayAubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCAuc2hhZG93LnRvcCB7XG5cdGJveC1zaGFkb3c6IG5vbmU7XG59XG5cbi5oYy1ibGFjayAubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCAuc2hhZG93LmxlZnQge1xuXHRib3gtc2hhZG93OiBub25lO1xufVxuXG4uaGMtYmxhY2sgLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgLnNoYWRvdy50b3AubGVmdCB7XG5cdGJveC1zaGFkb3c6IG5vbmU7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .on-type-rename-decoration {
	border-left: 1px solid transparent;
	/* So border can be transparent */
	background-clip: padding-box;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvY29udHJpYi9yZW5hbWUvbWVkaWEvb25UeXBlUmVuYW1lLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxrQ0FBa0M7Q0FDbEMsaUNBQWlDO0NBQ2pDLDRCQUE0QjtBQUM3QiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4ubW9uYWNvLWVkaXRvciAub24tdHlwZS1yZW5hbWUtZGVjb3JhdGlvbiB7XG5cdGJvcmRlci1sZWZ0OiAxcHggc29saWQgdHJhbnNwYXJlbnQ7XG5cdC8qIFNvIGJvcmRlciBjYW4gYmUgdHJhbnNwYXJlbnQgKi9cblx0YmFja2dyb3VuZC1jbGlwOiBwYWRkaW5nLWJveDtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


/* Default standalone editor fonts */
.monaco-editor {
	font-family: -apple-system, BlinkMacSystemFont, "Segoe WPC", "Segoe UI", "HelveticaNeue-Light", system-ui, "Ubuntu", "Droid Sans", sans-serif;
	--monaco-monospace-font: "SF Mono", Monaco, Menlo, Consolas, "Ubuntu Mono", "Liberation Mono", "DejaVu Sans Mono", "Courier New", monospace;
}

.monaco-menu .monaco-action-bar.vertical .action-item .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
.monaco-editor.hc-black .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-hover p {
	margin: 0;
}

/* The hc-black theme is already high contrast optimized */
.monaco-editor.hc-black {
	-ms-high-contrast-adjust: none;
}
/* In case the browser goes into high contrast mode and the editor is not configured with the hc-black theme */
@media screen and (-ms-high-contrast:active) {

	/* current line highlight */
	.monaco-editor.vs .view-overlays .current-line,
	.monaco-editor.vs-dark .view-overlays .current-line {
		border-color: windowtext !important;
		border-left: 0;
		border-right: 0;
	}

	/* view cursors */
	.monaco-editor.vs .cursor,
	.monaco-editor.vs-dark .cursor {
		background-color: windowtext !important;
	}
	/* dnd target */
	.monaco-editor.vs .dnd-target,
	.monaco-editor.vs-dark .dnd-target {
		border-color: windowtext !important;
	}

	/* selected text background */
	.monaco-editor.vs .selected-text,
	.monaco-editor.vs-dark .selected-text {
		background-color: highlight !important;
	}

	/* allow the text to have a transparent background. */
	.monaco-editor.vs .view-line,
	.monaco-editor.vs-dark .view-line {
		-ms-high-contrast-adjust: none;
	}

	/* text color */
	.monaco-editor.vs .view-line span,
	.monaco-editor.vs-dark .view-line span {
		color: windowtext !important;
	}
	/* selected text color */
	.monaco-editor.vs .view-line span.inline-selected-text,
	.monaco-editor.vs-dark .view-line span.inline-selected-text {
		color: highlighttext !important;
	}

	/* allow decorations */
	.monaco-editor.vs .view-overlays,
	.monaco-editor.vs-dark .view-overlays {
		-ms-high-contrast-adjust: none;
	}

	/* various decorations */
	.monaco-editor.vs .selectionHighlight,
	.monaco-editor.vs-dark .selectionHighlight,
	.monaco-editor.vs .wordHighlight,
	.monaco-editor.vs-dark .wordHighlight,
	.monaco-editor.vs .wordHighlightStrong,
	.monaco-editor.vs-dark .wordHighlightStrong,
	.monaco-editor.vs .reference-decoration,
	.monaco-editor.vs-dark .reference-decoration {
		border: 2px dotted highlight !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .rangeHighlight,
	.monaco-editor.vs-dark .rangeHighlight {
		background: transparent !important;
		border: 1px dotted activeborder !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .bracket-match,
	.monaco-editor.vs-dark .bracket-match {
		border-color: windowtext !important;
		background: transparent !important;
	}

	/* find widget */
	.monaco-editor.vs .findMatch,
	.monaco-editor.vs-dark .findMatch,
	.monaco-editor.vs .currentFindMatch,
	.monaco-editor.vs-dark .currentFindMatch {
		border: 2px dotted activeborder !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .find-widget,
	.monaco-editor.vs-dark .find-widget {
		border: 1px solid windowtext;
	}

	/* list - used by suggest widget */
	.monaco-editor.vs .monaco-list .monaco-list-row,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row {
		-ms-high-contrast-adjust: none;
		color: windowtext !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row.focused,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row.focused {
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row:hover,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row:hover {
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* scrollbars */
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar {
		-ms-high-contrast-adjust: none;
		background: background !important;
		border: 1px solid windowtext;
		box-sizing: border-box;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
		background: windowtext !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider:hover,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider:hover {
		background: highlight !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider.active,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
		background: highlight !important;
	}

	/* overview ruler */
	.monaco-editor.vs .decorationsOverviewRuler,
	.monaco-editor.vs-dark .decorationsOverviewRuler {
		opacity: 0;
	}

	/* minimap */
	.monaco-editor.vs .minimap,
	.monaco-editor.vs-dark .minimap {
		display: none;
	}

	/* squiggles */
	.monaco-editor.vs .squiggly-d-error,
	.monaco-editor.vs-dark .squiggly-d-error {
		background: transparent !important;
		border-bottom: 4px double #E47777;
	}
	.monaco-editor.vs .squiggly-c-warning,
	.monaco-editor.vs-dark .squiggly-c-warning {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-b-info,
	.monaco-editor.vs-dark .squiggly-b-info {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-a-hint,
	.monaco-editor.vs-dark .squiggly-a-hint {
		border-bottom: 4px double #6c6c6c;
	}

	/* contextmenu */
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
		-ms-high-contrast-adjust: none;
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label {
		-ms-high-contrast-adjust: none;
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* diff editor */
	.monaco-diff-editor.vs .diffOverviewRuler,
	.monaco-diff-editor.vs-dark .diffOverviewRuler {
		display: none;
	}
	.monaco-editor.vs .line-insert,
	.monaco-editor.vs-dark .line-insert,
	.monaco-editor.vs .line-delete,
	.monaco-editor.vs-dark .line-delete {
		background: transparent !important;
		border: 1px solid highlight !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .char-insert,
	.monaco-editor.vs-dark .char-insert,
	.monaco-editor.vs .char-delete,
	.monaco-editor.vs-dark .char-delete {
		background: transparent !important;
	}
}

/*.monaco-editor.vs [tabindex="0"]:focus {
	outline: 1px solid rgba(0, 122, 204, 0.4);
	outline-offset: -1px;
	opacity: 1 !important;
}

.monaco-editor.vs-dark [tabindex="0"]:focus {
	outline: 1px solid rgba(14, 99, 156, 0.6);
	outline-offset: -1px;
	opacity: 1 !important;
}*/

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3Ivc3RhbmRhbG9uZS9icm93c2VyL3N0YW5kYWxvbmUtdG9rZW5zLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7O0FBRy9GLG9DQUFvQztBQUNwQztDQUNDLDZJQUE2STtDQUM3SSwySUFBMkk7QUFDNUk7O0FBRUE7Q0FDQyxtQkFBbUI7QUFDcEI7O0FBRUE7O0NBRUMsbUJBQW1CO0FBQ3BCOztBQUVBO0NBQ0MsU0FBUztBQUNWOztBQUVBLDBEQUEwRDtBQUMxRDtDQUNDLDhCQUE4QjtBQUMvQjtBQUNBLDhHQUE4RztBQUM5Rzs7Q0FFQywyQkFBMkI7Q0FDM0I7O0VBRUMsbUNBQW1DO0VBQ25DLGNBQWM7RUFDZCxlQUFlO0NBQ2hCOztDQUVBLGlCQUFpQjtDQUNqQjs7RUFFQyx1Q0FBdUM7Q0FDeEM7Q0FDQSxlQUFlO0NBQ2Y7O0VBRUMsbUNBQW1DO0NBQ3BDOztDQUVBLDZCQUE2QjtDQUM3Qjs7RUFFQyxzQ0FBc0M7Q0FDdkM7O0NBRUEscURBQXFEO0NBQ3JEOztFQUVDLDhCQUE4QjtDQUMvQjs7Q0FFQSxlQUFlO0NBQ2Y7O0VBRUMsNEJBQTRCO0NBQzdCO0NBQ0Esd0JBQXdCO0NBQ3hCOztFQUVDLCtCQUErQjtDQUNoQzs7Q0FFQSxzQkFBc0I7Q0FDdEI7O0VBRUMsOEJBQThCO0NBQy9COztDQUVBLHdCQUF3QjtDQUN4Qjs7Ozs7Ozs7RUFRQyx1Q0FBdUM7RUFDdkMsa0NBQWtDO0VBQ2xDLHNCQUFzQjtDQUN2QjtDQUNBOztFQUVDLGtDQUFrQztFQUNsQywwQ0FBMEM7RUFDMUMsc0JBQXNCO0NBQ3ZCO0NBQ0E7O0VBRUMsbUNBQW1DO0VBQ25DLGtDQUFrQztDQUNuQzs7Q0FFQSxnQkFBZ0I7Q0FDaEI7Ozs7RUFJQywwQ0FBMEM7RUFDMUMsa0NBQWtDO0VBQ2xDLHNCQUFzQjtDQUN2QjtDQUNBOztFQUVDLDRCQUE0QjtDQUM3Qjs7Q0FFQSxrQ0FBa0M7Q0FDbEM7O0VBRUMsOEJBQThCO0VBQzlCLDRCQUE0QjtDQUM3QjtDQUNBOztFQUVDLCtCQUErQjtFQUMvQixzQ0FBc0M7Q0FDdkM7Q0FDQTs7RUFFQyxrQ0FBa0M7RUFDbEMsMkJBQTJCO0VBQzNCLHNCQUFzQjtDQUN2Qjs7Q0FFQSxlQUFlO0NBQ2Y7O0VBRUMsOEJBQThCO0VBQzlCLGlDQUFpQztFQUNqQyw0QkFBNEI7RUFDNUIsc0JBQXNCO0NBQ3ZCO0NBQ0E7O0VBRUMsaUNBQWlDO0NBQ2xDO0NBQ0E7O0VBRUMsZ0NBQWdDO0NBQ2pDO0NBQ0E7O0VBRUMsZ0NBQWdDO0NBQ2pDOztDQUVBLG1CQUFtQjtDQUNuQjs7RUFFQyxVQUFVO0NBQ1g7O0NBRUEsWUFBWTtDQUNaOztFQUVDLGFBQWE7Q0FDZDs7Q0FFQSxjQUFjO0NBQ2Q7O0VBRUMsa0NBQWtDO0VBQ2xDLGlDQUFpQztDQUNsQztDQUNBOztFQUVDLGlDQUFpQztDQUNsQztDQUNBOztFQUVDLGlDQUFpQztDQUNsQztDQUNBOztFQUVDLGlDQUFpQztDQUNsQzs7Q0FFQSxnQkFBZ0I7Q0FDaEI7O0VBRUMsOEJBQThCO0VBQzlCLCtCQUErQjtFQUMvQixzQ0FBc0M7Q0FDdkM7Q0FDQTs7RUFFQyw4QkFBOEI7RUFDOUIsa0NBQWtDO0VBQ2xDLDJCQUEyQjtFQUMzQixzQkFBc0I7Q0FDdkI7O0NBRUEsZ0JBQWdCO0NBQ2hCOztFQUVDLGFBQWE7Q0FDZDtDQUNBOzs7O0VBSUMsa0NBQWtDO0VBQ2xDLHNDQUFzQztFQUN0QyxzQkFBc0I7Q0FDdkI7Q0FDQTs7OztFQUlDLGtDQUFrQztDQUNuQztBQUNEOztBQUVBOzs7Ozs7Ozs7O0VBVUUiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuXG4vKiBEZWZhdWx0IHN0YW5kYWxvbmUgZWRpdG9yIGZvbnRzICovXG4ubW9uYWNvLWVkaXRvciB7XG5cdGZvbnQtZmFtaWx5OiAtYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFwiU2Vnb2UgV1BDXCIsIFwiU2Vnb2UgVUlcIiwgXCJIZWx2ZXRpY2FOZXVlLUxpZ2h0XCIsIHN5c3RlbS11aSwgXCJVYnVudHVcIiwgXCJEcm9pZCBTYW5zXCIsIHNhbnMtc2VyaWY7XG5cdC0tbW9uYWNvLW1vbm9zcGFjZS1mb250OiBcIlNGIE1vbm9cIiwgTW9uYWNvLCBNZW5sbywgQ29uc29sYXMsIFwiVWJ1bnR1IE1vbm9cIiwgXCJMaWJlcmF0aW9uIE1vbm9cIiwgXCJEZWphVnUgU2FucyBNb25vXCIsIFwiQ291cmllciBOZXdcIiwgbW9ub3NwYWNlO1xufVxuXG4ubW9uYWNvLW1lbnUgLm1vbmFjby1hY3Rpb24tYmFyLnZlcnRpY2FsIC5hY3Rpb24taXRlbSAuYWN0aW9uLW1lbnUtaXRlbTpmb2N1cyAuYWN0aW9uLWxhYmVsIHtcblx0c3Ryb2tlLXdpZHRoOiAxLjJweDtcbn1cblxuLm1vbmFjby1lZGl0b3IudnMtZGFyayAubW9uYWNvLW1lbnUgLm1vbmFjby1hY3Rpb24tYmFyLnZlcnRpY2FsIC5hY3Rpb24tbWVudS1pdGVtOmZvY3VzIC5hY3Rpb24tbGFiZWwsXG4ubW9uYWNvLWVkaXRvci5oYy1ibGFjayAubW9uYWNvLW1lbnUgLm1vbmFjby1hY3Rpb24tYmFyLnZlcnRpY2FsIC5hY3Rpb24tbWVudS1pdGVtOmZvY3VzIC5hY3Rpb24tbGFiZWwge1xuXHRzdHJva2Utd2lkdGg6IDEuMnB4O1xufVxuXG4ubW9uYWNvLWhvdmVyIHAge1xuXHRtYXJnaW46IDA7XG59XG5cbi8qIFRoZSBoYy1ibGFjayB0aGVtZSBpcyBhbHJlYWR5IGhpZ2ggY29udHJhc3Qgb3B0aW1pemVkICovXG4ubW9uYWNvLWVkaXRvci5oYy1ibGFjayB7XG5cdC1tcy1oaWdoLWNvbnRyYXN0LWFkanVzdDogbm9uZTtcbn1cbi8qIEluIGNhc2UgdGhlIGJyb3dzZXIgZ29lcyBpbnRvIGhpZ2ggY29udHJhc3QgbW9kZSBhbmQgdGhlIGVkaXRvciBpcyBub3QgY29uZmlndXJlZCB3aXRoIHRoZSBoYy1ibGFjayB0aGVtZSAqL1xuQG1lZGlhIHNjcmVlbiBhbmQgKC1tcy1oaWdoLWNvbnRyYXN0OmFjdGl2ZSkge1xuXG5cdC8qIGN1cnJlbnQgbGluZSBoaWdobGlnaHQgKi9cblx0Lm1vbmFjby1lZGl0b3IudnMgLnZpZXctb3ZlcmxheXMgLmN1cnJlbnQtbGluZSxcblx0Lm1vbmFjby1lZGl0b3IudnMtZGFyayAudmlldy1vdmVybGF5cyAuY3VycmVudC1saW5lIHtcblx0XHRib3JkZXItY29sb3I6IHdpbmRvd3RleHQgIWltcG9ydGFudDtcblx0XHRib3JkZXItbGVmdDogMDtcblx0XHRib3JkZXItcmlnaHQ6IDA7XG5cdH1cblxuXHQvKiB2aWV3IGN1cnNvcnMgKi9cblx0Lm1vbmFjby1lZGl0b3IudnMgLmN1cnNvcixcblx0Lm1vbmFjby1lZGl0b3IudnMtZGFyayAuY3Vyc29yIHtcblx0XHRiYWNrZ3JvdW5kLWNvbG9yOiB3aW5kb3d0ZXh0ICFpbXBvcnRhbnQ7XG5cdH1cblx0LyogZG5kIHRhcmdldCAqL1xuXHQubW9uYWNvLWVkaXRvci52cyAuZG5kLXRhcmdldCxcblx0Lm1vbmFjby1lZGl0b3IudnMtZGFyayAuZG5kLXRhcmdldCB7XG5cdFx0Ym9yZGVyLWNvbG9yOiB3aW5kb3d0ZXh0ICFpbXBvcnRhbnQ7XG5cdH1cblxuXHQvKiBzZWxlY3RlZCB0ZXh0IGJhY2tncm91bmQgKi9cblx0Lm1vbmFjby1lZGl0b3IudnMgLnNlbGVjdGVkLXRleHQsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnNlbGVjdGVkLXRleHQge1xuXHRcdGJhY2tncm91bmQtY29sb3I6IGhpZ2hsaWdodCAhaW1wb3J0YW50O1xuXHR9XG5cblx0LyogYWxsb3cgdGhlIHRleHQgdG8gaGF2ZSBhIHRyYW5zcGFyZW50IGJhY2tncm91bmQuICovXG5cdC5tb25hY28tZWRpdG9yLnZzIC52aWV3LWxpbmUsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnZpZXctbGluZSB7XG5cdFx0LW1zLWhpZ2gtY29udHJhc3QtYWRqdXN0OiBub25lO1xuXHR9XG5cblx0LyogdGV4dCBjb2xvciAqL1xuXHQubW9uYWNvLWVkaXRvci52cyAudmlldy1saW5lIHNwYW4sXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnZpZXctbGluZSBzcGFuIHtcblx0XHRjb2xvcjogd2luZG93dGV4dCAhaW1wb3J0YW50O1xuXHR9XG5cdC8qIHNlbGVjdGVkIHRleHQgY29sb3IgKi9cblx0Lm1vbmFjby1lZGl0b3IudnMgLnZpZXctbGluZSBzcGFuLmlubGluZS1zZWxlY3RlZC10ZXh0LFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC52aWV3LWxpbmUgc3Bhbi5pbmxpbmUtc2VsZWN0ZWQtdGV4dCB7XG5cdFx0Y29sb3I6IGhpZ2hsaWdodHRleHQgIWltcG9ydGFudDtcblx0fVxuXG5cdC8qIGFsbG93IGRlY29yYXRpb25zICovXG5cdC5tb25hY28tZWRpdG9yLnZzIC52aWV3LW92ZXJsYXlzLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC52aWV3LW92ZXJsYXlzIHtcblx0XHQtbXMtaGlnaC1jb250cmFzdC1hZGp1c3Q6IG5vbmU7XG5cdH1cblxuXHQvKiB2YXJpb3VzIGRlY29yYXRpb25zICovXG5cdC5tb25hY28tZWRpdG9yLnZzIC5zZWxlY3Rpb25IaWdobGlnaHQsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnNlbGVjdGlvbkhpZ2hsaWdodCxcblx0Lm1vbmFjby1lZGl0b3IudnMgLndvcmRIaWdobGlnaHQsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLndvcmRIaWdobGlnaHQsXG5cdC5tb25hY28tZWRpdG9yLnZzIC53b3JkSGlnaGxpZ2h0U3Ryb25nLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC53b3JkSGlnaGxpZ2h0U3Ryb25nLFxuXHQubW9uYWNvLWVkaXRvci52cyAucmVmZXJlbmNlLWRlY29yYXRpb24sXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnJlZmVyZW5jZS1kZWNvcmF0aW9uIHtcblx0XHRib3JkZXI6IDJweCBkb3R0ZWQgaGlnaGxpZ2h0ICFpbXBvcnRhbnQ7XG5cdFx0YmFja2dyb3VuZDogdHJhbnNwYXJlbnQgIWltcG9ydGFudDtcblx0XHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xuXHR9XG5cdC5tb25hY28tZWRpdG9yLnZzIC5yYW5nZUhpZ2hsaWdodCxcblx0Lm1vbmFjby1lZGl0b3IudnMtZGFyayAucmFuZ2VIaWdobGlnaHQge1xuXHRcdGJhY2tncm91bmQ6IHRyYW5zcGFyZW50ICFpbXBvcnRhbnQ7XG5cdFx0Ym9yZGVyOiAxcHggZG90dGVkIGFjdGl2ZWJvcmRlciAhaW1wb3J0YW50O1xuXHRcdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG5cdH1cblx0Lm1vbmFjby1lZGl0b3IudnMgLmJyYWNrZXQtbWF0Y2gsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLmJyYWNrZXQtbWF0Y2gge1xuXHRcdGJvcmRlci1jb2xvcjogd2luZG93dGV4dCAhaW1wb3J0YW50O1xuXHRcdGJhY2tncm91bmQ6IHRyYW5zcGFyZW50ICFpbXBvcnRhbnQ7XG5cdH1cblxuXHQvKiBmaW5kIHdpZGdldCAqL1xuXHQubW9uYWNvLWVkaXRvci52cyAuZmluZE1hdGNoLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5maW5kTWF0Y2gsXG5cdC5tb25hY28tZWRpdG9yLnZzIC5jdXJyZW50RmluZE1hdGNoLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5jdXJyZW50RmluZE1hdGNoIHtcblx0XHRib3JkZXI6IDJweCBkb3R0ZWQgYWN0aXZlYm9yZGVyICFpbXBvcnRhbnQ7XG5cdFx0YmFja2dyb3VuZDogdHJhbnNwYXJlbnQgIWltcG9ydGFudDtcblx0XHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xuXHR9XG5cdC5tb25hY28tZWRpdG9yLnZzIC5maW5kLXdpZGdldCxcblx0Lm1vbmFjby1lZGl0b3IudnMtZGFyayAuZmluZC13aWRnZXQge1xuXHRcdGJvcmRlcjogMXB4IHNvbGlkIHdpbmRvd3RleHQ7XG5cdH1cblxuXHQvKiBsaXN0IC0gdXNlZCBieSBzdWdnZXN0IHdpZGdldCAqL1xuXHQubW9uYWNvLWVkaXRvci52cyAubW9uYWNvLWxpc3QgLm1vbmFjby1saXN0LXJvdyxcblx0Lm1vbmFjby1lZGl0b3IudnMtZGFyayAubW9uYWNvLWxpc3QgLm1vbmFjby1saXN0LXJvdyB7XG5cdFx0LW1zLWhpZ2gtY29udHJhc3QtYWRqdXN0OiBub25lO1xuXHRcdGNvbG9yOiB3aW5kb3d0ZXh0ICFpbXBvcnRhbnQ7XG5cdH1cblx0Lm1vbmFjby1lZGl0b3IudnMgLm1vbmFjby1saXN0IC5tb25hY28tbGlzdC1yb3cuZm9jdXNlZCxcblx0Lm1vbmFjby1lZGl0b3IudnMtZGFyayAubW9uYWNvLWxpc3QgLm1vbmFjby1saXN0LXJvdy5mb2N1c2VkIHtcblx0XHRjb2xvcjogaGlnaGxpZ2h0dGV4dCAhaW1wb3J0YW50O1xuXHRcdGJhY2tncm91bmQtY29sb3I6IGhpZ2hsaWdodCAhaW1wb3J0YW50O1xuXHR9XG5cdC5tb25hY28tZWRpdG9yLnZzIC5tb25hY28tbGlzdCAubW9uYWNvLWxpc3Qtcm93OmhvdmVyLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5tb25hY28tbGlzdCAubW9uYWNvLWxpc3Qtcm93OmhvdmVyIHtcblx0XHRiYWNrZ3JvdW5kOiB0cmFuc3BhcmVudCAhaW1wb3J0YW50O1xuXHRcdGJvcmRlcjogMXB4IHNvbGlkIGhpZ2hsaWdodDtcblx0XHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xuXHR9XG5cblx0Lyogc2Nyb2xsYmFycyAqL1xuXHQubW9uYWNvLWVkaXRvci52cyAubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCA+IC5zY3JvbGxiYXIsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQgPiAuc2Nyb2xsYmFyIHtcblx0XHQtbXMtaGlnaC1jb250cmFzdC1hZGp1c3Q6IG5vbmU7XG5cdFx0YmFja2dyb3VuZDogYmFja2dyb3VuZCAhaW1wb3J0YW50O1xuXHRcdGJvcmRlcjogMXB4IHNvbGlkIHdpbmRvd3RleHQ7XG5cdFx0Ym94LXNpemluZzogYm9yZGVyLWJveDtcblx0fVxuXHQubW9uYWNvLWVkaXRvci52cyAubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCA+IC5zY3JvbGxiYXIgPiAuc2xpZGVyLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50ID4gLnNjcm9sbGJhciA+IC5zbGlkZXIge1xuXHRcdGJhY2tncm91bmQ6IHdpbmRvd3RleHQgIWltcG9ydGFudDtcblx0fVxuXHQubW9uYWNvLWVkaXRvci52cyAubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudCA+IC5zY3JvbGxiYXIgPiAuc2xpZGVyOmhvdmVyLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50ID4gLnNjcm9sbGJhciA+IC5zbGlkZXI6aG92ZXIge1xuXHRcdGJhY2tncm91bmQ6IGhpZ2hsaWdodCAhaW1wb3J0YW50O1xuXHR9XG5cdC5tb25hY28tZWRpdG9yLnZzIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50ID4gLnNjcm9sbGJhciA+IC5zbGlkZXIuYWN0aXZlLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50ID4gLnNjcm9sbGJhciA+IC5zbGlkZXIuYWN0aXZlIHtcblx0XHRiYWNrZ3JvdW5kOiBoaWdobGlnaHQgIWltcG9ydGFudDtcblx0fVxuXG5cdC8qIG92ZXJ2aWV3IHJ1bGVyICovXG5cdC5tb25hY28tZWRpdG9yLnZzIC5kZWNvcmF0aW9uc092ZXJ2aWV3UnVsZXIsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLmRlY29yYXRpb25zT3ZlcnZpZXdSdWxlciB7XG5cdFx0b3BhY2l0eTogMDtcblx0fVxuXG5cdC8qIG1pbmltYXAgKi9cblx0Lm1vbmFjby1lZGl0b3IudnMgLm1pbmltYXAsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLm1pbmltYXAge1xuXHRcdGRpc3BsYXk6IG5vbmU7XG5cdH1cblxuXHQvKiBzcXVpZ2dsZXMgKi9cblx0Lm1vbmFjby1lZGl0b3IudnMgLnNxdWlnZ2x5LWQtZXJyb3IsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnNxdWlnZ2x5LWQtZXJyb3Ige1xuXHRcdGJhY2tncm91bmQ6IHRyYW5zcGFyZW50ICFpbXBvcnRhbnQ7XG5cdFx0Ym9yZGVyLWJvdHRvbTogNHB4IGRvdWJsZSAjRTQ3Nzc3O1xuXHR9XG5cdC5tb25hY28tZWRpdG9yLnZzIC5zcXVpZ2dseS1jLXdhcm5pbmcsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnNxdWlnZ2x5LWMtd2FybmluZyB7XG5cdFx0Ym9yZGVyLWJvdHRvbTogNHB4IGRvdWJsZSAjNzFCNzcxO1xuXHR9XG5cdC5tb25hY28tZWRpdG9yLnZzIC5zcXVpZ2dseS1iLWluZm8sXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnNxdWlnZ2x5LWItaW5mbyB7XG5cdFx0Ym9yZGVyLWJvdHRvbTogNHB4IGRvdWJsZSAjNzFCNzcxO1xuXHR9XG5cdC5tb25hY28tZWRpdG9yLnZzIC5zcXVpZ2dseS1hLWhpbnQsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLnNxdWlnZ2x5LWEtaGludCB7XG5cdFx0Ym9yZGVyLWJvdHRvbTogNHB4IGRvdWJsZSAjNmM2YzZjO1xuXHR9XG5cblx0LyogY29udGV4dG1lbnUgKi9cblx0Lm1vbmFjby1lZGl0b3IudnMgLm1vbmFjby1tZW51IC5tb25hY28tYWN0aW9uLWJhci52ZXJ0aWNhbCAuYWN0aW9uLW1lbnUtaXRlbTpmb2N1cyAuYWN0aW9uLWxhYmVsLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5tb25hY28tbWVudSAubW9uYWNvLWFjdGlvbi1iYXIudmVydGljYWwgLmFjdGlvbi1tZW51LWl0ZW06Zm9jdXMgLmFjdGlvbi1sYWJlbCB7XG5cdFx0LW1zLWhpZ2gtY29udHJhc3QtYWRqdXN0OiBub25lO1xuXHRcdGNvbG9yOiBoaWdobGlnaHR0ZXh0ICFpbXBvcnRhbnQ7XG5cdFx0YmFja2dyb3VuZC1jb2xvcjogaGlnaGxpZ2h0ICFpbXBvcnRhbnQ7XG5cdH1cblx0Lm1vbmFjby1lZGl0b3IudnMgLm1vbmFjby1tZW51IC5tb25hY28tYWN0aW9uLWJhci52ZXJ0aWNhbCAuYWN0aW9uLW1lbnUtaXRlbTpob3ZlciAuYWN0aW9uLWxhYmVsLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5tb25hY28tbWVudSAubW9uYWNvLWFjdGlvbi1iYXIudmVydGljYWwgLmFjdGlvbi1tZW51LWl0ZW06aG92ZXIgLmFjdGlvbi1sYWJlbCB7XG5cdFx0LW1zLWhpZ2gtY29udHJhc3QtYWRqdXN0OiBub25lO1xuXHRcdGJhY2tncm91bmQ6IHRyYW5zcGFyZW50ICFpbXBvcnRhbnQ7XG5cdFx0Ym9yZGVyOiAxcHggc29saWQgaGlnaGxpZ2h0O1xuXHRcdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG5cdH1cblxuXHQvKiBkaWZmIGVkaXRvciAqL1xuXHQubW9uYWNvLWRpZmYtZWRpdG9yLnZzIC5kaWZmT3ZlcnZpZXdSdWxlcixcblx0Lm1vbmFjby1kaWZmLWVkaXRvci52cy1kYXJrIC5kaWZmT3ZlcnZpZXdSdWxlciB7XG5cdFx0ZGlzcGxheTogbm9uZTtcblx0fVxuXHQubW9uYWNvLWVkaXRvci52cyAubGluZS1pbnNlcnQsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLmxpbmUtaW5zZXJ0LFxuXHQubW9uYWNvLWVkaXRvci52cyAubGluZS1kZWxldGUsXG5cdC5tb25hY28tZWRpdG9yLnZzLWRhcmsgLmxpbmUtZGVsZXRlIHtcblx0XHRiYWNrZ3JvdW5kOiB0cmFuc3BhcmVudCAhaW1wb3J0YW50O1xuXHRcdGJvcmRlcjogMXB4IHNvbGlkIGhpZ2hsaWdodCAhaW1wb3J0YW50O1xuXHRcdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG5cdH1cblx0Lm1vbmFjby1lZGl0b3IudnMgLmNoYXItaW5zZXJ0LFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5jaGFyLWluc2VydCxcblx0Lm1vbmFjby1lZGl0b3IudnMgLmNoYXItZGVsZXRlLFxuXHQubW9uYWNvLWVkaXRvci52cy1kYXJrIC5jaGFyLWRlbGV0ZSB7XG5cdFx0YmFja2dyb3VuZDogdHJhbnNwYXJlbnQgIWltcG9ydGFudDtcblx0fVxufVxuXG4vKi5tb25hY28tZWRpdG9yLnZzIFt0YWJpbmRleD1cIjBcIl06Zm9jdXMge1xuXHRvdXRsaW5lOiAxcHggc29saWQgcmdiYSgwLCAxMjIsIDIwNCwgMC40KTtcblx0b3V0bGluZS1vZmZzZXQ6IC0xcHg7XG5cdG9wYWNpdHk6IDEgIWltcG9ydGFudDtcbn1cblxuLm1vbmFjby1lZGl0b3IudnMtZGFyayBbdGFiaW5kZXg9XCIwXCJdOmZvY3VzIHtcblx0b3V0bGluZTogMXB4IHNvbGlkIHJnYmEoMTQsIDk5LCAxNTYsIDAuNik7XG5cdG91dGxpbmUtb2Zmc2V0OiAtMXB4O1xuXHRvcGFjaXR5OiAxICFpbXBvcnRhbnQ7XG59Ki9cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -------------------- IE10 remove auto clear button -------------------- */

::-ms-clear {
	display: none;
}

/* All widgets */
/* I am not a big fan of this rule */
.monaco-editor .editor-widget input {
	color: inherit;
}

/* -------------------- Editor -------------------- */

.monaco-editor {
	position: relative;
	overflow: visible;
	-webkit-text-size-adjust: 100%;
}

/* -------------------- Misc -------------------- */

.monaco-editor .overflow-guard {
	position: relative;
	overflow: hidden;
}

.monaco-editor .view-overlays {
	position: absolute;
	top: 0;
}

/*
.monaco-editor .auto-closed-character {
	opacity: 0.3;
}
*/

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci93aWRnZXQvbWVkaWEvZWRpdG9yLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0YsNEVBQTRFOztBQUU1RTtDQUNDLGFBQWE7QUFDZDs7QUFFQSxnQkFBZ0I7QUFDaEIsb0NBQW9DO0FBQ3BDO0NBQ0MsY0FBYztBQUNmOztBQUVBLHFEQUFxRDs7QUFFckQ7Q0FDQyxrQkFBa0I7Q0FDbEIsaUJBQWlCO0NBQ2pCLDhCQUE4QjtBQUMvQjs7QUFFQSxtREFBbUQ7O0FBRW5EO0NBQ0Msa0JBQWtCO0NBQ2xCLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixNQUFNO0FBQ1A7O0FBRUE7Ozs7Q0FJQyIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4vKiAtLS0tLS0tLS0tLS0tLS0tLS0tLSBJRTEwIHJlbW92ZSBhdXRvIGNsZWFyIGJ1dHRvbiAtLS0tLS0tLS0tLS0tLS0tLS0tLSAqL1xuXG46Oi1tcy1jbGVhciB7XG5cdGRpc3BsYXk6IG5vbmU7XG59XG5cbi8qIEFsbCB3aWRnZXRzICovXG4vKiBJIGFtIG5vdCBhIGJpZyBmYW4gb2YgdGhpcyBydWxlICovXG4ubW9uYWNvLWVkaXRvciAuZWRpdG9yLXdpZGdldCBpbnB1dCB7XG5cdGNvbG9yOiBpbmhlcml0O1xufVxuXG4vKiAtLS0tLS0tLS0tLS0tLS0tLS0tLSBFZGl0b3IgLS0tLS0tLS0tLS0tLS0tLS0tLS0gKi9cblxuLm1vbmFjby1lZGl0b3Ige1xuXHRwb3NpdGlvbjogcmVsYXRpdmU7XG5cdG92ZXJmbG93OiB2aXNpYmxlO1xuXHQtd2Via2l0LXRleHQtc2l6ZS1hZGp1c3Q6IDEwMCU7XG59XG5cbi8qIC0tLS0tLS0tLS0tLS0tLS0tLS0tIE1pc2MgLS0tLS0tLS0tLS0tLS0tLS0tLS0gKi9cblxuLm1vbmFjby1lZGl0b3IgLm92ZXJmbG93LWd1YXJkIHtcblx0cG9zaXRpb246IHJlbGF0aXZlO1xuXHRvdmVyZmxvdzogaGlkZGVuO1xufVxuXG4ubW9uYWNvLWVkaXRvciAudmlldy1vdmVybGF5cyB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0dG9wOiAwO1xufVxuXG4vKlxuLm1vbmFjby1lZGl0b3IgLmF1dG8tY2xvc2VkLWNoYXJhY3RlciB7XG5cdG9wYWNpdHk6IDAuMztcbn1cbiovXG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .inputarea {
	min-width: 0;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	outline: none !important;
	resize: none;
	border: none;
	overflow: hidden;
	color: transparent;
	background-color: transparent;
}
/*.monaco-editor .inputarea {
	position: fixed !important;
	width: 800px !important;
	height: 500px !important;
	top: initial !important;
	left: initial !important;
	bottom: 0 !important;
	right: 0 !important;
	color: black !important;
	background: white !important;
	line-height: 15px !important;
	font-size: 14px !important;
}*/
.monaco-editor .inputarea.ime-input {
	z-index: 10;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci9jb250cm9sbGVyL3RleHRBcmVhSGFuZGxlci5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GO0NBQ0MsWUFBWTtDQUNaLGFBQWE7Q0FDYixTQUFTO0NBQ1QsVUFBVTtDQUNWLGtCQUFrQjtDQUNsQix3QkFBd0I7Q0FDeEIsWUFBWTtDQUNaLFlBQVk7Q0FDWixnQkFBZ0I7Q0FDaEIsa0JBQWtCO0NBQ2xCLDZCQUE2QjtBQUM5QjtBQUNBOzs7Ozs7Ozs7Ozs7RUFZRTtBQUNGO0NBQ0MsV0FBVztBQUNaIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5tb25hY28tZWRpdG9yIC5pbnB1dGFyZWEge1xuXHRtaW4td2lkdGg6IDA7XG5cdG1pbi1oZWlnaHQ6IDA7XG5cdG1hcmdpbjogMDtcblx0cGFkZGluZzogMDtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHRvdXRsaW5lOiBub25lICFpbXBvcnRhbnQ7XG5cdHJlc2l6ZTogbm9uZTtcblx0Ym9yZGVyOiBub25lO1xuXHRvdmVyZmxvdzogaGlkZGVuO1xuXHRjb2xvcjogdHJhbnNwYXJlbnQ7XG5cdGJhY2tncm91bmQtY29sb3I6IHRyYW5zcGFyZW50O1xufVxuLyoubW9uYWNvLWVkaXRvciAuaW5wdXRhcmVhIHtcblx0cG9zaXRpb246IGZpeGVkICFpbXBvcnRhbnQ7XG5cdHdpZHRoOiA4MDBweCAhaW1wb3J0YW50O1xuXHRoZWlnaHQ6IDUwMHB4ICFpbXBvcnRhbnQ7XG5cdHRvcDogaW5pdGlhbCAhaW1wb3J0YW50O1xuXHRsZWZ0OiBpbml0aWFsICFpbXBvcnRhbnQ7XG5cdGJvdHRvbTogMCAhaW1wb3J0YW50O1xuXHRyaWdodDogMCAhaW1wb3J0YW50O1xuXHRjb2xvcjogYmxhY2sgIWltcG9ydGFudDtcblx0YmFja2dyb3VuZDogd2hpdGUgIWltcG9ydGFudDtcblx0bGluZS1oZWlnaHQ6IDE1cHggIWltcG9ydGFudDtcblx0Zm9udC1zaXplOiAxNHB4ICFpbXBvcnRhbnQ7XG59Ki9cbi5tb25hY28tZWRpdG9yIC5pbnB1dGFyZWEuaW1lLWlucHV0IHtcblx0ei1pbmRleDogMTA7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .line-numbers {
	font-variant-numeric: tabular-nums;
	position: absolute;
	text-align: right;
	display: inline-block;
	vertical-align: middle;
	box-sizing: border-box;
	cursor: default;
	height: 100%;
}

.monaco-editor .relative-current-line-number {
	text-align: left;
	display: inline-block;
	width: 100%;
}

.monaco-editor .margin-view-overlays .line-numbers.lh-odd {
	margin-top: 1px;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvbGluZU51bWJlcnMvbGluZU51bWJlcnMuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLGtDQUFrQztDQUNsQyxrQkFBa0I7Q0FDbEIsaUJBQWlCO0NBQ2pCLHFCQUFxQjtDQUNyQixzQkFBc0I7Q0FDdEIsc0JBQXNCO0NBQ3RCLGVBQWU7Q0FDZixZQUFZO0FBQ2I7O0FBRUE7Q0FDQyxnQkFBZ0I7Q0FDaEIscUJBQXFCO0NBQ3JCLFdBQVc7QUFDWjs7QUFFQTtDQUNDLGVBQWU7QUFDaEIiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLm1vbmFjby1lZGl0b3IgLm1hcmdpbi12aWV3LW92ZXJsYXlzIC5saW5lLW51bWJlcnMge1xuXHRmb250LXZhcmlhbnQtbnVtZXJpYzogdGFidWxhci1udW1zO1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdHRleHQtYWxpZ246IHJpZ2h0O1xuXHRkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG5cdHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7XG5cdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG5cdGN1cnNvcjogZGVmYXVsdDtcblx0aGVpZ2h0OiAxMDAlO1xufVxuXG4ubW9uYWNvLWVkaXRvciAucmVsYXRpdmUtY3VycmVudC1saW5lLW51bWJlciB7XG5cdHRleHQtYWxpZ246IGxlZnQ7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0d2lkdGg6IDEwMCU7XG59XG5cbi5tb25hY28tZWRpdG9yIC5tYXJnaW4tdmlldy1vdmVybGF5cyAubGluZS1udW1iZXJzLmxoLW9kZCB7XG5cdG1hcmdpbi10b3A6IDFweDtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-mouse-cursor-text {
	cursor: text;
}

/* The following selector looks a bit funny, but that is needed to cover all the workbench and the editor!! */
.vs-dark .mac .monaco-mouse-cursor-text, .hc-black .mac .monaco-mouse-cursor-text,
.vs-dark.mac .monaco-mouse-cursor-text, .hc-black.mac .monaco-mouse-cursor-text {
	cursor: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAAL0lEQVQoz2NgCD3x//9/BhBYBWdhgFVAiVW4JBFKGIa4AqD0//9D3pt4I4tAdAMAHTQ/j5Zom30AAAAASUVORK5CYII=) 1x, url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAAz0lEQVRIx2NgYGBY/R8I/vx5eelX3n82IJ9FxGf6tksvf/8FiTMQAcAGQMDvSwu09abffY8QYSAScNk45G198eX//yev73/4///701eh//kZSARckrNBRvz//+8+6ZohwCzjGNjdgQxkAg7B9WADeBjIBqtJCbhRA0YNoIkBSNmaPEMoNmA0FkYNoFKhapJ6FGyAH3nauaSmPfwI0v/3OukVi0CIZ+F25KrtYcx/CTIy0e+rC7R1Z4KMICVTQQ14feVXIbR695u14+Ir4gwAAD49E54wc1kWAAAAAElFTkSuQmCC) 2x) 5 8, text;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvbW91c2VDdXJzb3IvbW91c2VDdXJzb3IuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLFlBQVk7QUFDYjs7QUFFQSw2R0FBNkc7QUFDN0c7O0NBRUMsK2tCQUEra0I7QUFDaGxCIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5tb25hY28tbW91c2UtY3Vyc29yLXRleHQge1xuXHRjdXJzb3I6IHRleHQ7XG59XG5cbi8qIFRoZSBmb2xsb3dpbmcgc2VsZWN0b3IgbG9va3MgYSBiaXQgZnVubnksIGJ1dCB0aGF0IGlzIG5lZWRlZCB0byBjb3ZlciBhbGwgdGhlIHdvcmtiZW5jaCBhbmQgdGhlIGVkaXRvciEhICovXG4udnMtZGFyayAubWFjIC5tb25hY28tbW91c2UtY3Vyc29yLXRleHQsIC5oYy1ibGFjayAubWFjIC5tb25hY28tbW91c2UtY3Vyc29yLXRleHQsXG4udnMtZGFyay5tYWMgLm1vbmFjby1tb3VzZS1jdXJzb3ItdGV4dCwgLmhjLWJsYWNrLm1hYyAubW9uYWNvLW1vdXNlLWN1cnNvci10ZXh0IHtcblx0Y3Vyc29yOiAtd2Via2l0LWltYWdlLXNldCh1cmwoZGF0YTppbWFnZS9wbmc7YmFzZTY0LGlWQk9SdzBLR2dvQUFBQU5TVWhFVWdBQUFCQUFBQUFRQ0FRQUFBQzEramZxQUFBQUwwbEVRVlFvejJOZ0NEM3gvLzkvQmhCWUJXZGhnRlZBaVZXNEpCRktHSWE0QXFEMC8vOUQzcHQ0STR0QWRBTUFIVFEvajVab20zMEFBQUFBU1VWT1JLNUNZSUk9KSAxeCwgdXJsKGRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCxpVkJPUncwS0dnb0FBQUFOU1VoRVVnQUFBQ0FBQUFBZ0NBUUFBQURaYzdKL0FBQUF6MGxFUVZSSXgyTmdZR0JZL1I4SS92eDVlZWxYM244MklKOUZ4R2Y2dGtzdmYvOEZpVE1RQWNBR1FNRHZTd3UwOWFiZmZZOFFZU0FTY05rNDVHMTk4ZVgvL3lldjczLzQvLy83MDFlaC8va1pTQVJja3JOQlJ2ei8vKzgrNlpvaHdDempHTmpkZ1F4a0FnN0I5V0FEZUJqSUJxdEpDYmhSQTBZTm9Ja0JTTm1hUEVNb05tQTBGa1lOb0ZLaGFwSjZGR3lBSDNuYXVhU21QZndJMHYvM091a1ZpMENJWitGMjVLcnRZY3gvQ1RJeTBlK3JDN1IxWjRLTUlDVlRRUTE0ZmVWWEliUjY5NXUxNCtJcjRnd0FBRDQ5RTU0d2Mxa1dBQUFBQUVsRlRrU3VRbUNDKSAyeCkgNSA4LCB0ZXh0O1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line.current-line-margin.current-line-margin-both {
	border-right: 0;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvY3VycmVudExpbmVIaWdobGlnaHQvY3VycmVudExpbmVIaWdobGlnaHQuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLGNBQWM7Q0FDZCxrQkFBa0I7Q0FDbEIsT0FBTztDQUNQLE1BQU07Q0FDTixzQkFBc0I7QUFDdkI7O0FBRUE7Q0FDQyxjQUFjO0NBQ2Qsa0JBQWtCO0NBQ2xCLE9BQU87Q0FDUCxNQUFNO0NBQ04sc0JBQXNCO0FBQ3ZCOztBQUVBO0NBQ0MsZUFBZTtBQUNoQiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4ubW9uYWNvLWVkaXRvciAudmlldy1vdmVybGF5cyAuY3VycmVudC1saW5lIHtcblx0ZGlzcGxheTogYmxvY2s7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0bGVmdDogMDtcblx0dG9wOiAwO1xuXHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xufVxuXG4ubW9uYWNvLWVkaXRvciAubWFyZ2luLXZpZXctb3ZlcmxheXMgLmN1cnJlbnQtbGluZSB7XG5cdGRpc3BsYXk6IGJsb2NrO1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdGxlZnQ6IDA7XG5cdHRvcDogMDtcblx0Ym94LXNpemluZzogYm9yZGVyLWJveDtcbn1cblxuLm1vbmFjby1lZGl0b3IgLm1hcmdpbi12aWV3LW92ZXJsYXlzIC5jdXJyZW50LWxpbmUuY3VycmVudC1saW5lLW1hcmdpbi5jdXJyZW50LWxpbmUtbWFyZ2luLWJvdGgge1xuXHRib3JkZXItcmlnaHQ6IDA7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cdr = core decorations rendering (div)
*/
.monaco-editor .lines-content .cdr {
	position: absolute;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvZGVjb3JhdGlvbnMvZGVjb3JhdGlvbnMuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjs7O0NBR0M7QUFDRDtDQUNDLGtCQUFrQjtBQUNuQiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4vKlxuXHRLZWVwaW5nIG5hbWUgc2hvcnQgZm9yIGZhc3RlciBwYXJzaW5nLlxuXHRjZHIgPSBjb3JlIGRlY29yYXRpb25zIHJlbmRlcmluZyAoZGl2KVxuKi9cbi5tb25hY28tZWRpdG9yIC5saW5lcy1jb250ZW50IC5jZHIge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG59Il0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .glyph-margin {
	position: absolute;
	top: 0;
}

/*
	Keeping name short for faster parsing.
	cgmr = core glyph margin rendering (div)
*/
.monaco-editor .margin-view-overlays .cgmr {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvZ2x5cGhNYXJnaW4vZ2x5cGhNYXJnaW4uY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLGtCQUFrQjtDQUNsQixNQUFNO0FBQ1A7O0FBRUE7OztDQUdDO0FBQ0Q7Q0FDQyxrQkFBa0I7Q0FDbEIsYUFBYTtDQUNiLG1CQUFtQjtDQUNuQix1QkFBdUI7QUFDeEIiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLm1vbmFjby1lZGl0b3IgLmdseXBoLW1hcmdpbiB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0dG9wOiAwO1xufVxuXG4vKlxuXHRLZWVwaW5nIG5hbWUgc2hvcnQgZm9yIGZhc3RlciBwYXJzaW5nLlxuXHRjZ21yID0gY29yZSBnbHlwaCBtYXJnaW4gcmVuZGVyaW5nIChkaXYpXG4qL1xuLm1vbmFjby1lZGl0b3IgLm1hcmdpbi12aWV3LW92ZXJsYXlzIC5jZ21yIHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRhbGlnbi1pdGVtczogY2VudGVyO1xuXHRqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cigr = core ident guides rendering (div)
*/
.monaco-editor .lines-content .cigr {
	position: absolute;
}
.monaco-editor .lines-content .cigra {
	position: absolute;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvaW5kZW50R3VpZGVzL2luZGVudEd1aWRlcy5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GOzs7Q0FHQztBQUNEO0NBQ0Msa0JBQWtCO0FBQ25CO0FBQ0E7Q0FDQyxrQkFBa0I7QUFDbkIiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLypcblx0S2VlcGluZyBuYW1lIHNob3J0IGZvciBmYXN0ZXIgcGFyc2luZy5cblx0Y2lnciA9IGNvcmUgaWRlbnQgZ3VpZGVzIHJlbmRlcmluZyAoZGl2KVxuKi9cbi5tb25hY28tZWRpdG9yIC5saW5lcy1jb250ZW50IC5jaWdyIHtcblx0cG9zaXRpb246IGFic29sdXRlO1xufVxuLm1vbmFjby1lZGl0b3IgLmxpbmVzLWNvbnRlbnQgLmNpZ3JhIHtcblx0cG9zaXRpb246IGFic29sdXRlO1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Uncomment to see lines flashing when they're painted */
/*.monaco-editor .view-lines > .view-line {
	background-color: none;
	animation-name: flash-background;
	animation-duration: 800ms;
}
@keyframes flash-background {
	0%   { background-color: lightgreen; }
	100% { background-color: none }
}*/

.monaco-editor.no-user-select .lines-content,
.monaco-editor.no-user-select .view-line,
.monaco-editor.no-user-select .view-lines {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-editor .view-lines {
	white-space: nowrap;
}

.monaco-editor .view-line {
	position: absolute;
	width: 100%;
}

.monaco-editor .mtkz {
	display: inline-block;
}

/* TODO@tokenization bootstrap fix */
/*.monaco-editor .view-line > span > span {
	float: none;
	min-height: inherit;
	margin-left: inherit;
}*/

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvbGluZXMvdmlld0xpbmVzLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0YseURBQXlEO0FBQ3pEOzs7Ozs7OztFQVFFOztBQUVGOzs7Q0FHQyxpQkFBaUI7Q0FDakIseUJBQXlCO0NBQ3pCLHFCQUFxQjtBQUN0Qjs7QUFFQTtDQUNDLG1CQUFtQjtBQUNwQjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixXQUFXO0FBQ1o7O0FBRUE7Q0FDQyxxQkFBcUI7QUFDdEI7O0FBRUEsb0NBQW9DO0FBQ3BDOzs7O0VBSUUiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLyogVW5jb21tZW50IHRvIHNlZSBsaW5lcyBmbGFzaGluZyB3aGVuIHRoZXkncmUgcGFpbnRlZCAqL1xuLyoubW9uYWNvLWVkaXRvciAudmlldy1saW5lcyA+IC52aWV3LWxpbmUge1xuXHRiYWNrZ3JvdW5kLWNvbG9yOiBub25lO1xuXHRhbmltYXRpb24tbmFtZTogZmxhc2gtYmFja2dyb3VuZDtcblx0YW5pbWF0aW9uLWR1cmF0aW9uOiA4MDBtcztcbn1cbkBrZXlmcmFtZXMgZmxhc2gtYmFja2dyb3VuZCB7XG5cdDAlICAgeyBiYWNrZ3JvdW5kLWNvbG9yOiBsaWdodGdyZWVuOyB9XG5cdDEwMCUgeyBiYWNrZ3JvdW5kLWNvbG9yOiBub25lIH1cbn0qL1xuXG4ubW9uYWNvLWVkaXRvci5uby11c2VyLXNlbGVjdCAubGluZXMtY29udGVudCxcbi5tb25hY28tZWRpdG9yLm5vLXVzZXItc2VsZWN0IC52aWV3LWxpbmUsXG4ubW9uYWNvLWVkaXRvci5uby11c2VyLXNlbGVjdCAudmlldy1saW5lcyB7XG5cdHVzZXItc2VsZWN0OiBub25lO1xuXHQtd2Via2l0LXVzZXItc2VsZWN0OiBub25lO1xuXHQtbXMtdXNlci1zZWxlY3Q6IG5vbmU7XG59XG5cbi5tb25hY28tZWRpdG9yIC52aWV3LWxpbmVzIHtcblx0d2hpdGUtc3BhY2U6IG5vd3JhcDtcbn1cblxuLm1vbmFjby1lZGl0b3IgLnZpZXctbGluZSB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0d2lkdGg6IDEwMCU7XG59XG5cbi5tb25hY28tZWRpdG9yIC5tdGt6IHtcblx0ZGlzcGxheTogaW5saW5lLWJsb2NrO1xufVxuXG4vKiBUT0RPQHRva2VuaXphdGlvbiBib290c3RyYXAgZml4ICovXG4vKi5tb25hY28tZWRpdG9yIC52aWV3LWxpbmUgPiBzcGFuID4gc3BhbiB7XG5cdGZsb2F0OiBub25lO1xuXHRtaW4taGVpZ2h0OiBpbmhlcml0O1xuXHRtYXJnaW4tbGVmdDogaW5oZXJpdDtcbn0qL1xuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .lines-decorations {
	position: absolute;
	top: 0;
	background: white;
}

/*
	Keeping name short for faster parsing.
	cldr = core lines decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cldr {
	position: absolute;
	height: 100%;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvbGluZXNEZWNvcmF0aW9ucy9saW5lc0RlY29yYXRpb25zLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjtBQUMvRjtDQUNDLGtCQUFrQjtDQUNsQixNQUFNO0NBQ04saUJBQWlCO0FBQ2xCOztBQUVBOzs7Q0FHQztBQUNEO0NBQ0Msa0JBQWtCO0NBQ2xCLFlBQVk7QUFDYiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuLm1vbmFjby1lZGl0b3IgLmxpbmVzLWRlY29yYXRpb25zIHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHR0b3A6IDA7XG5cdGJhY2tncm91bmQ6IHdoaXRlO1xufVxuXG4vKlxuXHRLZWVwaW5nIG5hbWUgc2hvcnQgZm9yIGZhc3RlciBwYXJzaW5nLlxuXHRjbGRyID0gY29yZSBsaW5lcyBkZWNvcmF0aW9ucyByZW5kZXJpbmcgKGRpdilcbiovXG4ubW9uYWNvLWVkaXRvciAubWFyZ2luLXZpZXctb3ZlcmxheXMgLmNsZHIge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdGhlaWdodDogMTAwJTtcbn0iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cmdr = core margin decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cmdr {
	position: absolute;
	left: 0;
	width: 100%;
	height: 100%;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvbWFyZ2luRGVjb3JhdGlvbnMvbWFyZ2luRGVjb3JhdGlvbnMuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjs7O0NBR0M7QUFDRDtDQUNDLGtCQUFrQjtDQUNsQixPQUFPO0NBQ1AsV0FBVztDQUNYLFlBQVk7QUFDYiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4vKlxuXHRLZWVwaW5nIG5hbWUgc2hvcnQgZm9yIGZhc3RlciBwYXJzaW5nLlxuXHRjbWRyID0gY29yZSBtYXJnaW4gZGVjb3JhdGlvbnMgcmVuZGVyaW5nIChkaXYpXG4qL1xuLm1vbmFjby1lZGl0b3IgLm1hcmdpbi12aWV3LW92ZXJsYXlzIC5jbWRyIHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHRsZWZ0OiAwO1xuXHR3aWR0aDogMTAwJTtcblx0aGVpZ2h0OiAxMDAlO1xufSJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* START cover the case that slider is visible on mouseover */
.monaco-editor .minimap.slider-mouseover .minimap-slider {
	opacity: 0;
	transition: opacity 100ms linear;
}
.monaco-editor .minimap.slider-mouseover:hover .minimap-slider {
	opacity: 1;
}
.monaco-editor .minimap.slider-mouseover .minimap-slider.active {
	opacity: 1;
}
/* END cover the case that slider is visible on mouseover */

.monaco-editor .minimap-shadow-hidden {
	position: absolute;
	width: 0;
}
.monaco-editor .minimap-shadow-visible {
	position: absolute;
	left: -6px;
	width: 6px;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvbWluaW1hcC9taW5pbWFwLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0YsNkRBQTZEO0FBQzdEO0NBQ0MsVUFBVTtDQUNWLGdDQUFnQztBQUNqQztBQUNBO0NBQ0MsVUFBVTtBQUNYO0FBQ0E7Q0FDQyxVQUFVO0FBQ1g7QUFDQSwyREFBMkQ7O0FBRTNEO0NBQ0Msa0JBQWtCO0NBQ2xCLFFBQVE7QUFDVDtBQUNBO0NBQ0Msa0JBQWtCO0NBQ2xCLFVBQVU7Q0FDVixVQUFVO0FBQ1giLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLyogU1RBUlQgY292ZXIgdGhlIGNhc2UgdGhhdCBzbGlkZXIgaXMgdmlzaWJsZSBvbiBtb3VzZW92ZXIgKi9cbi5tb25hY28tZWRpdG9yIC5taW5pbWFwLnNsaWRlci1tb3VzZW92ZXIgLm1pbmltYXAtc2xpZGVyIHtcblx0b3BhY2l0eTogMDtcblx0dHJhbnNpdGlvbjogb3BhY2l0eSAxMDBtcyBsaW5lYXI7XG59XG4ubW9uYWNvLWVkaXRvciAubWluaW1hcC5zbGlkZXItbW91c2VvdmVyOmhvdmVyIC5taW5pbWFwLXNsaWRlciB7XG5cdG9wYWNpdHk6IDE7XG59XG4ubW9uYWNvLWVkaXRvciAubWluaW1hcC5zbGlkZXItbW91c2VvdmVyIC5taW5pbWFwLXNsaWRlci5hY3RpdmUge1xuXHRvcGFjaXR5OiAxO1xufVxuLyogRU5EIGNvdmVyIHRoZSBjYXNlIHRoYXQgc2xpZGVyIGlzIHZpc2libGUgb24gbW91c2VvdmVyICovXG5cbi5tb25hY28tZWRpdG9yIC5taW5pbWFwLXNoYWRvdy1oaWRkZW4ge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdHdpZHRoOiAwO1xufVxuLm1vbmFjby1lZGl0b3IgLm1pbmltYXAtc2hhZG93LXZpc2libGUge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdGxlZnQ6IC02cHg7XG5cdHdpZHRoOiA2cHg7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .overlayWidgets {
	position: absolute;
	top: 0;
	left:0;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvb3ZlcmxheVdpZGdldHMvb3ZlcmxheVdpZGdldHMuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGO0FBQy9GO0NBQ0Msa0JBQWtCO0NBQ2xCLE1BQU07Q0FDTixNQUFNO0FBQ1AiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi5tb25hY28tZWRpdG9yIC5vdmVybGF5V2lkZ2V0cyB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0dG9wOiAwO1xuXHRsZWZ0OjA7XG59Il0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-ruler {
	position: absolute;
	top: 0;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvcnVsZXJzL3J1bGVycy5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GO0NBQ0Msa0JBQWtCO0NBQ2xCLE1BQU07QUFDUCIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4ubW9uYWNvLWVkaXRvciAudmlldy1ydWxlciB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0dG9wOiAwO1xufSJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .scroll-decoration {
	position: absolute;
	top: 0;
	left: 0;
	height: 6px;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvc2Nyb2xsRGVjb3JhdGlvbi9zY3JvbGxEZWNvcmF0aW9uLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxrQkFBa0I7Q0FDbEIsTUFBTTtDQUNOLE9BQU87Q0FDUCxXQUFXO0FBQ1oiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLm1vbmFjby1lZGl0b3IgLnNjcm9sbC1kZWNvcmF0aW9uIHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHR0b3A6IDA7XG5cdGxlZnQ6IDA7XG5cdGhlaWdodDogNnB4O1xufSJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cslr = core selections layer rendering (div)
*/
.monaco-editor .lines-content .cslr {
	position: absolute;
}

.monaco-editor			.top-left-radius		{ border-top-left-radius: 3px; }
.monaco-editor			.bottom-left-radius		{ border-bottom-left-radius: 3px; }
.monaco-editor			.top-right-radius		{ border-top-right-radius: 3px; }
.monaco-editor			.bottom-right-radius	{ border-bottom-right-radius: 3px; }

.monaco-editor.hc-black .top-left-radius		{ border-top-left-radius: 0; }
.monaco-editor.hc-black .bottom-left-radius		{ border-bottom-left-radius: 0; }
.monaco-editor.hc-black .top-right-radius		{ border-top-right-radius: 0; }
.monaco-editor.hc-black .bottom-right-radius	{ border-bottom-right-radius: 0; }

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvc2VsZWN0aW9ucy9zZWxlY3Rpb25zLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7OztDQUdDO0FBQ0Q7Q0FDQyxrQkFBa0I7QUFDbkI7O0FBRUEscUNBQXFDLDJCQUEyQixFQUFFO0FBQ2xFLHdDQUF3Qyw4QkFBOEIsRUFBRTtBQUN4RSxzQ0FBc0MsNEJBQTRCLEVBQUU7QUFDcEUsd0NBQXdDLCtCQUErQixFQUFFOztBQUV6RSw0Q0FBNEMseUJBQXlCLEVBQUU7QUFDdkUsK0NBQStDLDRCQUE0QixFQUFFO0FBQzdFLDZDQUE2QywwQkFBMEIsRUFBRTtBQUN6RSwrQ0FBK0MsNkJBQTZCLEVBQUUiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLypcblx0S2VlcGluZyBuYW1lIHNob3J0IGZvciBmYXN0ZXIgcGFyc2luZy5cblx0Y3NsciA9IGNvcmUgc2VsZWN0aW9ucyBsYXllciByZW5kZXJpbmcgKGRpdilcbiovXG4ubW9uYWNvLWVkaXRvciAubGluZXMtY29udGVudCAuY3NsciB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcbn1cblxuLm1vbmFjby1lZGl0b3JcdFx0XHQudG9wLWxlZnQtcmFkaXVzXHRcdHsgYm9yZGVyLXRvcC1sZWZ0LXJhZGl1czogM3B4OyB9XG4ubW9uYWNvLWVkaXRvclx0XHRcdC5ib3R0b20tbGVmdC1yYWRpdXNcdFx0eyBib3JkZXItYm90dG9tLWxlZnQtcmFkaXVzOiAzcHg7IH1cbi5tb25hY28tZWRpdG9yXHRcdFx0LnRvcC1yaWdodC1yYWRpdXNcdFx0eyBib3JkZXItdG9wLXJpZ2h0LXJhZGl1czogM3B4OyB9XG4ubW9uYWNvLWVkaXRvclx0XHRcdC5ib3R0b20tcmlnaHQtcmFkaXVzXHR7IGJvcmRlci1ib3R0b20tcmlnaHQtcmFkaXVzOiAzcHg7IH1cblxuLm1vbmFjby1lZGl0b3IuaGMtYmxhY2sgLnRvcC1sZWZ0LXJhZGl1c1x0XHR7IGJvcmRlci10b3AtbGVmdC1yYWRpdXM6IDA7IH1cbi5tb25hY28tZWRpdG9yLmhjLWJsYWNrIC5ib3R0b20tbGVmdC1yYWRpdXNcdFx0eyBib3JkZXItYm90dG9tLWxlZnQtcmFkaXVzOiAwOyB9XG4ubW9uYWNvLWVkaXRvci5oYy1ibGFjayAudG9wLXJpZ2h0LXJhZGl1c1x0XHR7IGJvcmRlci10b3AtcmlnaHQtcmFkaXVzOiAwOyB9XG4ubW9uYWNvLWVkaXRvci5oYy1ibGFjayAuYm90dG9tLXJpZ2h0LXJhZGl1c1x0eyBib3JkZXItYm90dG9tLXJpZ2h0LXJhZGl1czogMDsgfVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .cursors-layer {
	position: absolute;
	top: 0;
}

.monaco-editor .cursors-layer > .cursor {
	position: absolute;
	overflow: hidden;
}

/* -- smooth-caret-animation -- */
.monaco-editor .cursors-layer.cursor-smooth-caret-animation > .cursor {
	transition: all 80ms;
}

/* -- block-outline-style -- */
.monaco-editor .cursors-layer.cursor-block-outline-style > .cursor {
	box-sizing: border-box;
	background: transparent !important;
	border-style: solid;
	border-width: 1px;
}

/* -- underline-style -- */
.monaco-editor .cursors-layer.cursor-underline-style > .cursor {
	border-bottom-width: 2px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

/* -- underline-thin-style -- */
.monaco-editor .cursors-layer.cursor-underline-thin-style > .cursor {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

@keyframes monaco-cursor-smooth {
	0%,
	20% {
		opacity: 1;
	}
	60%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-phase {
	0%,
	20% {
		opacity: 1;
	}
	90%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-expand {
	0%,
	20% {
		transform: scaleY(1);
	}
	80%,
	100% {
		transform: scaleY(0);
	}
}

.cursor-smooth {
	animation: monaco-cursor-smooth 0.5s ease-in-out 0s 20 alternate;
}

.cursor-phase {
	animation: monaco-cursor-phase 0.5s ease-in-out 0s 20 alternate;
}

.cursor-expand > .cursor {
	animation: monaco-cursor-expand 0.5s ease-in-out 0s 20 alternate;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci92aWV3UGFydHMvdmlld0N1cnNvcnMvdmlld0N1cnNvcnMuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGO0FBQy9GO0NBQ0Msa0JBQWtCO0NBQ2xCLE1BQU07QUFDUDs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixnQkFBZ0I7QUFDakI7O0FBRUEsaUNBQWlDO0FBQ2pDO0NBQ0Msb0JBQW9CO0FBQ3JCOztBQUVBLDhCQUE4QjtBQUM5QjtDQUNDLHNCQUFzQjtDQUN0QixrQ0FBa0M7Q0FDbEMsbUJBQW1CO0NBQ25CLGlCQUFpQjtBQUNsQjs7QUFFQSwwQkFBMEI7QUFDMUI7Q0FDQyx3QkFBd0I7Q0FDeEIsMEJBQTBCO0NBQzFCLGtDQUFrQztDQUNsQyxzQkFBc0I7QUFDdkI7O0FBRUEsK0JBQStCO0FBQy9CO0NBQ0Msd0JBQXdCO0NBQ3hCLDBCQUEwQjtDQUMxQixrQ0FBa0M7Q0FDbEMsc0JBQXNCO0FBQ3ZCOztBQUVBO0NBQ0M7O0VBRUMsVUFBVTtDQUNYO0NBQ0E7O0VBRUMsVUFBVTtDQUNYO0FBQ0Q7O0FBRUE7Q0FDQzs7RUFFQyxVQUFVO0NBQ1g7Q0FDQTs7RUFFQyxVQUFVO0NBQ1g7QUFDRDs7QUFFQTtDQUNDOztFQUVDLG9CQUFvQjtDQUNyQjtDQUNBOztFQUVDLG9CQUFvQjtDQUNyQjtBQUNEOztBQUVBO0NBQ0MsZ0VBQWdFO0FBQ2pFOztBQUVBO0NBQ0MsK0RBQStEO0FBQ2hFOztBQUVBO0NBQ0MsZ0VBQWdFO0FBQ2pFIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG4ubW9uYWNvLWVkaXRvciAuY3Vyc29ycy1sYXllciB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0dG9wOiAwO1xufVxuXG4ubW9uYWNvLWVkaXRvciAuY3Vyc29ycy1sYXllciA+IC5jdXJzb3Ige1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdG92ZXJmbG93OiBoaWRkZW47XG59XG5cbi8qIC0tIHNtb290aC1jYXJldC1hbmltYXRpb24gLS0gKi9cbi5tb25hY28tZWRpdG9yIC5jdXJzb3JzLWxheWVyLmN1cnNvci1zbW9vdGgtY2FyZXQtYW5pbWF0aW9uID4gLmN1cnNvciB7XG5cdHRyYW5zaXRpb246IGFsbCA4MG1zO1xufVxuXG4vKiAtLSBibG9jay1vdXRsaW5lLXN0eWxlIC0tICovXG4ubW9uYWNvLWVkaXRvciAuY3Vyc29ycy1sYXllci5jdXJzb3ItYmxvY2stb3V0bGluZS1zdHlsZSA+IC5jdXJzb3Ige1xuXHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xuXHRiYWNrZ3JvdW5kOiB0cmFuc3BhcmVudCAhaW1wb3J0YW50O1xuXHRib3JkZXItc3R5bGU6IHNvbGlkO1xuXHRib3JkZXItd2lkdGg6IDFweDtcbn1cblxuLyogLS0gdW5kZXJsaW5lLXN0eWxlIC0tICovXG4ubW9uYWNvLWVkaXRvciAuY3Vyc29ycy1sYXllci5jdXJzb3ItdW5kZXJsaW5lLXN0eWxlID4gLmN1cnNvciB7XG5cdGJvcmRlci1ib3R0b20td2lkdGg6IDJweDtcblx0Ym9yZGVyLWJvdHRvbS1zdHlsZTogc29saWQ7XG5cdGJhY2tncm91bmQ6IHRyYW5zcGFyZW50ICFpbXBvcnRhbnQ7XG5cdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG59XG5cbi8qIC0tIHVuZGVybGluZS10aGluLXN0eWxlIC0tICovXG4ubW9uYWNvLWVkaXRvciAuY3Vyc29ycy1sYXllci5jdXJzb3ItdW5kZXJsaW5lLXRoaW4tc3R5bGUgPiAuY3Vyc29yIHtcblx0Ym9yZGVyLWJvdHRvbS13aWR0aDogMXB4O1xuXHRib3JkZXItYm90dG9tLXN0eWxlOiBzb2xpZDtcblx0YmFja2dyb3VuZDogdHJhbnNwYXJlbnQgIWltcG9ydGFudDtcblx0Ym94LXNpemluZzogYm9yZGVyLWJveDtcbn1cblxuQGtleWZyYW1lcyBtb25hY28tY3Vyc29yLXNtb290aCB7XG5cdDAlLFxuXHQyMCUge1xuXHRcdG9wYWNpdHk6IDE7XG5cdH1cblx0NjAlLFxuXHQxMDAlIHtcblx0XHRvcGFjaXR5OiAwO1xuXHR9XG59XG5cbkBrZXlmcmFtZXMgbW9uYWNvLWN1cnNvci1waGFzZSB7XG5cdDAlLFxuXHQyMCUge1xuXHRcdG9wYWNpdHk6IDE7XG5cdH1cblx0OTAlLFxuXHQxMDAlIHtcblx0XHRvcGFjaXR5OiAwO1xuXHR9XG59XG5cbkBrZXlmcmFtZXMgbW9uYWNvLWN1cnNvci1leHBhbmQge1xuXHQwJSxcblx0MjAlIHtcblx0XHR0cmFuc2Zvcm06IHNjYWxlWSgxKTtcblx0fVxuXHQ4MCUsXG5cdDEwMCUge1xuXHRcdHRyYW5zZm9ybTogc2NhbGVZKDApO1xuXHR9XG59XG5cbi5jdXJzb3Itc21vb3RoIHtcblx0YW5pbWF0aW9uOiBtb25hY28tY3Vyc29yLXNtb290aCAwLjVzIGVhc2UtaW4tb3V0IDBzIDIwIGFsdGVybmF0ZTtcbn1cblxuLmN1cnNvci1waGFzZSB7XG5cdGFuaW1hdGlvbjogbW9uYWNvLWN1cnNvci1waGFzZSAwLjVzIGVhc2UtaW4tb3V0IDBzIDIwIGFsdGVybmF0ZTtcbn1cblxuLmN1cnNvci1leHBhbmQgPiAuY3Vyc29yIHtcblx0YW5pbWF0aW9uOiBtb25hY28tY3Vyc29yLWV4cGFuZCAwLjVzIGVhc2UtaW4tb3V0IDBzIDIwIGFsdGVybmF0ZTtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- DiffEditor ---------- */

.monaco-diff-editor .diffOverview {
	z-index: 9;
}

.monaco-diff-editor .diffOverview .diffViewport {
	z-index: 10;
}

/* colors not externalized: using transparancy on background */
.monaco-diff-editor.vs			.diffOverview { background: rgba(0, 0, 0, 0.03); }
.monaco-diff-editor.vs-dark		.diffOverview { background: rgba(255, 255, 255, 0.01); }

.monaco-scrollable-element.modified-in-monaco-diff-editor.vs		.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.vs-dark	.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.hc-black	.scrollbar { background: none; }

.monaco-scrollable-element.modified-in-monaco-diff-editor .slider {
	z-index: 10;
}
.modified-in-monaco-diff-editor				.slider.active { background: rgba(171, 171, 171, .4); }
.modified-in-monaco-diff-editor.hc-black	.slider.active { background: none; }

/* ---------- Diff ---------- */

.monaco-editor .insert-sign,
.monaco-diff-editor .insert-sign,
.monaco-editor .delete-sign,
.monaco-diff-editor .delete-sign {
	font-size: 11px !important;
	opacity: 0.7 !important;
	display: flex !important;
	align-items: center;
}
.monaco-editor.hc-black .insert-sign,
.monaco-diff-editor.hc-black .insert-sign,
.monaco-editor.hc-black .delete-sign,
.monaco-diff-editor.hc-black .delete-sign {
	opacity: 1;
}

.monaco-editor .inline-deleted-margin-view-zone {
	text-align: right;
}
.monaco-editor .inline-added-margin-view-zone {
	text-align: right;
}

/* ---------- Inline Diff ---------- */

.monaco-editor .view-zones .view-lines .view-line span {
	display: inline-block;
}

.monaco-editor .margin-view-zones .lightbulb-glyph:hover {
	cursor: pointer;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci93aWRnZXQvbWVkaWEvZGlmZkVkaXRvci5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7QUFDL0YscUNBQXFDOztBQUVyQztDQUNDLFVBQVU7QUFDWDs7QUFFQTtDQUNDLFdBQVc7QUFDWjs7QUFFQSw4REFBOEQ7QUFDOUQseUNBQXlDLCtCQUErQixFQUFFO0FBQzFFLDZDQUE2QyxxQ0FBcUMsRUFBRTs7QUFFcEYsMkVBQTJFLHlCQUF5QixFQUFFO0FBQ3RHLCtFQUErRSx5QkFBeUIsRUFBRTtBQUMxRyxnRkFBZ0YsZ0JBQWdCLEVBQUU7O0FBRWxHO0NBQ0MsV0FBVztBQUNaO0FBQ0Esb0RBQW9ELG1DQUFtQyxFQUFFO0FBQ3pGLDBEQUEwRCxnQkFBZ0IsRUFBRTs7QUFFNUUsK0JBQStCOztBQUUvQjs7OztDQUlDLDBCQUEwQjtDQUMxQix1QkFBdUI7Q0FDdkIsd0JBQXdCO0NBQ3hCLG1CQUFtQjtBQUNwQjtBQUNBOzs7O0NBSUMsVUFBVTtBQUNYOztBQUVBO0NBQ0MsaUJBQWlCO0FBQ2xCO0FBQ0E7Q0FDQyxpQkFBaUI7QUFDbEI7O0FBRUEsc0NBQXNDOztBQUV0QztDQUNDLHFCQUFxQjtBQUN0Qjs7QUFFQTtDQUNDLGVBQWU7QUFDaEIiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi8qIC0tLS0tLS0tLS0gRGlmZkVkaXRvciAtLS0tLS0tLS0tICovXG5cbi5tb25hY28tZGlmZi1lZGl0b3IgLmRpZmZPdmVydmlldyB7XG5cdHotaW5kZXg6IDk7XG59XG5cbi5tb25hY28tZGlmZi1lZGl0b3IgLmRpZmZPdmVydmlldyAuZGlmZlZpZXdwb3J0IHtcblx0ei1pbmRleDogMTA7XG59XG5cbi8qIGNvbG9ycyBub3QgZXh0ZXJuYWxpemVkOiB1c2luZyB0cmFuc3BhcmFuY3kgb24gYmFja2dyb3VuZCAqL1xuLm1vbmFjby1kaWZmLWVkaXRvci52c1x0XHRcdC5kaWZmT3ZlcnZpZXcgeyBiYWNrZ3JvdW5kOiByZ2JhKDAsIDAsIDAsIDAuMDMpOyB9XG4ubW9uYWNvLWRpZmYtZWRpdG9yLnZzLWRhcmtcdFx0LmRpZmZPdmVydmlldyB7IGJhY2tncm91bmQ6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4wMSk7IH1cblxuLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQubW9kaWZpZWQtaW4tbW9uYWNvLWRpZmYtZWRpdG9yLnZzXHRcdC5zY3JvbGxiYXIgeyBiYWNrZ3JvdW5kOiByZ2JhKDAsMCwwLDApOyB9XG4ubW9uYWNvLXNjcm9sbGFibGUtZWxlbWVudC5tb2RpZmllZC1pbi1tb25hY28tZGlmZi1lZGl0b3IudnMtZGFya1x0LnNjcm9sbGJhciB7IGJhY2tncm91bmQ6IHJnYmEoMCwwLDAsMCk7IH1cbi5tb25hY28tc2Nyb2xsYWJsZS1lbGVtZW50Lm1vZGlmaWVkLWluLW1vbmFjby1kaWZmLWVkaXRvci5oYy1ibGFja1x0LnNjcm9sbGJhciB7IGJhY2tncm91bmQ6IG5vbmU7IH1cblxuLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQubW9kaWZpZWQtaW4tbW9uYWNvLWRpZmYtZWRpdG9yIC5zbGlkZXIge1xuXHR6LWluZGV4OiAxMDtcbn1cbi5tb2RpZmllZC1pbi1tb25hY28tZGlmZi1lZGl0b3JcdFx0XHRcdC5zbGlkZXIuYWN0aXZlIHsgYmFja2dyb3VuZDogcmdiYSgxNzEsIDE3MSwgMTcxLCAuNCk7IH1cbi5tb2RpZmllZC1pbi1tb25hY28tZGlmZi1lZGl0b3IuaGMtYmxhY2tcdC5zbGlkZXIuYWN0aXZlIHsgYmFja2dyb3VuZDogbm9uZTsgfVxuXG4vKiAtLS0tLS0tLS0tIERpZmYgLS0tLS0tLS0tLSAqL1xuXG4ubW9uYWNvLWVkaXRvciAuaW5zZXJ0LXNpZ24sXG4ubW9uYWNvLWRpZmYtZWRpdG9yIC5pbnNlcnQtc2lnbixcbi5tb25hY28tZWRpdG9yIC5kZWxldGUtc2lnbixcbi5tb25hY28tZGlmZi1lZGl0b3IgLmRlbGV0ZS1zaWduIHtcblx0Zm9udC1zaXplOiAxMXB4ICFpbXBvcnRhbnQ7XG5cdG9wYWNpdHk6IDAuNyAhaW1wb3J0YW50O1xuXHRkaXNwbGF5OiBmbGV4ICFpbXBvcnRhbnQ7XG5cdGFsaWduLWl0ZW1zOiBjZW50ZXI7XG59XG4ubW9uYWNvLWVkaXRvci5oYy1ibGFjayAuaW5zZXJ0LXNpZ24sXG4ubW9uYWNvLWRpZmYtZWRpdG9yLmhjLWJsYWNrIC5pbnNlcnQtc2lnbixcbi5tb25hY28tZWRpdG9yLmhjLWJsYWNrIC5kZWxldGUtc2lnbixcbi5tb25hY28tZGlmZi1lZGl0b3IuaGMtYmxhY2sgLmRlbGV0ZS1zaWduIHtcblx0b3BhY2l0eTogMTtcbn1cblxuLm1vbmFjby1lZGl0b3IgLmlubGluZS1kZWxldGVkLW1hcmdpbi12aWV3LXpvbmUge1xuXHR0ZXh0LWFsaWduOiByaWdodDtcbn1cbi5tb25hY28tZWRpdG9yIC5pbmxpbmUtYWRkZWQtbWFyZ2luLXZpZXctem9uZSB7XG5cdHRleHQtYWxpZ246IHJpZ2h0O1xufVxuXG4vKiAtLS0tLS0tLS0tIElubGluZSBEaWZmIC0tLS0tLS0tLS0gKi9cblxuLm1vbmFjby1lZGl0b3IgLnZpZXctem9uZXMgLnZpZXctbGluZXMgLnZpZXctbGluZSBzcGFuIHtcblx0ZGlzcGxheTogaW5saW5lLWJsb2NrO1xufVxuXG4ubW9uYWNvLWVkaXRvciAubWFyZ2luLXZpZXctem9uZXMgLmxpZ2h0YnVsYi1nbHlwaDpob3ZlciB7XG5cdGN1cnNvcjogcG9pbnRlcjtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-diff-editor .diff-review-line-number {
	text-align: right;
	display: inline-block;
}

.monaco-diff-editor .diff-review {
	position: absolute;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-diff-editor .diff-review-summary {
	padding-left: 10px;
}

.monaco-diff-editor .diff-review-shadow {
	position: absolute;
}

.monaco-diff-editor .diff-review-row {
	white-space: pre;
}

.monaco-diff-editor .diff-review-table {
	display: table;
	min-width: 100%;
}

.monaco-diff-editor .diff-review-row {
	display: table-row;
	width: 100%;
}

.monaco-diff-editor .diff-review-spacer {
	display: inline-block;
	width: 10px;
	vertical-align: middle;
}

.monaco-diff-editor .diff-review-spacer > .codicon {
	font-size: 9px !important;
}

.monaco-diff-editor .diff-review-actions {
	display: inline-block;
	position: absolute;
	right: 10px;
	top: 2px;
}

.monaco-diff-editor .diff-review-actions .action-label {
	width: 16px;
	height: 16px;
	margin: 2px 0;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3IvYnJvd3Nlci93aWRnZXQvbWVkaWEvZGlmZlJldmlldy5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GO0NBQ0MsaUJBQWlCO0NBQ2pCLHFCQUFxQjtBQUN0Qjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixpQkFBaUI7Q0FDakIseUJBQXlCO0NBQ3pCLHFCQUFxQjtBQUN0Qjs7QUFFQTtDQUNDLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGNBQWM7Q0FDZCxlQUFlO0FBQ2hCOztBQUVBO0NBQ0Msa0JBQWtCO0NBQ2xCLFdBQVc7QUFDWjs7QUFFQTtDQUNDLHFCQUFxQjtDQUNyQixXQUFXO0NBQ1gsc0JBQXNCO0FBQ3ZCOztBQUVBO0NBQ0MseUJBQXlCO0FBQzFCOztBQUVBO0NBQ0MscUJBQXFCO0NBQ3JCLGtCQUFrQjtDQUNsQixXQUFXO0NBQ1gsUUFBUTtBQUNUOztBQUVBO0NBQ0MsV0FBVztDQUNYLFlBQVk7Q0FDWixhQUFhO0FBQ2QiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLm1vbmFjby1kaWZmLWVkaXRvciAuZGlmZi1yZXZpZXctbGluZS1udW1iZXIge1xuXHR0ZXh0LWFsaWduOiByaWdodDtcblx0ZGlzcGxheTogaW5saW5lLWJsb2NrO1xufVxuXG4ubW9uYWNvLWRpZmYtZWRpdG9yIC5kaWZmLXJldmlldyB7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0dXNlci1zZWxlY3Q6IG5vbmU7XG5cdC13ZWJraXQtdXNlci1zZWxlY3Q6IG5vbmU7XG5cdC1tcy11c2VyLXNlbGVjdDogbm9uZTtcbn1cblxuLm1vbmFjby1kaWZmLWVkaXRvciAuZGlmZi1yZXZpZXctc3VtbWFyeSB7XG5cdHBhZGRpbmctbGVmdDogMTBweDtcbn1cblxuLm1vbmFjby1kaWZmLWVkaXRvciAuZGlmZi1yZXZpZXctc2hhZG93IHtcblx0cG9zaXRpb246IGFic29sdXRlO1xufVxuXG4ubW9uYWNvLWRpZmYtZWRpdG9yIC5kaWZmLXJldmlldy1yb3cge1xuXHR3aGl0ZS1zcGFjZTogcHJlO1xufVxuXG4ubW9uYWNvLWRpZmYtZWRpdG9yIC5kaWZmLXJldmlldy10YWJsZSB7XG5cdGRpc3BsYXk6IHRhYmxlO1xuXHRtaW4td2lkdGg6IDEwMCU7XG59XG5cbi5tb25hY28tZGlmZi1lZGl0b3IgLmRpZmYtcmV2aWV3LXJvdyB7XG5cdGRpc3BsYXk6IHRhYmxlLXJvdztcblx0d2lkdGg6IDEwMCU7XG59XG5cbi5tb25hY28tZGlmZi1lZGl0b3IgLmRpZmYtcmV2aWV3LXNwYWNlciB7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0d2lkdGg6IDEwcHg7XG5cdHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7XG59XG5cbi5tb25hY28tZGlmZi1lZGl0b3IgLmRpZmYtcmV2aWV3LXNwYWNlciA+IC5jb2RpY29uIHtcblx0Zm9udC1zaXplOiA5cHggIWltcG9ydGFudDtcbn1cblxuLm1vbmFjby1kaWZmLWVkaXRvciAuZGlmZi1yZXZpZXctYWN0aW9ucyB7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHRyaWdodDogMTBweDtcblx0dG9wOiAycHg7XG59XG5cbi5tb25hY28tZGlmZi1lZGl0b3IgLmRpZmYtcmV2aWV3LWFjdGlvbnMgLmFjdGlvbi1sYWJlbCB7XG5cdHdpZHRoOiAxNnB4O1xuXHRoZWlnaHQ6IDE2cHg7XG5cdG1hcmdpbjogMnB4IDA7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

@font-face {
	font-family: "codicon";
	src: url(assets/fonts/codicon.b3726f.ttf) format("truetype");
}

.codicon[class*='codicon-'] {
	font: normal normal normal 16px/1 codicon;
	display: inline-block;
	text-decoration: none;
	text-rendering: auto;
	text-align: center;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

/* icon rules are dynamically created in codiconStyles */

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvY29kaWNvbnMvY29kaWNvbi9jb2RpY29uLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxzQkFBc0I7Q0FDdEIsK0RBQTBDO0FBQzNDOztBQUVBO0NBQ0MseUNBQXlDO0NBQ3pDLHFCQUFxQjtDQUNyQixxQkFBcUI7Q0FDckIsb0JBQW9CO0NBQ3BCLGtCQUFrQjtDQUNsQixtQ0FBbUM7Q0FDbkMsa0NBQWtDO0NBQ2xDLGlCQUFpQjtDQUNqQix5QkFBeUI7Q0FDekIscUJBQXFCO0FBQ3RCOztBQUVBLHdEQUF3RCIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG5AZm9udC1mYWNlIHtcblx0Zm9udC1mYW1pbHk6IFwiY29kaWNvblwiO1xuXHRzcmM6IHVybCguL2NvZGljb24udHRmKSBmb3JtYXQoXCJ0cnVldHlwZVwiKTtcbn1cblxuLmNvZGljb25bY2xhc3MqPSdjb2RpY29uLSddIHtcblx0Zm9udDogbm9ybWFsIG5vcm1hbCBub3JtYWwgMTZweC8xIGNvZGljb247XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0dGV4dC1kZWNvcmF0aW9uOiBub25lO1xuXHR0ZXh0LXJlbmRlcmluZzogYXV0bztcblx0dGV4dC1hbGlnbjogY2VudGVyO1xuXHQtd2Via2l0LWZvbnQtc21vb3RoaW5nOiBhbnRpYWxpYXNlZDtcblx0LW1vei1vc3gtZm9udC1zbW9vdGhpbmc6IGdyYXlzY2FsZTtcblx0dXNlci1zZWxlY3Q6IG5vbmU7XG5cdC13ZWJraXQtdXNlci1zZWxlY3Q6IG5vbmU7XG5cdC1tcy11c2VyLXNlbGVjdDogbm9uZTtcbn1cblxuLyogaWNvbiBydWxlcyBhcmUgZHluYW1pY2FsbHkgY3JlYXRlZCBpbiBjb2RpY29uU3R5bGVzICovXG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.codicon-wrench-subaction {
	opacity: 0.5;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvY29kaWNvbnMvY29kaWNvbi9jb2RpY29uLW1vZGlmaWNhdGlvbnMuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLFlBQVk7QUFDYiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4uY29kaWNvbi13cmVuY2gtc3ViYWN0aW9uIHtcblx0b3BhY2l0eTogMC41O1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

@keyframes codicon-spin {
	100% {
		transform:rotate(360deg);
	}
}

.codicon-animation-spin {
	/* Use steps to throttle FPS to reduce CPU usage */
	animation: codicon-spin 1.5s steps(30) infinite;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvY29kaWNvbnMvY29kaWNvbi9jb2RpY29uLWFuaW1hdGlvbnMuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDO0VBQ0Msd0JBQXdCO0NBQ3pCO0FBQ0Q7O0FBRUE7Q0FDQyxrREFBa0Q7Q0FDbEQsK0NBQStDO0FBQ2hEIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbkBrZXlmcmFtZXMgY29kaWNvbi1zcGluIHtcblx0MTAwJSB7XG5cdFx0dHJhbnNmb3JtOnJvdGF0ZSgzNjBkZWcpO1xuXHR9XG59XG5cbi5jb2RpY29uLWFuaW1hdGlvbi1zcGluIHtcblx0LyogVXNlIHN0ZXBzIHRvIHRocm90dGxlIEZQUyB0byByZWR1Y2UgQ1BVIHVzYWdlICovXG5cdGFuaW1hdGlvbjogY29kaWNvbi1zcGluIDEuNXMgc3RlcHMoMzApIGluZmluaXRlO1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view .monaco-menu {
	min-width: 130px;
}


/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9wbGF0Zm9ybS9jb250ZXh0dmlldy9icm93c2VyL2NvbnRleHRNZW51SGFuZGxlci5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GO0NBQ0MsZ0JBQWdCO0FBQ2pCIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5jb250ZXh0LXZpZXcgLm1vbmFjby1tZW51IHtcblx0bWluLXdpZHRoOiAxMzBweDtcbn1cblxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view {
	position: absolute;
	z-index: 2500;
}

.context-view.fixed {
	all: initial;
	font-family: inherit;
	font-size: 13px;
	position: fixed;
	z-index: 2500;
	color: inherit;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvY29udGV4dHZpZXcvY29udGV4dHZpZXcuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLGtCQUFrQjtDQUNsQixhQUFhO0FBQ2Q7O0FBRUE7Q0FDQyxZQUFZO0NBQ1osb0JBQW9CO0NBQ3BCLGVBQWU7Q0FDZixlQUFlO0NBQ2YsYUFBYTtDQUNiLGNBQWM7QUFDZiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4uY29udGV4dC12aWV3IHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHR6LWluZGV4OiAyNTAwO1xufVxuXG4uY29udGV4dC12aWV3LmZpeGVkIHtcblx0YWxsOiBpbml0aWFsO1xuXHRmb250LWZhbWlseTogaW5oZXJpdDtcblx0Zm9udC1zaXplOiAxM3B4O1xuXHRwb3NpdGlvbjogZml4ZWQ7XG5cdHotaW5kZXg6IDI1MDA7XG5cdGNvbG9yOiBpbmhlcml0O1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-list {
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
}

.monaco-list.mouse-support {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-list > .monaco-scrollable-element {
	height: 100%;
}

.monaco-list-rows {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-list.horizontal-scrolling .monaco-list-rows {
	width: auto;
	min-width: 100%;
}

.monaco-list-row {
	position: absolute;
	box-sizing:	border-box;
	overflow: hidden;
	width: 100%;
}

.monaco-list.mouse-support .monaco-list-row {
	cursor: pointer;
	touch-action: none;
}

/* for OS X ballistic scrolling */
.monaco-list-row.scrolling {
	display: none !important;
}

/* Focus */
.monaco-list.element-focused, .monaco-list.selection-single, .monaco-list.selection-multiple {
	outline: 0 !important;
}

.monaco-list:focus .monaco-list-row.selected .codicon {
	color: inherit;
}

/* Dnd */
.monaco-drag-image {
	display: inline-block;
	padding: 1px 7px;
	border-radius: 10px;
	font-size: 12px;
	position: absolute;
}

/* Type filter */

.monaco-list-type-filter {
	display: flex;
	align-items: center;
	position: absolute;
	border-radius: 2px;
	padding: 0px 3px;
	max-width: calc(100% - 10px);
	text-overflow: ellipsis;
	overflow: hidden;
	text-align: right;
	box-sizing: border-box;
	cursor: all-scroll;
	font-size: 13px;
	line-height: 18px;
	height: 20px;
	z-index: 1;
	top: 4px;
}

.monaco-list-type-filter.dragging {
	transition: top 0.2s, left 0.2s;
}

.monaco-list-type-filter.ne {
	right: 4px;
}

.monaco-list-type-filter.nw {
	left: 4px;
}

.monaco-list-type-filter > .controls {
	display: flex;
	align-items: center;
	box-sizing: border-box;
	transition: width 0.2s;
	width: 0;
}

.monaco-list-type-filter.dragging > .controls,
.monaco-list-type-filter:hover > .controls {
	width: 36px;
}

.monaco-list-type-filter > .controls > * {
	border: none;
	box-sizing: border-box;
	-webkit-appearance: none;
	-moz-appearance: none;
	background: none;
	width: 16px;
	height: 16px;
	flex-shrink: 0;
	margin: 0;
	padding: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	cursor: pointer;
}

.monaco-list-type-filter > .controls > .filter {
	margin-left: 4px;
}

.monaco-list-type-filter-message {
	position: absolute;
	box-sizing: border-box;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	padding: 40px 1em 1em 1em;
	text-align: center;
	white-space: normal;
	opacity: 0.7;
	pointer-events: none;
}

.monaco-list-type-filter-message:empty {
	display: none;
}

/* Electron */

.monaco-list-type-filter {
	cursor: grab;
}

.monaco-list-type-filter.dragging {
	cursor: grabbing;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvbGlzdC9saXN0LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxrQkFBa0I7Q0FDbEIsWUFBWTtDQUNaLFdBQVc7Q0FDWCxtQkFBbUI7QUFDcEI7O0FBRUE7Q0FDQyxpQkFBaUI7Q0FDakIseUJBQXlCO0NBQ3pCLHFCQUFxQjtBQUN0Qjs7QUFFQTtDQUNDLFlBQVk7QUFDYjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixXQUFXO0NBQ1gsWUFBWTtBQUNiOztBQUVBO0NBQ0MsV0FBVztDQUNYLGVBQWU7QUFDaEI7O0FBRUE7Q0FDQyxrQkFBa0I7Q0FDbEIsc0JBQXNCO0NBQ3RCLGdCQUFnQjtDQUNoQixXQUFXO0FBQ1o7O0FBRUE7Q0FDQyxlQUFlO0NBQ2Ysa0JBQWtCO0FBQ25COztBQUVBLGlDQUFpQztBQUNqQztDQUNDLHdCQUF3QjtBQUN6Qjs7QUFFQSxVQUFVO0FBQ1Y7Q0FDQyxxQkFBcUI7QUFDdEI7O0FBRUE7Q0FDQyxjQUFjO0FBQ2Y7O0FBRUEsUUFBUTtBQUNSO0NBQ0MscUJBQXFCO0NBQ3JCLGdCQUFnQjtDQUNoQixtQkFBbUI7Q0FDbkIsZUFBZTtDQUNmLGtCQUFrQjtBQUNuQjs7QUFFQSxnQkFBZ0I7O0FBRWhCO0NBQ0MsYUFBYTtDQUNiLG1CQUFtQjtDQUNuQixrQkFBa0I7Q0FDbEIsa0JBQWtCO0NBQ2xCLGdCQUFnQjtDQUNoQiw0QkFBNEI7Q0FDNUIsdUJBQXVCO0NBQ3ZCLGdCQUFnQjtDQUNoQixpQkFBaUI7Q0FDakIsc0JBQXNCO0NBQ3RCLGtCQUFrQjtDQUNsQixlQUFlO0NBQ2YsaUJBQWlCO0NBQ2pCLFlBQVk7Q0FDWixVQUFVO0NBQ1YsUUFBUTtBQUNUOztBQUVBO0NBQ0MsK0JBQStCO0FBQ2hDOztBQUVBO0NBQ0MsVUFBVTtBQUNYOztBQUVBO0NBQ0MsU0FBUztBQUNWOztBQUVBO0NBQ0MsYUFBYTtDQUNiLG1CQUFtQjtDQUNuQixzQkFBc0I7Q0FDdEIsc0JBQXNCO0NBQ3RCLFFBQVE7QUFDVDs7QUFFQTs7Q0FFQyxXQUFXO0FBQ1o7O0FBRUE7Q0FDQyxZQUFZO0NBQ1osc0JBQXNCO0NBQ3RCLHdCQUF3QjtDQUN4QixxQkFBcUI7Q0FDckIsZ0JBQWdCO0NBQ2hCLFdBQVc7Q0FDWCxZQUFZO0NBQ1osY0FBYztDQUNkLFNBQVM7Q0FDVCxVQUFVO0NBQ1YsYUFBYTtDQUNiLG1CQUFtQjtDQUNuQix1QkFBdUI7Q0FDdkIsZUFBZTtBQUNoQjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixzQkFBc0I7Q0FDdEIsV0FBVztDQUNYLFlBQVk7Q0FDWixNQUFNO0NBQ04sT0FBTztDQUNQLHlCQUF5QjtDQUN6QixrQkFBa0I7Q0FDbEIsbUJBQW1CO0NBQ25CLFlBQVk7Q0FDWixvQkFBb0I7QUFDckI7O0FBRUE7Q0FDQyxhQUFhO0FBQ2Q7O0FBRUEsYUFBYTs7QUFFYjtDQUNDLFlBQVk7QUFDYjs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4ubW9uYWNvLWxpc3Qge1xuXHRwb3NpdGlvbjogcmVsYXRpdmU7XG5cdGhlaWdodDogMTAwJTtcblx0d2lkdGg6IDEwMCU7XG5cdHdoaXRlLXNwYWNlOiBub3dyYXA7XG59XG5cbi5tb25hY28tbGlzdC5tb3VzZS1zdXBwb3J0IHtcblx0dXNlci1zZWxlY3Q6IG5vbmU7XG5cdC13ZWJraXQtdXNlci1zZWxlY3Q6IG5vbmU7XG5cdC1tcy11c2VyLXNlbGVjdDogbm9uZTtcbn1cblxuLm1vbmFjby1saXN0ID4gLm1vbmFjby1zY3JvbGxhYmxlLWVsZW1lbnQge1xuXHRoZWlnaHQ6IDEwMCU7XG59XG5cbi5tb25hY28tbGlzdC1yb3dzIHtcblx0cG9zaXRpb246IHJlbGF0aXZlO1xuXHR3aWR0aDogMTAwJTtcblx0aGVpZ2h0OiAxMDAlO1xufVxuXG4ubW9uYWNvLWxpc3QuaG9yaXpvbnRhbC1zY3JvbGxpbmcgLm1vbmFjby1saXN0LXJvd3Mge1xuXHR3aWR0aDogYXV0bztcblx0bWluLXdpZHRoOiAxMDAlO1xufVxuXG4ubW9uYWNvLWxpc3Qtcm93IHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHRib3gtc2l6aW5nOlx0Ym9yZGVyLWJveDtcblx0b3ZlcmZsb3c6IGhpZGRlbjtcblx0d2lkdGg6IDEwMCU7XG59XG5cbi5tb25hY28tbGlzdC5tb3VzZS1zdXBwb3J0IC5tb25hY28tbGlzdC1yb3cge1xuXHRjdXJzb3I6IHBvaW50ZXI7XG5cdHRvdWNoLWFjdGlvbjogbm9uZTtcbn1cblxuLyogZm9yIE9TIFggYmFsbGlzdGljIHNjcm9sbGluZyAqL1xuLm1vbmFjby1saXN0LXJvdy5zY3JvbGxpbmcge1xuXHRkaXNwbGF5OiBub25lICFpbXBvcnRhbnQ7XG59XG5cbi8qIEZvY3VzICovXG4ubW9uYWNvLWxpc3QuZWxlbWVudC1mb2N1c2VkLCAubW9uYWNvLWxpc3Quc2VsZWN0aW9uLXNpbmdsZSwgLm1vbmFjby1saXN0LnNlbGVjdGlvbi1tdWx0aXBsZSB7XG5cdG91dGxpbmU6IDAgIWltcG9ydGFudDtcbn1cblxuLm1vbmFjby1saXN0OmZvY3VzIC5tb25hY28tbGlzdC1yb3cuc2VsZWN0ZWQgLmNvZGljb24ge1xuXHRjb2xvcjogaW5oZXJpdDtcbn1cblxuLyogRG5kICovXG4ubW9uYWNvLWRyYWctaW1hZ2Uge1xuXHRkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG5cdHBhZGRpbmc6IDFweCA3cHg7XG5cdGJvcmRlci1yYWRpdXM6IDEwcHg7XG5cdGZvbnQtc2l6ZTogMTJweDtcblx0cG9zaXRpb246IGFic29sdXRlO1xufVxuXG4vKiBUeXBlIGZpbHRlciAqL1xuXG4ubW9uYWNvLWxpc3QtdHlwZS1maWx0ZXIge1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRhbGlnbi1pdGVtczogY2VudGVyO1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdGJvcmRlci1yYWRpdXM6IDJweDtcblx0cGFkZGluZzogMHB4IDNweDtcblx0bWF4LXdpZHRoOiBjYWxjKDEwMCUgLSAxMHB4KTtcblx0dGV4dC1vdmVyZmxvdzogZWxsaXBzaXM7XG5cdG92ZXJmbG93OiBoaWRkZW47XG5cdHRleHQtYWxpZ246IHJpZ2h0O1xuXHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xuXHRjdXJzb3I6IGFsbC1zY3JvbGw7XG5cdGZvbnQtc2l6ZTogMTNweDtcblx0bGluZS1oZWlnaHQ6IDE4cHg7XG5cdGhlaWdodDogMjBweDtcblx0ei1pbmRleDogMTtcblx0dG9wOiA0cHg7XG59XG5cbi5tb25hY28tbGlzdC10eXBlLWZpbHRlci5kcmFnZ2luZyB7XG5cdHRyYW5zaXRpb246IHRvcCAwLjJzLCBsZWZ0IDAuMnM7XG59XG5cbi5tb25hY28tbGlzdC10eXBlLWZpbHRlci5uZSB7XG5cdHJpZ2h0OiA0cHg7XG59XG5cbi5tb25hY28tbGlzdC10eXBlLWZpbHRlci5udyB7XG5cdGxlZnQ6IDRweDtcbn1cblxuLm1vbmFjby1saXN0LXR5cGUtZmlsdGVyID4gLmNvbnRyb2xzIHtcblx0ZGlzcGxheTogZmxleDtcblx0YWxpZ24taXRlbXM6IGNlbnRlcjtcblx0Ym94LXNpemluZzogYm9yZGVyLWJveDtcblx0dHJhbnNpdGlvbjogd2lkdGggMC4ycztcblx0d2lkdGg6IDA7XG59XG5cbi5tb25hY28tbGlzdC10eXBlLWZpbHRlci5kcmFnZ2luZyA+IC5jb250cm9scyxcbi5tb25hY28tbGlzdC10eXBlLWZpbHRlcjpob3ZlciA+IC5jb250cm9scyB7XG5cdHdpZHRoOiAzNnB4O1xufVxuXG4ubW9uYWNvLWxpc3QtdHlwZS1maWx0ZXIgPiAuY29udHJvbHMgPiAqIHtcblx0Ym9yZGVyOiBub25lO1xuXHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xuXHQtd2Via2l0LWFwcGVhcmFuY2U6IG5vbmU7XG5cdC1tb3otYXBwZWFyYW5jZTogbm9uZTtcblx0YmFja2dyb3VuZDogbm9uZTtcblx0d2lkdGg6IDE2cHg7XG5cdGhlaWdodDogMTZweDtcblx0ZmxleC1zaHJpbms6IDA7XG5cdG1hcmdpbjogMDtcblx0cGFkZGluZzogMDtcblx0ZGlzcGxheTogZmxleDtcblx0YWxpZ24taXRlbXM6IGNlbnRlcjtcblx0anVzdGlmeS1jb250ZW50OiBjZW50ZXI7XG5cdGN1cnNvcjogcG9pbnRlcjtcbn1cblxuLm1vbmFjby1saXN0LXR5cGUtZmlsdGVyID4gLmNvbnRyb2xzID4gLmZpbHRlciB7XG5cdG1hcmdpbi1sZWZ0OiA0cHg7XG59XG5cbi5tb25hY28tbGlzdC10eXBlLWZpbHRlci1tZXNzYWdlIHtcblx0cG9zaXRpb246IGFic29sdXRlO1xuXHRib3gtc2l6aW5nOiBib3JkZXItYm94O1xuXHR3aWR0aDogMTAwJTtcblx0aGVpZ2h0OiAxMDAlO1xuXHR0b3A6IDA7XG5cdGxlZnQ6IDA7XG5cdHBhZGRpbmc6IDQwcHggMWVtIDFlbSAxZW07XG5cdHRleHQtYWxpZ246IGNlbnRlcjtcblx0d2hpdGUtc3BhY2U6IG5vcm1hbDtcblx0b3BhY2l0eTogMC43O1xuXHRwb2ludGVyLWV2ZW50czogbm9uZTtcbn1cblxuLm1vbmFjby1saXN0LXR5cGUtZmlsdGVyLW1lc3NhZ2U6ZW1wdHkge1xuXHRkaXNwbGF5OiBub25lO1xufVxuXG4vKiBFbGVjdHJvbiAqL1xuXG4ubW9uYWNvLWxpc3QtdHlwZS1maWx0ZXIge1xuXHRjdXJzb3I6IGdyYWI7XG59XG5cbi5tb25hY28tbGlzdC10eXBlLWZpbHRlci5kcmFnZ2luZyB7XG5cdGN1cnNvcjogZ3JhYmJpbmc7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-tl-row {
	display: flex;
	height: 100%;
	align-items: center;
	position: relative;
}

.monaco-tl-indent {
	height: 100%;
	position: absolute;
	top: 0;
	left: 16px;
	pointer-events: none;
}

.hide-arrows .monaco-tl-indent {
	left: 12px;
}

.monaco-tl-indent > .indent-guide {
	display: inline-block;
	box-sizing: border-box;
	height: 100%;
	border-left: 1px solid transparent;
}

.monaco-tl-indent > .indent-guide {
	transition: border-color 0.1s linear;
}

.monaco-tl-twistie,
.monaco-tl-contents {
	height: 100%;
}

.monaco-tl-twistie {
	font-size: 10px;
	text-align: right;
	padding-right: 6px;
	flex-shrink: 0;
	width: 16px;
	display: flex !important;
	align-items: center;
	justify-content: center;
	color: inherit !important;
	transform: translateX(3px);
}

.monaco-tl-contents {
	flex: 1;
	overflow: hidden;
}

.monaco-tl-twistie.collapsed::before {
	transform: rotate(-90deg);
}

.monaco-tl-twistie.codicon-tree-item-loading::before {
	/* Use steps to throttle FPS to reduce CPU usage */
	animation: codicon-spin 1.25s steps(30) infinite;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvdHJlZS9tZWRpYS90cmVlLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxhQUFhO0NBQ2IsWUFBWTtDQUNaLG1CQUFtQjtDQUNuQixrQkFBa0I7QUFDbkI7O0FBRUE7Q0FDQyxZQUFZO0NBQ1osa0JBQWtCO0NBQ2xCLE1BQU07Q0FDTixVQUFVO0NBQ1Ysb0JBQW9CO0FBQ3JCOztBQUVBO0NBQ0MsVUFBVTtBQUNYOztBQUVBO0NBQ0MscUJBQXFCO0NBQ3JCLHNCQUFzQjtDQUN0QixZQUFZO0NBQ1osa0NBQWtDO0FBQ25DOztBQUVBO0NBQ0Msb0NBQW9DO0FBQ3JDOztBQUVBOztDQUVDLFlBQVk7QUFDYjs7QUFFQTtDQUNDLGVBQWU7Q0FDZixpQkFBaUI7Q0FDakIsa0JBQWtCO0NBQ2xCLGNBQWM7Q0FDZCxXQUFXO0NBQ1gsd0JBQXdCO0NBQ3hCLG1CQUFtQjtDQUNuQix1QkFBdUI7Q0FDdkIseUJBQXlCO0NBQ3pCLDBCQUEwQjtBQUMzQjs7QUFFQTtDQUNDLE9BQU87Q0FDUCxnQkFBZ0I7QUFDakI7O0FBRUE7Q0FDQyx5QkFBeUI7QUFDMUI7O0FBRUE7Q0FDQyxrREFBa0Q7Q0FDbEQsZ0RBQWdEO0FBQ2pEIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5tb25hY28tdGwtcm93IHtcblx0ZGlzcGxheTogZmxleDtcblx0aGVpZ2h0OiAxMDAlO1xuXHRhbGlnbi1pdGVtczogY2VudGVyO1xuXHRwb3NpdGlvbjogcmVsYXRpdmU7XG59XG5cbi5tb25hY28tdGwtaW5kZW50IHtcblx0aGVpZ2h0OiAxMDAlO1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdHRvcDogMDtcblx0bGVmdDogMTZweDtcblx0cG9pbnRlci1ldmVudHM6IG5vbmU7XG59XG5cbi5oaWRlLWFycm93cyAubW9uYWNvLXRsLWluZGVudCB7XG5cdGxlZnQ6IDEycHg7XG59XG5cbi5tb25hY28tdGwtaW5kZW50ID4gLmluZGVudC1ndWlkZSB7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblx0Ym94LXNpemluZzogYm9yZGVyLWJveDtcblx0aGVpZ2h0OiAxMDAlO1xuXHRib3JkZXItbGVmdDogMXB4IHNvbGlkIHRyYW5zcGFyZW50O1xufVxuXG4ubW9uYWNvLXRsLWluZGVudCA+IC5pbmRlbnQtZ3VpZGUge1xuXHR0cmFuc2l0aW9uOiBib3JkZXItY29sb3IgMC4xcyBsaW5lYXI7XG59XG5cbi5tb25hY28tdGwtdHdpc3RpZSxcbi5tb25hY28tdGwtY29udGVudHMge1xuXHRoZWlnaHQ6IDEwMCU7XG59XG5cbi5tb25hY28tdGwtdHdpc3RpZSB7XG5cdGZvbnQtc2l6ZTogMTBweDtcblx0dGV4dC1hbGlnbjogcmlnaHQ7XG5cdHBhZGRpbmctcmlnaHQ6IDZweDtcblx0ZmxleC1zaHJpbms6IDA7XG5cdHdpZHRoOiAxNnB4O1xuXHRkaXNwbGF5OiBmbGV4ICFpbXBvcnRhbnQ7XG5cdGFsaWduLWl0ZW1zOiBjZW50ZXI7XG5cdGp1c3RpZnktY29udGVudDogY2VudGVyO1xuXHRjb2xvcjogaW5oZXJpdCAhaW1wb3J0YW50O1xuXHR0cmFuc2Zvcm06IHRyYW5zbGF0ZVgoM3B4KTtcbn1cblxuLm1vbmFjby10bC1jb250ZW50cyB7XG5cdGZsZXg6IDE7XG5cdG92ZXJmbG93OiBoaWRkZW47XG59XG5cbi5tb25hY28tdGwtdHdpc3RpZS5jb2xsYXBzZWQ6OmJlZm9yZSB7XG5cdHRyYW5zZm9ybTogcm90YXRlKC05MGRlZyk7XG59XG5cbi5tb25hY28tdGwtdHdpc3RpZS5jb2RpY29uLXRyZWUtaXRlbS1sb2FkaW5nOjpiZWZvcmUge1xuXHQvKiBVc2Ugc3RlcHMgdG8gdGhyb3R0bGUgRlBTIHRvIHJlZHVjZSBDUFUgdXNhZ2UgKi9cblx0YW5pbWF0aW9uOiBjb2RpY29uLXNwaW4gMS4yNXMgc3RlcHMoMzApIGluZmluaXRlO1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.quick-input-widget {
	font-size: 13px;
}

.quick-input-widget .monaco-highlighted-label .highlight,
.quick-input-widget .monaco-highlighted-label .highlight {
	color: #0066BF;
}

.vs-dark .quick-input-widget .monaco-highlighted-label .highlight,
.vs-dark .quick-input-widget .monaco-highlighted-label .highlight {
	color: #0097fb;
}

.hc-black .quick-input-widget .monaco-highlighted-label .highlight,
.hc-black .quick-input-widget .monaco-highlighted-label .highlight {
	color: #F38518;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9lZGl0b3Ivc3RhbmRhbG9uZS9icm93c2VyL3F1aWNrSW5wdXQvc3RhbmRhbG9uZVF1aWNrSW5wdXQuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLGVBQWU7QUFDaEI7O0FBRUE7O0NBRUMsY0FBYztBQUNmOztBQUVBOztDQUVDLGNBQWM7QUFDZjs7QUFFQTs7Q0FFQyxjQUFjO0FBQ2YiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLnF1aWNrLWlucHV0LXdpZGdldCB7XG5cdGZvbnQtc2l6ZTogMTNweDtcbn1cblxuLnF1aWNrLWlucHV0LXdpZGdldCAubW9uYWNvLWhpZ2hsaWdodGVkLWxhYmVsIC5oaWdobGlnaHQsXG4ucXVpY2staW5wdXQtd2lkZ2V0IC5tb25hY28taGlnaGxpZ2h0ZWQtbGFiZWwgLmhpZ2hsaWdodCB7XG5cdGNvbG9yOiAjMDA2NkJGO1xufVxuXG4udnMtZGFyayAucXVpY2staW5wdXQtd2lkZ2V0IC5tb25hY28taGlnaGxpZ2h0ZWQtbGFiZWwgLmhpZ2hsaWdodCxcbi52cy1kYXJrIC5xdWljay1pbnB1dC13aWRnZXQgLm1vbmFjby1oaWdobGlnaHRlZC1sYWJlbCAuaGlnaGxpZ2h0IHtcblx0Y29sb3I6ICMwMDk3ZmI7XG59XG5cbi5oYy1ibGFjayAucXVpY2staW5wdXQtd2lkZ2V0IC5tb25hY28taGlnaGxpZ2h0ZWQtbGFiZWwgLmhpZ2hsaWdodCxcbi5oYy1ibGFjayAucXVpY2staW5wdXQtd2lkZ2V0IC5tb25hY28taGlnaGxpZ2h0ZWQtbGFiZWwgLmhpZ2hsaWdodCB7XG5cdGNvbG9yOiAjRjM4NTE4O1xufVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.quick-input-widget {
	position: absolute;
	width: 600px;
	z-index: 2000;
	padding-bottom: 6px;
	left: 50%;
	margin-left: -300px;
}

.quick-input-titlebar {
	display: flex;
}

.quick-input-left-action-bar {
	display: flex;
	margin-left: 4px;
	flex: 1;
}

.quick-input-left-action-bar.monaco-action-bar .actions-container {
	justify-content: flex-start;
}

.quick-input-title {
	padding: 3px 0px;
	text-align: center;
}

.quick-input-right-action-bar {
	display: flex;
	margin-right: 4px;
	flex: 1;
}

.quick-input-titlebar .monaco-action-bar .action-label.codicon {
	margin: 0;
	width: 19px;
	height: 100%;
	background-position: center;
	background-repeat: no-repeat;
}

.quick-input-description {
	margin: 6px;
}

.quick-input-header {
	display: flex;
	padding: 6px 6px 0px 6px;
	margin-bottom: -2px;
}

.quick-input-widget.hidden-input .quick-input-header {
	/* reduce margins and paddings when input box hidden */
	padding: 0;
	margin-bottom: 0;
}

.quick-input-and-message {
	display: flex;
	flex-direction: column;
	flex-grow: 1;
	position: relative;
}

.quick-input-check-all {
	align-self: center;
	margin: 0;
}

.quick-input-filter {
	flex-grow: 1;
	display: flex;
	position: relative;
}

.quick-input-box {
	flex-grow: 1;
}

.quick-input-widget.show-checkboxes .quick-input-box,
.quick-input-widget.show-checkboxes .quick-input-message {
	margin-left: 5px;
}

.quick-input-visible-count {
	position: absolute;
	left: -10000px;
}

.quick-input-count {
	align-self: center;
	position: absolute;
	right: 4px;
	display: flex;
	align-items: center;
}

.quick-input-count .monaco-count-badge {
	vertical-align: middle;
	padding: 2px 4px;
	border-radius: 2px;
	min-height: auto;
	line-height: normal;
}

.quick-input-action {
	margin-left: 6px;
}

.quick-input-action .monaco-text-button {
	font-size: 11px;
	padding: 0 6px;
	display: flex;
	height: 100%;
	align-items: center;
}

.quick-input-message {
	margin-top: -1px;
	padding: 5px 5px 2px 5px;
}

.quick-input-progress.monaco-progress-container {
	position: relative;
}

.quick-input-progress.monaco-progress-container,
.quick-input-progress.monaco-progress-container .progress-bit {
	height: 2px;
}

.quick-input-list {
	line-height: 22px;
	margin-top: 6px;
}

.quick-input-widget.hidden-input .quick-input-list {
	margin-top: 0; /* reduce margins when input box hidden */
}

.quick-input-list .monaco-list {
	overflow: hidden;
	max-height: calc(20 * 22px);
}

.quick-input-list .quick-input-list-entry {
	box-sizing: border-box;
	overflow: hidden;
	display: flex;
	height: 100%;
	padding: 0 6px;
}

.quick-input-list .quick-input-list-entry.quick-input-list-separator-border {
	border-top-width: 1px;
	border-top-style: solid;
}

.quick-input-list .monaco-list-row:first-child .quick-input-list-entry.quick-input-list-separator-border {
	border-top-style: none;
}

.quick-input-list .quick-input-list-label {
	overflow: hidden;
	display: flex;
	height: 100%;
	flex: 1;
}

.quick-input-list .quick-input-list-checkbox {
	align-self: center;
	margin: 0;
}

.quick-input-list .quick-input-list-rows {
	overflow: hidden;
	text-overflow: ellipsis;
	display: flex;
	flex-direction: column;
	height: 100%;
	flex: 1;
	margin-left: 5px;
}

.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-rows {
	margin-left: 10px;
}

.quick-input-widget .quick-input-list .quick-input-list-checkbox {
	display: none;
}
.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-checkbox {
	display: inline;
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row {
	display: flex;
	align-items: center;
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-icon-label,
.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-icon-label .monaco-icon-label-container > .monaco-icon-name-container {
	flex: 1; /* make sure the icon label grows within the row */
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row .codicon[class*='codicon-'] {
	vertical-align: sub;
}

.quick-input-list .quick-input-list-rows .monaco-highlighted-label span {
	opacity: 1;
}

.quick-input-list .quick-input-list-entry .quick-input-list-entry-keybinding {
	margin-right: 8px; /* separate from the separator label or scrollbar if any */
}

.quick-input-list .quick-input-list-label-meta {
	opacity: 0.7;
	line-height: normal;
	text-overflow: ellipsis;
	overflow: hidden;
}

.quick-input-list .monaco-highlighted-label .highlight {
	font-weight: bold;
}

.quick-input-list .quick-input-list-entry .quick-input-list-separator {
	margin-right: 8px; /* separate from keybindings or actions */
}

.quick-input-list .quick-input-list-entry-action-bar {
	display: flex;
	flex: 0;
	overflow: visible;
}

.quick-input-list .quick-input-list-entry-action-bar .action-label {
	/*
	 * By default, actions in the quick input action bar are hidden
	 * until hovered over them or selected.
	 */
	display: none;
}

.quick-input-list .quick-input-list-entry-action-bar .action-label.codicon {
	margin: 0;
	height: 100%;
	padding: 0 2px;
	vertical-align: middle;
}

.quick-input-list .quick-input-list-entry-action-bar {
	margin-top: 1px;
}

.quick-input-list .quick-input-list-entry-action-bar {
	margin-right: 4px; /* separate from scrollbar */
}

.quick-input-list .quick-input-list-entry-action-bar .action-label.codicon {
	margin-right: 4px; /* separate actions */
}

.quick-input-list .quick-input-list-entry .quick-input-list-entry-action-bar .action-label.always-visible,
.quick-input-list .quick-input-list-entry:hover .quick-input-list-entry-action-bar .action-label,
.quick-input-list .monaco-list-row.focused .quick-input-list-entry-action-bar .action-label {
	display: flex;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL3BhcnRzL3F1aWNraW5wdXQvYnJvd3Nlci9tZWRpYS9xdWlja0lucHV0LmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxrQkFBa0I7Q0FDbEIsWUFBWTtDQUNaLGFBQWE7Q0FDYixtQkFBbUI7Q0FDbkIsU0FBUztDQUNULG1CQUFtQjtBQUNwQjs7QUFFQTtDQUNDLGFBQWE7QUFDZDs7QUFFQTtDQUNDLGFBQWE7Q0FDYixnQkFBZ0I7Q0FDaEIsT0FBTztBQUNSOztBQUVBO0NBQ0MsMkJBQTJCO0FBQzVCOztBQUVBO0NBQ0MsZ0JBQWdCO0NBQ2hCLGtCQUFrQjtBQUNuQjs7QUFFQTtDQUNDLGFBQWE7Q0FDYixpQkFBaUI7Q0FDakIsT0FBTztBQUNSOztBQUVBO0NBQ0MsU0FBUztDQUNULFdBQVc7Q0FDWCxZQUFZO0NBQ1osMkJBQTJCO0NBQzNCLDRCQUE0QjtBQUM3Qjs7QUFFQTtDQUNDLFdBQVc7QUFDWjs7QUFFQTtDQUNDLGFBQWE7Q0FDYix3QkFBd0I7Q0FDeEIsbUJBQW1CO0FBQ3BCOztBQUVBO0NBQ0Msc0RBQXNEO0NBQ3RELFVBQVU7Q0FDVixnQkFBZ0I7QUFDakI7O0FBRUE7Q0FDQyxhQUFhO0NBQ2Isc0JBQXNCO0NBQ3RCLFlBQVk7Q0FDWixrQkFBa0I7QUFDbkI7O0FBRUE7Q0FDQyxrQkFBa0I7Q0FDbEIsU0FBUztBQUNWOztBQUVBO0NBQ0MsWUFBWTtDQUNaLGFBQWE7Q0FDYixrQkFBa0I7QUFDbkI7O0FBRUE7Q0FDQyxZQUFZO0FBQ2I7O0FBRUE7O0NBRUMsZ0JBQWdCO0FBQ2pCOztBQUVBO0NBQ0Msa0JBQWtCO0NBQ2xCLGNBQWM7QUFDZjs7QUFFQTtDQUNDLGtCQUFrQjtDQUNsQixrQkFBa0I7Q0FDbEIsVUFBVTtDQUNWLGFBQWE7Q0FDYixtQkFBbUI7QUFDcEI7O0FBRUE7Q0FDQyxzQkFBc0I7Q0FDdEIsZ0JBQWdCO0NBQ2hCLGtCQUFrQjtDQUNsQixnQkFBZ0I7Q0FDaEIsbUJBQW1CO0FBQ3BCOztBQUVBO0NBQ0MsZ0JBQWdCO0FBQ2pCOztBQUVBO0NBQ0MsZUFBZTtDQUNmLGNBQWM7Q0FDZCxhQUFhO0NBQ2IsWUFBWTtDQUNaLG1CQUFtQjtBQUNwQjs7QUFFQTtDQUNDLGdCQUFnQjtDQUNoQix3QkFBd0I7QUFDekI7O0FBRUE7Q0FDQyxrQkFBa0I7QUFDbkI7O0FBRUE7O0NBRUMsV0FBVztBQUNaOztBQUVBO0NBQ0MsaUJBQWlCO0NBQ2pCLGVBQWU7QUFDaEI7O0FBRUE7Q0FDQyxhQUFhLEVBQUUseUNBQXlDO0FBQ3pEOztBQUVBO0NBQ0MsZ0JBQWdCO0NBQ2hCLDJCQUEyQjtBQUM1Qjs7QUFFQTtDQUNDLHNCQUFzQjtDQUN0QixnQkFBZ0I7Q0FDaEIsYUFBYTtDQUNiLFlBQVk7Q0FDWixjQUFjO0FBQ2Y7O0FBRUE7Q0FDQyxxQkFBcUI7Q0FDckIsdUJBQXVCO0FBQ3hCOztBQUVBO0NBQ0Msc0JBQXNCO0FBQ3ZCOztBQUVBO0NBQ0MsZ0JBQWdCO0NBQ2hCLGFBQWE7Q0FDYixZQUFZO0NBQ1osT0FBTztBQUNSOztBQUVBO0NBQ0Msa0JBQWtCO0NBQ2xCLFNBQVM7QUFDVjs7QUFFQTtDQUNDLGdCQUFnQjtDQUNoQix1QkFBdUI7Q0FDdkIsYUFBYTtDQUNiLHNCQUFzQjtDQUN0QixZQUFZO0NBQ1osT0FBTztDQUNQLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGlCQUFpQjtBQUNsQjs7QUFFQTtDQUNDLGFBQWE7QUFDZDtBQUNBO0NBQ0MsZUFBZTtBQUNoQjs7QUFFQTtDQUNDLGFBQWE7Q0FDYixtQkFBbUI7QUFDcEI7O0FBRUE7O0NBRUMsT0FBTyxFQUFFLGtEQUFrRDtBQUM1RDs7QUFFQTtDQUNDLG1CQUFtQjtBQUNwQjs7QUFFQTtDQUNDLFVBQVU7QUFDWDs7QUFFQTtDQUNDLGlCQUFpQixFQUFFLDBEQUEwRDtBQUM5RTs7QUFFQTtDQUNDLFlBQVk7Q0FDWixtQkFBbUI7Q0FDbkIsdUJBQXVCO0NBQ3ZCLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLGlCQUFpQjtBQUNsQjs7QUFFQTtDQUNDLGlCQUFpQixFQUFFLHlDQUF5QztBQUM3RDs7QUFFQTtDQUNDLGFBQWE7Q0FDYixPQUFPO0NBQ1AsaUJBQWlCO0FBQ2xCOztBQUVBO0NBQ0M7OztHQUdFO0NBQ0YsYUFBYTtBQUNkOztBQUVBO0NBQ0MsU0FBUztDQUNULFlBQVk7Q0FDWixjQUFjO0NBQ2Qsc0JBQXNCO0FBQ3ZCOztBQUVBO0NBQ0MsZUFBZTtBQUNoQjs7QUFFQTtDQUNDLGlCQUFpQixFQUFFLDRCQUE0QjtBQUNoRDs7QUFFQTtDQUNDLGlCQUFpQixFQUFFLHFCQUFxQjtBQUN6Qzs7QUFFQTs7O0NBR0MsYUFBYTtBQUNkIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5xdWljay1pbnB1dC13aWRnZXQge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdHdpZHRoOiA2MDBweDtcblx0ei1pbmRleDogMjAwMDtcblx0cGFkZGluZy1ib3R0b206IDZweDtcblx0bGVmdDogNTAlO1xuXHRtYXJnaW4tbGVmdDogLTMwMHB4O1xufVxuXG4ucXVpY2staW5wdXQtdGl0bGViYXIge1xuXHRkaXNwbGF5OiBmbGV4O1xufVxuXG4ucXVpY2staW5wdXQtbGVmdC1hY3Rpb24tYmFyIHtcblx0ZGlzcGxheTogZmxleDtcblx0bWFyZ2luLWxlZnQ6IDRweDtcblx0ZmxleDogMTtcbn1cblxuLnF1aWNrLWlucHV0LWxlZnQtYWN0aW9uLWJhci5tb25hY28tYWN0aW9uLWJhciAuYWN0aW9ucy1jb250YWluZXIge1xuXHRqdXN0aWZ5LWNvbnRlbnQ6IGZsZXgtc3RhcnQ7XG59XG5cbi5xdWljay1pbnB1dC10aXRsZSB7XG5cdHBhZGRpbmc6IDNweCAwcHg7XG5cdHRleHQtYWxpZ246IGNlbnRlcjtcbn1cblxuLnF1aWNrLWlucHV0LXJpZ2h0LWFjdGlvbi1iYXIge1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRtYXJnaW4tcmlnaHQ6IDRweDtcblx0ZmxleDogMTtcbn1cblxuLnF1aWNrLWlucHV0LXRpdGxlYmFyIC5tb25hY28tYWN0aW9uLWJhciAuYWN0aW9uLWxhYmVsLmNvZGljb24ge1xuXHRtYXJnaW46IDA7XG5cdHdpZHRoOiAxOXB4O1xuXHRoZWlnaHQ6IDEwMCU7XG5cdGJhY2tncm91bmQtcG9zaXRpb246IGNlbnRlcjtcblx0YmFja2dyb3VuZC1yZXBlYXQ6IG5vLXJlcGVhdDtcbn1cblxuLnF1aWNrLWlucHV0LWRlc2NyaXB0aW9uIHtcblx0bWFyZ2luOiA2cHg7XG59XG5cbi5xdWljay1pbnB1dC1oZWFkZXIge1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRwYWRkaW5nOiA2cHggNnB4IDBweCA2cHg7XG5cdG1hcmdpbi1ib3R0b206IC0ycHg7XG59XG5cbi5xdWljay1pbnB1dC13aWRnZXQuaGlkZGVuLWlucHV0IC5xdWljay1pbnB1dC1oZWFkZXIge1xuXHQvKiByZWR1Y2UgbWFyZ2lucyBhbmQgcGFkZGluZ3Mgd2hlbiBpbnB1dCBib3ggaGlkZGVuICovXG5cdHBhZGRpbmc6IDA7XG5cdG1hcmdpbi1ib3R0b206IDA7XG59XG5cbi5xdWljay1pbnB1dC1hbmQtbWVzc2FnZSB7XG5cdGRpc3BsYXk6IGZsZXg7XG5cdGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG5cdGZsZXgtZ3JvdzogMTtcblx0cG9zaXRpb246IHJlbGF0aXZlO1xufVxuXG4ucXVpY2staW5wdXQtY2hlY2stYWxsIHtcblx0YWxpZ24tc2VsZjogY2VudGVyO1xuXHRtYXJnaW46IDA7XG59XG5cbi5xdWljay1pbnB1dC1maWx0ZXIge1xuXHRmbGV4LWdyb3c6IDE7XG5cdGRpc3BsYXk6IGZsZXg7XG5cdHBvc2l0aW9uOiByZWxhdGl2ZTtcbn1cblxuLnF1aWNrLWlucHV0LWJveCB7XG5cdGZsZXgtZ3JvdzogMTtcbn1cblxuLnF1aWNrLWlucHV0LXdpZGdldC5zaG93LWNoZWNrYm94ZXMgLnF1aWNrLWlucHV0LWJveCxcbi5xdWljay1pbnB1dC13aWRnZXQuc2hvdy1jaGVja2JveGVzIC5xdWljay1pbnB1dC1tZXNzYWdlIHtcblx0bWFyZ2luLWxlZnQ6IDVweDtcbn1cblxuLnF1aWNrLWlucHV0LXZpc2libGUtY291bnQge1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdGxlZnQ6IC0xMDAwMHB4O1xufVxuXG4ucXVpY2staW5wdXQtY291bnQge1xuXHRhbGlnbi1zZWxmOiBjZW50ZXI7XG5cdHBvc2l0aW9uOiBhYnNvbHV0ZTtcblx0cmlnaHQ6IDRweDtcblx0ZGlzcGxheTogZmxleDtcblx0YWxpZ24taXRlbXM6IGNlbnRlcjtcbn1cblxuLnF1aWNrLWlucHV0LWNvdW50IC5tb25hY28tY291bnQtYmFkZ2Uge1xuXHR2ZXJ0aWNhbC1hbGlnbjogbWlkZGxlO1xuXHRwYWRkaW5nOiAycHggNHB4O1xuXHRib3JkZXItcmFkaXVzOiAycHg7XG5cdG1pbi1oZWlnaHQ6IGF1dG87XG5cdGxpbmUtaGVpZ2h0OiBub3JtYWw7XG59XG5cbi5xdWljay1pbnB1dC1hY3Rpb24ge1xuXHRtYXJnaW4tbGVmdDogNnB4O1xufVxuXG4ucXVpY2staW5wdXQtYWN0aW9uIC5tb25hY28tdGV4dC1idXR0b24ge1xuXHRmb250LXNpemU6IDExcHg7XG5cdHBhZGRpbmc6IDAgNnB4O1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRoZWlnaHQ6IDEwMCU7XG5cdGFsaWduLWl0ZW1zOiBjZW50ZXI7XG59XG5cbi5xdWljay1pbnB1dC1tZXNzYWdlIHtcblx0bWFyZ2luLXRvcDogLTFweDtcblx0cGFkZGluZzogNXB4IDVweCAycHggNXB4O1xufVxuXG4ucXVpY2staW5wdXQtcHJvZ3Jlc3MubW9uYWNvLXByb2dyZXNzLWNvbnRhaW5lciB7XG5cdHBvc2l0aW9uOiByZWxhdGl2ZTtcbn1cblxuLnF1aWNrLWlucHV0LXByb2dyZXNzLm1vbmFjby1wcm9ncmVzcy1jb250YWluZXIsXG4ucXVpY2staW5wdXQtcHJvZ3Jlc3MubW9uYWNvLXByb2dyZXNzLWNvbnRhaW5lciAucHJvZ3Jlc3MtYml0IHtcblx0aGVpZ2h0OiAycHg7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IHtcblx0bGluZS1oZWlnaHQ6IDIycHg7XG5cdG1hcmdpbi10b3A6IDZweDtcbn1cblxuLnF1aWNrLWlucHV0LXdpZGdldC5oaWRkZW4taW5wdXQgLnF1aWNrLWlucHV0LWxpc3Qge1xuXHRtYXJnaW4tdG9wOiAwOyAvKiByZWR1Y2UgbWFyZ2lucyB3aGVuIGlucHV0IGJveCBoaWRkZW4gKi9cbn1cblxuLnF1aWNrLWlucHV0LWxpc3QgLm1vbmFjby1saXN0IHtcblx0b3ZlcmZsb3c6IGhpZGRlbjtcblx0bWF4LWhlaWdodDogY2FsYygyMCAqIDIycHgpO1xufVxuXG4ucXVpY2staW5wdXQtbGlzdCAucXVpY2staW5wdXQtbGlzdC1lbnRyeSB7XG5cdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG5cdG92ZXJmbG93OiBoaWRkZW47XG5cdGRpc3BsYXk6IGZsZXg7XG5cdGhlaWdodDogMTAwJTtcblx0cGFkZGluZzogMCA2cHg7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LWVudHJ5LnF1aWNrLWlucHV0LWxpc3Qtc2VwYXJhdG9yLWJvcmRlciB7XG5cdGJvcmRlci10b3Atd2lkdGg6IDFweDtcblx0Ym9yZGVyLXRvcC1zdHlsZTogc29saWQ7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5tb25hY28tbGlzdC1yb3c6Zmlyc3QtY2hpbGQgLnF1aWNrLWlucHV0LWxpc3QtZW50cnkucXVpY2staW5wdXQtbGlzdC1zZXBhcmF0b3ItYm9yZGVyIHtcblx0Ym9yZGVyLXRvcC1zdHlsZTogbm9uZTtcbn1cblxuLnF1aWNrLWlucHV0LWxpc3QgLnF1aWNrLWlucHV0LWxpc3QtbGFiZWwge1xuXHRvdmVyZmxvdzogaGlkZGVuO1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRoZWlnaHQ6IDEwMCU7XG5cdGZsZXg6IDE7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LWNoZWNrYm94IHtcblx0YWxpZ24tc2VsZjogY2VudGVyO1xuXHRtYXJnaW46IDA7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LXJvd3Mge1xuXHRvdmVyZmxvdzogaGlkZGVuO1xuXHR0ZXh0LW92ZXJmbG93OiBlbGxpcHNpcztcblx0ZGlzcGxheTogZmxleDtcblx0ZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcblx0aGVpZ2h0OiAxMDAlO1xuXHRmbGV4OiAxO1xuXHRtYXJnaW4tbGVmdDogNXB4O1xufVxuXG4ucXVpY2staW5wdXQtd2lkZ2V0LnNob3ctY2hlY2tib3hlcyAucXVpY2staW5wdXQtbGlzdCAucXVpY2staW5wdXQtbGlzdC1yb3dzIHtcblx0bWFyZ2luLWxlZnQ6IDEwcHg7XG59XG5cbi5xdWljay1pbnB1dC13aWRnZXQgLnF1aWNrLWlucHV0LWxpc3QgLnF1aWNrLWlucHV0LWxpc3QtY2hlY2tib3gge1xuXHRkaXNwbGF5OiBub25lO1xufVxuLnF1aWNrLWlucHV0LXdpZGdldC5zaG93LWNoZWNrYm94ZXMgLnF1aWNrLWlucHV0LWxpc3QgLnF1aWNrLWlucHV0LWxpc3QtY2hlY2tib3gge1xuXHRkaXNwbGF5OiBpbmxpbmU7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LXJvd3MgPiAucXVpY2staW5wdXQtbGlzdC1yb3cge1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRhbGlnbi1pdGVtczogY2VudGVyO1xufVxuXG4ucXVpY2staW5wdXQtbGlzdCAucXVpY2staW5wdXQtbGlzdC1yb3dzID4gLnF1aWNrLWlucHV0LWxpc3Qtcm93IC5tb25hY28taWNvbi1sYWJlbCxcbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LXJvd3MgPiAucXVpY2staW5wdXQtbGlzdC1yb3cgLm1vbmFjby1pY29uLWxhYmVsIC5tb25hY28taWNvbi1sYWJlbC1jb250YWluZXIgPiAubW9uYWNvLWljb24tbmFtZS1jb250YWluZXIge1xuXHRmbGV4OiAxOyAvKiBtYWtlIHN1cmUgdGhlIGljb24gbGFiZWwgZ3Jvd3Mgd2l0aGluIHRoZSByb3cgKi9cbn1cblxuLnF1aWNrLWlucHV0LWxpc3QgLnF1aWNrLWlucHV0LWxpc3Qtcm93cyA+IC5xdWljay1pbnB1dC1saXN0LXJvdyAuY29kaWNvbltjbGFzcyo9J2NvZGljb24tJ10ge1xuXHR2ZXJ0aWNhbC1hbGlnbjogc3ViO1xufVxuXG4ucXVpY2staW5wdXQtbGlzdCAucXVpY2staW5wdXQtbGlzdC1yb3dzIC5tb25hY28taGlnaGxpZ2h0ZWQtbGFiZWwgc3BhbiB7XG5cdG9wYWNpdHk6IDE7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LWVudHJ5IC5xdWljay1pbnB1dC1saXN0LWVudHJ5LWtleWJpbmRpbmcge1xuXHRtYXJnaW4tcmlnaHQ6IDhweDsgLyogc2VwYXJhdGUgZnJvbSB0aGUgc2VwYXJhdG9yIGxhYmVsIG9yIHNjcm9sbGJhciBpZiBhbnkgKi9cbn1cblxuLnF1aWNrLWlucHV0LWxpc3QgLnF1aWNrLWlucHV0LWxpc3QtbGFiZWwtbWV0YSB7XG5cdG9wYWNpdHk6IDAuNztcblx0bGluZS1oZWlnaHQ6IG5vcm1hbDtcblx0dGV4dC1vdmVyZmxvdzogZWxsaXBzaXM7XG5cdG92ZXJmbG93OiBoaWRkZW47XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5tb25hY28taGlnaGxpZ2h0ZWQtbGFiZWwgLmhpZ2hsaWdodCB7XG5cdGZvbnQtd2VpZ2h0OiBib2xkO1xufVxuXG4ucXVpY2staW5wdXQtbGlzdCAucXVpY2staW5wdXQtbGlzdC1lbnRyeSAucXVpY2staW5wdXQtbGlzdC1zZXBhcmF0b3Ige1xuXHRtYXJnaW4tcmlnaHQ6IDhweDsgLyogc2VwYXJhdGUgZnJvbSBrZXliaW5kaW5ncyBvciBhY3Rpb25zICovXG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LWVudHJ5LWFjdGlvbi1iYXIge1xuXHRkaXNwbGF5OiBmbGV4O1xuXHRmbGV4OiAwO1xuXHRvdmVyZmxvdzogdmlzaWJsZTtcbn1cblxuLnF1aWNrLWlucHV0LWxpc3QgLnF1aWNrLWlucHV0LWxpc3QtZW50cnktYWN0aW9uLWJhciAuYWN0aW9uLWxhYmVsIHtcblx0Lypcblx0ICogQnkgZGVmYXVsdCwgYWN0aW9ucyBpbiB0aGUgcXVpY2sgaW5wdXQgYWN0aW9uIGJhciBhcmUgaGlkZGVuXG5cdCAqIHVudGlsIGhvdmVyZWQgb3ZlciB0aGVtIG9yIHNlbGVjdGVkLlxuXHQgKi9cblx0ZGlzcGxheTogbm9uZTtcbn1cblxuLnF1aWNrLWlucHV0LWxpc3QgLnF1aWNrLWlucHV0LWxpc3QtZW50cnktYWN0aW9uLWJhciAuYWN0aW9uLWxhYmVsLmNvZGljb24ge1xuXHRtYXJnaW46IDA7XG5cdGhlaWdodDogMTAwJTtcblx0cGFkZGluZzogMCAycHg7XG5cdHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LWVudHJ5LWFjdGlvbi1iYXIge1xuXHRtYXJnaW4tdG9wOiAxcHg7XG59XG5cbi5xdWljay1pbnB1dC1saXN0IC5xdWljay1pbnB1dC1saXN0LWVudHJ5LWFjdGlvbi1iYXIge1xuXHRtYXJnaW4tcmlnaHQ6IDRweDsgLyogc2VwYXJhdGUgZnJvbSBzY3JvbGxiYXIgKi9cbn1cblxuLnF1aWNrLWlucHV0LWxpc3QgLnF1aWNrLWlucHV0LWxpc3QtZW50cnktYWN0aW9uLWJhciAuYWN0aW9uLWxhYmVsLmNvZGljb24ge1xuXHRtYXJnaW4tcmlnaHQ6IDRweDsgLyogc2VwYXJhdGUgYWN0aW9ucyAqL1xufVxuXG4ucXVpY2staW5wdXQtbGlzdCAucXVpY2staW5wdXQtbGlzdC1lbnRyeSAucXVpY2staW5wdXQtbGlzdC1lbnRyeS1hY3Rpb24tYmFyIC5hY3Rpb24tbGFiZWwuYWx3YXlzLXZpc2libGUsXG4ucXVpY2staW5wdXQtbGlzdCAucXVpY2staW5wdXQtbGlzdC1lbnRyeTpob3ZlciAucXVpY2staW5wdXQtbGlzdC1lbnRyeS1hY3Rpb24tYmFyIC5hY3Rpb24tbGFiZWwsXG4ucXVpY2staW5wdXQtbGlzdCAubW9uYWNvLWxpc3Qtcm93LmZvY3VzZWQgLnF1aWNrLWlucHV0LWxpc3QtZW50cnktYWN0aW9uLWJhciAuYWN0aW9uLWxhYmVsIHtcblx0ZGlzcGxheTogZmxleDtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* ---------- Icon label ---------- */

.monaco-icon-label {
	display: flex; /* required for icons support :before rule */
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-icon-label::before {

	/* svg icons rendered as background image */
	background-size: 16px;
	background-position: left center;
	background-repeat: no-repeat;
	padding-right: 6px;
	width: 16px;
	height: 22px;
	line-height: inherit !important;
	display: inline-block;

	/* fonts icons */
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	vertical-align: top;

	flex-shrink: 0; /* fix for https://github.com/Microsoft/vscode/issues/13787 */
}

.monaco-icon-label > .monaco-icon-label-container {
	min-width: 0;
	overflow: hidden;
	text-overflow: ellipsis;
	flex: 1;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name {
	color: inherit;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name > .label-separator {
	margin: 0 2px;
	opacity: 0.5;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .7;
	margin-left: 0.5em;
	font-size: 0.9em;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.vs .monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .95;
}

.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.italic > .monaco-icon-description-container > .label-description {
	font-style: italic;
}

.monaco-icon-label.strikethrough > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.strikethrough > .monaco-icon-description-container > .label-description {
	text-decoration: line-through;
}

.monaco-icon-label::after {
	opacity: 0.75;
	font-size: 90%;
	font-weight: 600;
	padding: 0 16px 0 5px;
	text-align: center;
}

/* make sure selection color wins when a label is being selected */
.monaco-list:focus .selected .monaco-icon-label, /* list */
.monaco-list:focus .selected .monaco-icon-label::after
{
	color: inherit !important;
}

.monaco-list-row.focused.selected .label-description,
.monaco-list-row.selected .label-description {
	opacity: .8;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvaWNvbkxhYmVsL2ljb25sYWJlbC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GLHFDQUFxQzs7QUFFckM7Q0FDQyxhQUFhLEVBQUUsNENBQTRDO0NBQzNELGdCQUFnQjtDQUNoQix1QkFBdUI7QUFDeEI7O0FBRUE7O0NBRUMsMkNBQTJDO0NBQzNDLHFCQUFxQjtDQUNyQixnQ0FBZ0M7Q0FDaEMsNEJBQTRCO0NBQzVCLGtCQUFrQjtDQUNsQixXQUFXO0NBQ1gsWUFBWTtDQUNaLCtCQUErQjtDQUMvQixxQkFBcUI7O0NBRXJCLGdCQUFnQjtDQUNoQixtQ0FBbUM7Q0FDbkMsa0NBQWtDO0NBQ2xDLG1CQUFtQjs7Q0FFbkIsY0FBYyxFQUFFLDZEQUE2RDtBQUM5RTs7QUFFQTtDQUNDLFlBQVk7Q0FDWixnQkFBZ0I7Q0FDaEIsdUJBQXVCO0NBQ3ZCLE9BQU87QUFDUjs7QUFFQTtDQUNDLGNBQWM7Q0FDZCxnQkFBZ0IsRUFBRSw0REFBNEQ7QUFDL0U7O0FBRUE7Q0FDQyxhQUFhO0NBQ2IsWUFBWTtBQUNiOztBQUVBO0NBQ0MsV0FBVztDQUNYLGtCQUFrQjtDQUNsQixnQkFBZ0I7Q0FDaEIsZ0JBQWdCLEVBQUUsNERBQTREO0FBQy9FOztBQUVBO0NBQ0MsWUFBWTtBQUNiOztBQUVBOztDQUVDLGtCQUFrQjtBQUNuQjs7QUFFQTs7Q0FFQyw2QkFBNkI7QUFDOUI7O0FBRUE7Q0FDQyxhQUFhO0NBQ2IsY0FBYztDQUNkLGdCQUFnQjtDQUNoQixxQkFBcUI7Q0FDckIsa0JBQWtCO0FBQ25COztBQUVBLGtFQUFrRTtBQUNsRTs7O0NBR0MseUJBQXlCO0FBQzFCOztBQUVBOztDQUVDLFdBQVc7QUFDWiIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4vKiAtLS0tLS0tLS0tIEljb24gbGFiZWwgLS0tLS0tLS0tLSAqL1xuXG4ubW9uYWNvLWljb24tbGFiZWwge1xuXHRkaXNwbGF5OiBmbGV4OyAvKiByZXF1aXJlZCBmb3IgaWNvbnMgc3VwcG9ydCA6YmVmb3JlIHJ1bGUgKi9cblx0b3ZlcmZsb3c6IGhpZGRlbjtcblx0dGV4dC1vdmVyZmxvdzogZWxsaXBzaXM7XG59XG5cbi5tb25hY28taWNvbi1sYWJlbDo6YmVmb3JlIHtcblxuXHQvKiBzdmcgaWNvbnMgcmVuZGVyZWQgYXMgYmFja2dyb3VuZCBpbWFnZSAqL1xuXHRiYWNrZ3JvdW5kLXNpemU6IDE2cHg7XG5cdGJhY2tncm91bmQtcG9zaXRpb246IGxlZnQgY2VudGVyO1xuXHRiYWNrZ3JvdW5kLXJlcGVhdDogbm8tcmVwZWF0O1xuXHRwYWRkaW5nLXJpZ2h0OiA2cHg7XG5cdHdpZHRoOiAxNnB4O1xuXHRoZWlnaHQ6IDIycHg7XG5cdGxpbmUtaGVpZ2h0OiBpbmhlcml0ICFpbXBvcnRhbnQ7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcblxuXHQvKiBmb250cyBpY29ucyAqL1xuXHQtd2Via2l0LWZvbnQtc21vb3RoaW5nOiBhbnRpYWxpYXNlZDtcblx0LW1vei1vc3gtZm9udC1zbW9vdGhpbmc6IGdyYXlzY2FsZTtcblx0dmVydGljYWwtYWxpZ246IHRvcDtcblxuXHRmbGV4LXNocmluazogMDsgLyogZml4IGZvciBodHRwczovL2dpdGh1Yi5jb20vTWljcm9zb2Z0L3ZzY29kZS9pc3N1ZXMvMTM3ODcgKi9cbn1cblxuLm1vbmFjby1pY29uLWxhYmVsID4gLm1vbmFjby1pY29uLWxhYmVsLWNvbnRhaW5lciB7XG5cdG1pbi13aWR0aDogMDtcblx0b3ZlcmZsb3c6IGhpZGRlbjtcblx0dGV4dC1vdmVyZmxvdzogZWxsaXBzaXM7XG5cdGZsZXg6IDE7XG59XG5cbi5tb25hY28taWNvbi1sYWJlbCA+IC5tb25hY28taWNvbi1sYWJlbC1jb250YWluZXIgPiAubW9uYWNvLWljb24tbmFtZS1jb250YWluZXIgPiAubGFiZWwtbmFtZSB7XG5cdGNvbG9yOiBpbmhlcml0O1xuXHR3aGl0ZS1zcGFjZTogcHJlOyAvKiBlbmFibGUgdG8gc2hvdyBsYWJlbHMgdGhhdCBpbmNsdWRlIG11bHRpcGxlIHdoaXRlc3BhY2VzICovXG59XG5cbi5tb25hY28taWNvbi1sYWJlbCA+IC5tb25hY28taWNvbi1sYWJlbC1jb250YWluZXIgPiAubW9uYWNvLWljb24tbmFtZS1jb250YWluZXIgPiAubGFiZWwtbmFtZSA+IC5sYWJlbC1zZXBhcmF0b3Ige1xuXHRtYXJnaW46IDAgMnB4O1xuXHRvcGFjaXR5OiAwLjU7XG59XG5cbi5tb25hY28taWNvbi1sYWJlbCA+IC5tb25hY28taWNvbi1sYWJlbC1jb250YWluZXIgPiAubW9uYWNvLWljb24tZGVzY3JpcHRpb24tY29udGFpbmVyID4gLmxhYmVsLWRlc2NyaXB0aW9uIHtcblx0b3BhY2l0eTogLjc7XG5cdG1hcmdpbi1sZWZ0OiAwLjVlbTtcblx0Zm9udC1zaXplOiAwLjllbTtcblx0d2hpdGUtc3BhY2U6IHByZTsgLyogZW5hYmxlIHRvIHNob3cgbGFiZWxzIHRoYXQgaW5jbHVkZSBtdWx0aXBsZSB3aGl0ZXNwYWNlcyAqL1xufVxuXG4udnMgLm1vbmFjby1pY29uLWxhYmVsID4gLm1vbmFjby1pY29uLWxhYmVsLWNvbnRhaW5lciA+IC5tb25hY28taWNvbi1kZXNjcmlwdGlvbi1jb250YWluZXIgPiAubGFiZWwtZGVzY3JpcHRpb24ge1xuXHRvcGFjaXR5OiAuOTU7XG59XG5cbi5tb25hY28taWNvbi1sYWJlbC5pdGFsaWMgPiAubW9uYWNvLWljb24tbGFiZWwtY29udGFpbmVyID4gLm1vbmFjby1pY29uLW5hbWUtY29udGFpbmVyID4gLmxhYmVsLW5hbWUsXG4ubW9uYWNvLWljb24tbGFiZWwuaXRhbGljID4gLm1vbmFjby1pY29uLWRlc2NyaXB0aW9uLWNvbnRhaW5lciA+IC5sYWJlbC1kZXNjcmlwdGlvbiB7XG5cdGZvbnQtc3R5bGU6IGl0YWxpYztcbn1cblxuLm1vbmFjby1pY29uLWxhYmVsLnN0cmlrZXRocm91Z2ggPiAubW9uYWNvLWljb24tbGFiZWwtY29udGFpbmVyID4gLm1vbmFjby1pY29uLW5hbWUtY29udGFpbmVyID4gLmxhYmVsLW5hbWUsXG4ubW9uYWNvLWljb24tbGFiZWwuc3RyaWtldGhyb3VnaCA+IC5tb25hY28taWNvbi1kZXNjcmlwdGlvbi1jb250YWluZXIgPiAubGFiZWwtZGVzY3JpcHRpb24ge1xuXHR0ZXh0LWRlY29yYXRpb246IGxpbmUtdGhyb3VnaDtcbn1cblxuLm1vbmFjby1pY29uLWxhYmVsOjphZnRlciB7XG5cdG9wYWNpdHk6IDAuNzU7XG5cdGZvbnQtc2l6ZTogOTAlO1xuXHRmb250LXdlaWdodDogNjAwO1xuXHRwYWRkaW5nOiAwIDE2cHggMCA1cHg7XG5cdHRleHQtYWxpZ246IGNlbnRlcjtcbn1cblxuLyogbWFrZSBzdXJlIHNlbGVjdGlvbiBjb2xvciB3aW5zIHdoZW4gYSBsYWJlbCBpcyBiZWluZyBzZWxlY3RlZCAqL1xuLm1vbmFjby1saXN0OmZvY3VzIC5zZWxlY3RlZCAubW9uYWNvLWljb24tbGFiZWwsIC8qIGxpc3QgKi9cbi5tb25hY28tbGlzdDpmb2N1cyAuc2VsZWN0ZWQgLm1vbmFjby1pY29uLWxhYmVsOjphZnRlclxue1xuXHRjb2xvcjogaW5oZXJpdCAhaW1wb3J0YW50O1xufVxuXG4ubW9uYWNvLWxpc3Qtcm93LmZvY3VzZWQuc2VsZWN0ZWQgLmxhYmVsLWRlc2NyaXB0aW9uLFxuLm1vbmFjby1saXN0LXJvdy5zZWxlY3RlZCAubGFiZWwtZGVzY3JpcHRpb24ge1xuXHRvcGFjaXR5OiAuODtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-keybinding {
	display: flex;
	align-items: center;
	line-height: 10px;
}

.monaco-keybinding > .monaco-keybinding-key {
	display: inline-block;
	border: solid 1px rgba(204, 204, 204, 0.4);
	border-bottom-color: rgba(187, 187, 187, 0.4);
	border-radius: 3px;
	box-shadow: inset 0 -1px 0 rgba(187, 187, 187, 0.4);
	background-color: rgba(221, 221, 221, 0.4);
	vertical-align: middle;
	color: #555;
	font-size: 11px;
	padding: 3px 5px;
	margin: 0 2px;
}

.monaco-keybinding > .monaco-keybinding-key:first-child {
	margin-left: 0;
}

.monaco-keybinding > .monaco-keybinding-key:last-child {
	margin-right: 0;
}

.hc-black .monaco-keybinding > .monaco-keybinding-key,
.vs-dark .monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(128, 128, 128, 0.17);
	color: #ccc;
	border: solid 1px rgba(51, 51, 51, 0.6);
	border-bottom-color: rgba(68, 68, 68, 0.6);
	box-shadow: inset 0 -1px 0 rgba(68, 68, 68, 0.6);
}

.monaco-keybinding > .monaco-keybinding-key-separator {
	display: inline-block;
}

.monaco-keybinding > .monaco-keybinding-key-chord-separator {
	width: 6px;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkva2V5YmluZGluZ0xhYmVsL2tleWJpbmRpbmdMYWJlbC5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GO0NBQ0MsYUFBYTtDQUNiLG1CQUFtQjtDQUNuQixpQkFBaUI7QUFDbEI7O0FBRUE7Q0FDQyxxQkFBcUI7Q0FDckIsMENBQTBDO0NBQzFDLDZDQUE2QztDQUM3QyxrQkFBa0I7Q0FDbEIsbURBQW1EO0NBQ25ELDBDQUEwQztDQUMxQyxzQkFBc0I7Q0FDdEIsV0FBVztDQUNYLGVBQWU7Q0FDZixnQkFBZ0I7Q0FDaEIsYUFBYTtBQUNkOztBQUVBO0NBQ0MsY0FBYztBQUNmOztBQUVBO0NBQ0MsZUFBZTtBQUNoQjs7QUFFQTs7Q0FFQywyQ0FBMkM7Q0FDM0MsV0FBVztDQUNYLHVDQUF1QztDQUN2QywwQ0FBMEM7Q0FDMUMsZ0RBQWdEO0FBQ2pEOztBQUVBO0NBQ0MscUJBQXFCO0FBQ3RCOztBQUVBO0NBQ0MsVUFBVTtBQUNYIiwic291cmNlc0NvbnRlbnQiOlsiLyotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAqICBDb3B5cmlnaHQgKGMpIE1pY3Jvc29mdCBDb3Jwb3JhdGlvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cbiAqICBMaWNlbnNlZCB1bmRlciB0aGUgTUlUIExpY2Vuc2UuIFNlZSBMaWNlbnNlLnR4dCBpbiB0aGUgcHJvamVjdCByb290IGZvciBsaWNlbnNlIGluZm9ybWF0aW9uLlxuICotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbi5tb25hY28ta2V5YmluZGluZyB7XG5cdGRpc3BsYXk6IGZsZXg7XG5cdGFsaWduLWl0ZW1zOiBjZW50ZXI7XG5cdGxpbmUtaGVpZ2h0OiAxMHB4O1xufVxuXG4ubW9uYWNvLWtleWJpbmRpbmcgPiAubW9uYWNvLWtleWJpbmRpbmcta2V5IHtcblx0ZGlzcGxheTogaW5saW5lLWJsb2NrO1xuXHRib3JkZXI6IHNvbGlkIDFweCByZ2JhKDIwNCwgMjA0LCAyMDQsIDAuNCk7XG5cdGJvcmRlci1ib3R0b20tY29sb3I6IHJnYmEoMTg3LCAxODcsIDE4NywgMC40KTtcblx0Ym9yZGVyLXJhZGl1czogM3B4O1xuXHRib3gtc2hhZG93OiBpbnNldCAwIC0xcHggMCByZ2JhKDE4NywgMTg3LCAxODcsIDAuNCk7XG5cdGJhY2tncm91bmQtY29sb3I6IHJnYmEoMjIxLCAyMjEsIDIyMSwgMC40KTtcblx0dmVydGljYWwtYWxpZ246IG1pZGRsZTtcblx0Y29sb3I6ICM1NTU7XG5cdGZvbnQtc2l6ZTogMTFweDtcblx0cGFkZGluZzogM3B4IDVweDtcblx0bWFyZ2luOiAwIDJweDtcbn1cblxuLm1vbmFjby1rZXliaW5kaW5nID4gLm1vbmFjby1rZXliaW5kaW5nLWtleTpmaXJzdC1jaGlsZCB7XG5cdG1hcmdpbi1sZWZ0OiAwO1xufVxuXG4ubW9uYWNvLWtleWJpbmRpbmcgPiAubW9uYWNvLWtleWJpbmRpbmcta2V5Omxhc3QtY2hpbGQge1xuXHRtYXJnaW4tcmlnaHQ6IDA7XG59XG5cbi5oYy1ibGFjayAubW9uYWNvLWtleWJpbmRpbmcgPiAubW9uYWNvLWtleWJpbmRpbmcta2V5LFxuLnZzLWRhcmsgLm1vbmFjby1rZXliaW5kaW5nID4gLm1vbmFjby1rZXliaW5kaW5nLWtleSB7XG5cdGJhY2tncm91bmQtY29sb3I6IHJnYmEoMTI4LCAxMjgsIDEyOCwgMC4xNyk7XG5cdGNvbG9yOiAjY2NjO1xuXHRib3JkZXI6IHNvbGlkIDFweCByZ2JhKDUxLCA1MSwgNTEsIDAuNik7XG5cdGJvcmRlci1ib3R0b20tY29sb3I6IHJnYmEoNjgsIDY4LCA2OCwgMC42KTtcblx0Ym94LXNoYWRvdzogaW5zZXQgMCAtMXB4IDAgcmdiYSg2OCwgNjgsIDY4LCAwLjYpO1xufVxuXG4ubW9uYWNvLWtleWJpbmRpbmcgPiAubW9uYWNvLWtleWJpbmRpbmcta2V5LXNlcGFyYXRvciB7XG5cdGRpc3BsYXk6IGlubGluZS1ibG9jaztcbn1cblxuLm1vbmFjby1rZXliaW5kaW5nID4gLm1vbmFjby1rZXliaW5kaW5nLWtleS1jaG9yZC1zZXBhcmF0b3Ige1xuXHR3aWR0aDogNnB4O1xufSJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-count-badge {
	padding: 3px 6px;
	border-radius: 11px;
	font-size: 11px;
	min-width: 18px;
	min-height: 18px;
	line-height: 11px;
	font-weight: normal;
	text-align: center;
	display: inline-block;
	box-sizing: border-box;
}

.monaco-count-badge.long {
	padding: 2px 3px;
	border-radius: 2px;
	min-height: auto;
	line-height: normal;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvY291bnRCYWRnZS9jb3VudEJhZGdlLmNzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7OytGQUcrRjs7QUFFL0Y7Q0FDQyxnQkFBZ0I7Q0FDaEIsbUJBQW1CO0NBQ25CLGVBQWU7Q0FDZixlQUFlO0NBQ2YsZ0JBQWdCO0NBQ2hCLGlCQUFpQjtDQUNqQixtQkFBbUI7Q0FDbkIsa0JBQWtCO0NBQ2xCLHFCQUFxQjtDQUNyQixzQkFBc0I7QUFDdkI7O0FBRUE7Q0FDQyxnQkFBZ0I7Q0FDaEIsa0JBQWtCO0NBQ2xCLGdCQUFnQjtDQUNoQixtQkFBbUI7QUFDcEIiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLm1vbmFjby1jb3VudC1iYWRnZSB7XG5cdHBhZGRpbmc6IDNweCA2cHg7XG5cdGJvcmRlci1yYWRpdXM6IDExcHg7XG5cdGZvbnQtc2l6ZTogMTFweDtcblx0bWluLXdpZHRoOiAxOHB4O1xuXHRtaW4taGVpZ2h0OiAxOHB4O1xuXHRsaW5lLWhlaWdodDogMTFweDtcblx0Zm9udC13ZWlnaHQ6IG5vcm1hbDtcblx0dGV4dC1hbGlnbjogY2VudGVyO1xuXHRkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XG5cdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG59XG5cbi5tb25hY28tY291bnQtYmFkZ2UubG9uZyB7XG5cdHBhZGRpbmc6IDJweCAzcHg7XG5cdGJvcmRlci1yYWRpdXM6IDJweDtcblx0bWluLWhlaWdodDogYXV0bztcblx0bGluZS1oZWlnaHQ6IG5vcm1hbDtcbn1cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-progress-container {
	width: 100%;
	height: 5px;
	overflow: hidden; /* keep progress bit in bounds */
}

.monaco-progress-container .progress-bit {
	width: 2%;
	height: 5px;
	position: absolute;
	left: 0;
	display: none;
}

.monaco-progress-container.active .progress-bit {
	display: inherit;
}

.monaco-progress-container.discrete .progress-bit {
	left: 0;
	transition: width 100ms linear;
}

.monaco-progress-container.discrete.done .progress-bit {
	width: 100%;
}

.monaco-progress-container.infinite .progress-bit {
	animation-name: progress;
	animation-duration: 4s;
	animation-iteration-count: infinite;
	animation-timing-function: linear;
	transform: translate3d(0px, 0px, 0px);
}

/**
 * The progress bit has a width: 2% (1/50) of the parent container. The animation moves it from 0% to 100% of
 * that container. Since translateX is relative to the progress bit size, we have to multiple it with
 * its relative size to the parent container:
 *  50%: 50 * 50 = 2500%
 * 100%: 50 * 100 - 50 (do not overflow): 4950%
 */
@keyframes progress { from { transform: translateX(0%) scaleX(1) } 50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4950%) scaleX(1) } }

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvcHJvZ3Jlc3NiYXIvcHJvZ3Jlc3NiYXIuY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7K0ZBRytGOztBQUUvRjtDQUNDLFdBQVc7Q0FDWCxXQUFXO0NBQ1gsZ0JBQWdCLEVBQUUsZ0NBQWdDO0FBQ25EOztBQUVBO0NBQ0MsU0FBUztDQUNULFdBQVc7Q0FDWCxrQkFBa0I7Q0FDbEIsT0FBTztDQUNQLGFBQWE7QUFDZDs7QUFFQTtDQUNDLGdCQUFnQjtBQUNqQjs7QUFFQTtDQUNDLE9BQU87Q0FDUCw4QkFBOEI7QUFDL0I7O0FBRUE7Q0FDQyxXQUFXO0FBQ1o7O0FBRUE7Q0FDQyx3QkFBd0I7Q0FDeEIsc0JBQXNCO0NBQ3RCLG1DQUFtQztDQUNuQyxpQ0FBaUM7Q0FDakMscUNBQXFDO0FBQ3RDOztBQUVBOzs7Ozs7RUFNRTtBQUNGLHNCQUFzQixPQUFPLG9DQUFvQyxFQUFFLE1BQU0sdUNBQXVDLEVBQUUsS0FBSyx1Q0FBdUMsRUFBRSIsInNvdXJjZXNDb250ZW50IjpbIi8qLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gKiAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uIEFsbCByaWdodHMgcmVzZXJ2ZWQuXG4gKiAgTGljZW5zZWQgdW5kZXIgdGhlIE1JVCBMaWNlbnNlLiBTZWUgTGljZW5zZS50eHQgaW4gdGhlIHByb2plY3Qgcm9vdCBmb3IgbGljZW5zZSBpbmZvcm1hdGlvbi5cbiAqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG4ubW9uYWNvLXByb2dyZXNzLWNvbnRhaW5lciB7XG5cdHdpZHRoOiAxMDAlO1xuXHRoZWlnaHQ6IDVweDtcblx0b3ZlcmZsb3c6IGhpZGRlbjsgLyoga2VlcCBwcm9ncmVzcyBiaXQgaW4gYm91bmRzICovXG59XG5cbi5tb25hY28tcHJvZ3Jlc3MtY29udGFpbmVyIC5wcm9ncmVzcy1iaXQge1xuXHR3aWR0aDogMiU7XG5cdGhlaWdodDogNXB4O1xuXHRwb3NpdGlvbjogYWJzb2x1dGU7XG5cdGxlZnQ6IDA7XG5cdGRpc3BsYXk6IG5vbmU7XG59XG5cbi5tb25hY28tcHJvZ3Jlc3MtY29udGFpbmVyLmFjdGl2ZSAucHJvZ3Jlc3MtYml0IHtcblx0ZGlzcGxheTogaW5oZXJpdDtcbn1cblxuLm1vbmFjby1wcm9ncmVzcy1jb250YWluZXIuZGlzY3JldGUgLnByb2dyZXNzLWJpdCB7XG5cdGxlZnQ6IDA7XG5cdHRyYW5zaXRpb246IHdpZHRoIDEwMG1zIGxpbmVhcjtcbn1cblxuLm1vbmFjby1wcm9ncmVzcy1jb250YWluZXIuZGlzY3JldGUuZG9uZSAucHJvZ3Jlc3MtYml0IHtcblx0d2lkdGg6IDEwMCU7XG59XG5cbi5tb25hY28tcHJvZ3Jlc3MtY29udGFpbmVyLmluZmluaXRlIC5wcm9ncmVzcy1iaXQge1xuXHRhbmltYXRpb24tbmFtZTogcHJvZ3Jlc3M7XG5cdGFuaW1hdGlvbi1kdXJhdGlvbjogNHM7XG5cdGFuaW1hdGlvbi1pdGVyYXRpb24tY291bnQ6IGluZmluaXRlO1xuXHRhbmltYXRpb24tdGltaW5nLWZ1bmN0aW9uOiBsaW5lYXI7XG5cdHRyYW5zZm9ybTogdHJhbnNsYXRlM2QoMHB4LCAwcHgsIDBweCk7XG59XG5cbi8qKlxuICogVGhlIHByb2dyZXNzIGJpdCBoYXMgYSB3aWR0aDogMiUgKDEvNTApIG9mIHRoZSBwYXJlbnQgY29udGFpbmVyLiBUaGUgYW5pbWF0aW9uIG1vdmVzIGl0IGZyb20gMCUgdG8gMTAwJSBvZlxuICogdGhhdCBjb250YWluZXIuIFNpbmNlIHRyYW5zbGF0ZVggaXMgcmVsYXRpdmUgdG8gdGhlIHByb2dyZXNzIGJpdCBzaXplLCB3ZSBoYXZlIHRvIG11bHRpcGxlIGl0IHdpdGhcbiAqIGl0cyByZWxhdGl2ZSBzaXplIHRvIHRoZSBwYXJlbnQgY29udGFpbmVyOlxuICogIDUwJTogNTAgKiA1MCA9IDI1MDAlXG4gKiAxMDAlOiA1MCAqIDEwMCAtIDUwIChkbyBub3Qgb3ZlcmZsb3cpOiA0OTUwJVxuICovXG5Aa2V5ZnJhbWVzIHByb2dyZXNzIHsgZnJvbSB7IHRyYW5zZm9ybTogdHJhbnNsYXRlWCgwJSkgc2NhbGVYKDEpIH0gNTAlIHsgdHJhbnNmb3JtOiB0cmFuc2xhdGVYKDI1MDAlKSBzY2FsZVgoMykgfSB0byB7IHRyYW5zZm9ybTogdHJhbnNsYXRlWCg0OTUwJSkgc2NhbGVYKDEpIH0gfVxuIl0sInNvdXJjZVJvb3QiOiIifQ== */</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-text-button {
	box-sizing: border-box;
	display: flex;
	width: 100%;
	padding: 4px;
	text-align: center;
	cursor: pointer;
	outline-offset: 2px !important;
	justify-content: center;
	align-items: center;
}

.monaco-text-button:hover {
	text-decoration: none !important;
}

.monaco-button.disabled {
	opacity: 0.4;
	cursor: default;
}

.monaco-button > .codicon {
	margin: 0 0.2em;
	color: inherit !important;
}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9tb25hY28tZWRpdG9yL2VzbS92cy9iYXNlL2Jyb3dzZXIvdWkvYnV0dG9uL2J1dHRvbi5jc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7OzsrRkFHK0Y7O0FBRS9GO0NBQ0Msc0JBQXNCO0NBQ3RCLGFBQWE7Q0FDYixXQUFXO0NBQ1gsWUFBWTtDQUNaLGtCQUFrQjtDQUNsQixlQUFlO0NBQ2YsOEJBQThCO0NBQzlCLHVCQUF1QjtDQUN2QixtQkFBbUI7QUFDcEI7O0FBRUE7Q0FDQyxnQ0FBZ0M7QUFDakM7O0FBRUE7Q0FDQyxZQUFZO0NBQ1osZUFBZTtBQUNoQjs7QUFFQTtDQUNDLGVBQWU7Q0FDZix5QkFBeUI7QUFDMUIiLCJzb3VyY2VzQ29udGVudCI6WyIvKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICogIENvcHlyaWdodCAoYykgTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLlxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBNSVQgTGljZW5zZS4gU2VlIExpY2Vuc2UudHh0IGluIHRoZSBwcm9qZWN0IHJvb3QgZm9yIGxpY2Vuc2UgaW5mb3JtYXRpb24uXG4gKi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuLm1vbmFjby10ZXh0LWJ1dHRvbiB7XG5cdGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG5cdGRpc3BsYXk6IGZsZXg7XG5cdHdpZHRoOiAxMDAlO1xuXHRwYWRkaW5nOiA0cHg7XG5cdHRleHQtYWxpZ246IGNlbnRlcjtcblx0Y3Vyc29yOiBwb2ludGVyO1xuXHRvdXRsaW5lLW9mZnNldDogMnB4ICFpbXBvcnRhbnQ7XG5cdGp1c3RpZnktY29udGVudDogY2VudGVyO1xuXHRhbGlnbi1pdGVtczogY2VudGVyO1xufVxuXG4ubW9uYWNvLXRleHQtYnV0dG9uOmhvdmVyIHtcblx0dGV4dC1kZWNvcmF0aW9uOiBub25lICFpbXBvcnRhbnQ7XG59XG5cbi5tb25hY28tYnV0dG9uLmRpc2FibGVkIHtcblx0b3BhY2l0eTogMC40O1xuXHRjdXJzb3I6IGRlZmF1bHQ7XG59XG5cbi5tb25hY28tYnV0dG9uID4gLmNvZGljb24ge1xuXHRtYXJnaW46IDAgMC4yZW07XG5cdGNvbG9yOiBpbmhlcml0ICFpbXBvcnRhbnQ7XG59XG4iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>:root{--diff-background-color:initial;--diff-text-color:initial;--diff-font-family:Consolas,Courier,monospace;--diff-selection-background-color:#b3d7ff;--diff-gutter-insert-background-color:#d6fedb;--diff-gutter-delete-background-color:#fadde0;--diff-gutter-selected-background-color:#fffce0;--diff-code-insert-background-color:#eaffee;--diff-code-delete-background-color:#fdeff0;--diff-code-insert-edit-background-color:#c0dc91;--diff-code-delete-edit-background-color:#f39ea2;--diff-code-selected-background-color:#fffce0;--diff-omit-gutter-line-color:#cb2a1d;}.diff{background-color:initial;background-color:var(--diff-background-color);color:initial;color:var(--diff-text-color);table-layout:fixed;border-collapse:collapse;width:100%;}.diff::-moz-selection{background-color:#b3d7ff;background-color:var(--diff-selection-background-color);}.diff::selection{background-color:#b3d7ff;background-color:var(--diff-selection-background-color);}.diff td{vertical-align:top;padding-top:0;padding-bottom:0;}.diff-line{line-height:1.5;font-family:Consolas,Courier,monospace;font-family:var(--diff-font-family);}.diff-gutter>a{color:inherit;display:block;}.diff-gutter,.diff-gutter>a{padding:0 1ch;text-align:right;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}.diff-gutter-insert{background-color:#d6fedb;background-color:var(--diff-gutter-insert-background-color);}.diff-gutter-delete{background-color:#fadde0;background-color:var(--diff-gutter-delete-background-color);}.diff-gutter-omit{cursor:default;}.diff-gutter-selected{background-color:#fffce0;background-color:var(--diff-gutter-selected-background-color);}.diff-code{white-space:pre-wrap;word-wrap:break-word;word-break:break-all;padding:0 0 0 .5em;}.diff-code-edit{display:inline-block;color:inherit;}.diff-code-insert{background-color:#eaffee;background-color:var(--diff-code-insert-background-color);}.diff-code-insert .diff-code-edit{background-color:#c0dc91;background-color:var(--diff-code-insert-edit-background-color);}.diff-code-delete{background-color:#fdeff0;background-color:var(--diff-code-delete-background-color);}.diff-code-delete .diff-code-edit{background-color:#f39ea2;background-color:var(--diff-code-delete-edit-background-color);}.diff-code-selected{background-color:#fffce0;background-color:var(--diff-code-selected-background-color);}.diff-widget-content{vertical-align:top;}.diff-gutter-col{width:7ch;}.diff-gutter-omit{height:0;}.diff-gutter-omit:before{content:" ";display:block;white-space:pre;width:2px;height:100%;margin-left:4.6ch;overflow:hidden;background-color:#cb2a1d;background-color:var(--diff-omit-gutter-line-color);}.diff-decoration{line-height:1.5;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}.diff-decoration-content{font-family:Consolas,Courier,monospace;font-family:var(--diff-font-family);padding:0;}

/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8uL25vZGVfbW9kdWxlcy9yZWFjdC1kaWZmLXZpZXcvc3R5bGUvaW5kZXguY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBLE1BQU0sK0JBQStCLENBQUMseUJBQXlCLENBQUMsNkNBQTZDLENBQUMseUNBQXlDLENBQUMsNkNBQTZDLENBQUMsNkNBQTZDLENBQUMsK0NBQStDLENBQUMsMkNBQTJDLENBQUMsMkNBQTJDLENBQUMsZ0RBQWdELENBQUMsZ0RBQWdELENBQUMsNkNBQTZDLENBQUMscUNBQXFDLENBQUMsQ0FBQyxNQUFNLHdCQUF3QixDQUFDLDZDQUE2QyxDQUFDLGFBQWEsQ0FBQyw0QkFBNEIsQ0FBQyxrQkFBa0IsQ0FBQyx3QkFBd0IsQ0FBQyxVQUFVLENBQUMsQ0FBQyxzQkFBc0Isd0JBQXdCLENBQUMsdURBQXVELENBQUMsQ0FBQyxpQkFBaUIsd0JBQXdCLENBQUMsdURBQXVELENBQUMsQ0FBQyxTQUFTLGtCQUFrQixDQUFDLGFBQWEsQ0FBQyxnQkFBZ0IsQ0FBQyxDQUFDLFdBQVcsZUFBZSxDQUFDLHNDQUFzQyxDQUFDLG1DQUFtQyxDQUFDLENBQUMsZUFBZSxhQUFhLENBQUMsYUFBYSxDQUFDLENBQUMsNEJBQTRCLGFBQWEsQ0FBQyxnQkFBZ0IsQ0FBQyxjQUFjLENBQUMsd0JBQXdCLENBQUMscUJBQXFCLENBQUMsb0JBQW9CLENBQUMsZ0JBQWdCLENBQUMsQ0FBQyxvQkFBb0Isd0JBQXdCLENBQUMsMkRBQTJELENBQUMsQ0FBQyxvQkFBb0Isd0JBQXdCLENBQUMsMkRBQTJELENBQUMsQ0FBQyxrQkFBa0IsY0FBYyxDQUFDLENBQUMsc0JBQXNCLHdCQUF3QixDQUFDLDZEQUE2RCxDQUFDLENBQUMsV0FBVyxvQkFBb0IsQ0FBQyxvQkFBb0IsQ0FBQyxvQkFBb0IsQ0FBQyxrQkFBa0IsQ0FBQyxDQUFDLGdCQUFnQixvQkFBb0IsQ0FBQyxhQUFhLENBQUMsQ0FBQyxrQkFBa0Isd0JBQXdCLENBQUMseURBQXlELENBQUMsQ0FBQyxrQ0FBa0Msd0JBQXdCLENBQUMsOERBQThELENBQUMsQ0FBQyxrQkFBa0Isd0JBQXdCLENBQUMseURBQXlELENBQUMsQ0FBQyxrQ0FBa0Msd0JBQXdCLENBQUMsOERBQThELENBQUMsQ0FBQyxvQkFBb0Isd0JBQXdCLENBQUMsMkRBQTJELENBQUMsQ0FBQyxxQkFBcUIsa0JBQWtCLENBQUMsQ0FBQyxpQkFBaUIsU0FBUyxDQUFDLENBQUMsa0JBQWtCLFFBQVEsQ0FBQyxDQUFDLHlCQUF5QixXQUFXLENBQUMsYUFBYSxDQUFDLGVBQWUsQ0FBQyxTQUFTLENBQUMsV0FBVyxDQUFDLGlCQUFpQixDQUFDLGVBQWUsQ0FBQyx3QkFBd0IsQ0FBQyxtREFBbUQsQ0FBQyxDQUFDLGlCQUFpQixlQUFlLENBQUMsd0JBQXdCLENBQUMscUJBQXFCLENBQUMsb0JBQW9CLENBQUMsZ0JBQWdCLENBQUMsQ0FBQyx5QkFBeUIsc0NBQXNDLENBQUMsbUNBQW1DLENBQUMsU0FBUyxDQUFDIiwic291cmNlc0NvbnRlbnQiOlsiOnJvb3R7LS1kaWZmLWJhY2tncm91bmQtY29sb3I6aW5pdGlhbDstLWRpZmYtdGV4dC1jb2xvcjppbml0aWFsOy0tZGlmZi1mb250LWZhbWlseTpDb25zb2xhcyxDb3VyaWVyLG1vbm9zcGFjZTstLWRpZmYtc2VsZWN0aW9uLWJhY2tncm91bmQtY29sb3I6I2IzZDdmZjstLWRpZmYtZ3V0dGVyLWluc2VydC1iYWNrZ3JvdW5kLWNvbG9yOiNkNmZlZGI7LS1kaWZmLWd1dHRlci1kZWxldGUtYmFja2dyb3VuZC1jb2xvcjojZmFkZGUwOy0tZGlmZi1ndXR0ZXItc2VsZWN0ZWQtYmFja2dyb3VuZC1jb2xvcjojZmZmY2UwOy0tZGlmZi1jb2RlLWluc2VydC1iYWNrZ3JvdW5kLWNvbG9yOiNlYWZmZWU7LS1kaWZmLWNvZGUtZGVsZXRlLWJhY2tncm91bmQtY29sb3I6I2ZkZWZmMDstLWRpZmYtY29kZS1pbnNlcnQtZWRpdC1iYWNrZ3JvdW5kLWNvbG9yOiNjMGRjOTE7LS1kaWZmLWNvZGUtZGVsZXRlLWVkaXQtYmFja2dyb3VuZC1jb2xvcjojZjM5ZWEyOy0tZGlmZi1jb2RlLXNlbGVjdGVkLWJhY2tncm91bmQtY29sb3I6I2ZmZmNlMDstLWRpZmYtb21pdC1ndXR0ZXItbGluZS1jb2xvcjojY2IyYTFkO30uZGlmZntiYWNrZ3JvdW5kLWNvbG9yOmluaXRpYWw7YmFja2dyb3VuZC1jb2xvcjp2YXIoLS1kaWZmLWJhY2tncm91bmQtY29sb3IpO2NvbG9yOmluaXRpYWw7Y29sb3I6dmFyKC0tZGlmZi10ZXh0LWNvbG9yKTt0YWJsZS1sYXlvdXQ6Zml4ZWQ7Ym9yZGVyLWNvbGxhcHNlOmNvbGxhcHNlO3dpZHRoOjEwMCU7fS5kaWZmOjotbW96LXNlbGVjdGlvbntiYWNrZ3JvdW5kLWNvbG9yOiNiM2Q3ZmY7YmFja2dyb3VuZC1jb2xvcjp2YXIoLS1kaWZmLXNlbGVjdGlvbi1iYWNrZ3JvdW5kLWNvbG9yKTt9LmRpZmY6OnNlbGVjdGlvbntiYWNrZ3JvdW5kLWNvbG9yOiNiM2Q3ZmY7YmFja2dyb3VuZC1jb2xvcjp2YXIoLS1kaWZmLXNlbGVjdGlvbi1iYWNrZ3JvdW5kLWNvbG9yKTt9LmRpZmYgdGR7dmVydGljYWwtYWxpZ246dG9wO3BhZGRpbmctdG9wOjA7cGFkZGluZy1ib3R0b206MDt9LmRpZmYtbGluZXtsaW5lLWhlaWdodDoxLjU7Zm9udC1mYW1pbHk6Q29uc29sYXMsQ291cmllcixtb25vc3BhY2U7Zm9udC1mYW1pbHk6dmFyKC0tZGlmZi1mb250LWZhbWlseSk7fS5kaWZmLWd1dHRlcj5he2NvbG9yOmluaGVyaXQ7ZGlzcGxheTpibG9jazt9LmRpZmYtZ3V0dGVyLC5kaWZmLWd1dHRlcj5he3BhZGRpbmc6MCAxY2g7dGV4dC1hbGlnbjpyaWdodDtjdXJzb3I6cG9pbnRlcjstd2Via2l0LXVzZXItc2VsZWN0Om5vbmU7LW1vei11c2VyLXNlbGVjdDpub25lOy1tcy11c2VyLXNlbGVjdDpub25lO3VzZXItc2VsZWN0Om5vbmU7fS5kaWZmLWd1dHRlci1pbnNlcnR7YmFja2dyb3VuZC1jb2xvcjojZDZmZWRiO2JhY2tncm91bmQtY29sb3I6dmFyKC0tZGlmZi1ndXR0ZXItaW5zZXJ0LWJhY2tncm91bmQtY29sb3IpO30uZGlmZi1ndXR0ZXItZGVsZXRle2JhY2tncm91bmQtY29sb3I6I2ZhZGRlMDtiYWNrZ3JvdW5kLWNvbG9yOnZhcigtLWRpZmYtZ3V0dGVyLWRlbGV0ZS1iYWNrZ3JvdW5kLWNvbG9yKTt9LmRpZmYtZ3V0dGVyLW9taXR7Y3Vyc29yOmRlZmF1bHQ7fS5kaWZmLWd1dHRlci1zZWxlY3RlZHtiYWNrZ3JvdW5kLWNvbG9yOiNmZmZjZTA7YmFja2dyb3VuZC1jb2xvcjp2YXIoLS1kaWZmLWd1dHRlci1zZWxlY3RlZC1iYWNrZ3JvdW5kLWNvbG9yKTt9LmRpZmYtY29kZXt3aGl0ZS1zcGFjZTpwcmUtd3JhcDt3b3JkLXdyYXA6YnJlYWstd29yZDt3b3JkLWJyZWFrOmJyZWFrLWFsbDtwYWRkaW5nOjAgMCAwIC41ZW07fS5kaWZmLWNvZGUtZWRpdHtkaXNwbGF5OmlubGluZS1ibG9jaztjb2xvcjppbmhlcml0O30uZGlmZi1jb2RlLWluc2VydHtiYWNrZ3JvdW5kLWNvbG9yOiNlYWZmZWU7YmFja2dyb3VuZC1jb2xvcjp2YXIoLS1kaWZmLWNvZGUtaW5zZXJ0LWJhY2tncm91bmQtY29sb3IpO30uZGlmZi1jb2RlLWluc2VydCAuZGlmZi1jb2RlLWVkaXR7YmFja2dyb3VuZC1jb2xvcjojYzBkYzkxO2JhY2tncm91bmQtY29sb3I6dmFyKC0tZGlmZi1jb2RlLWluc2VydC1lZGl0LWJhY2tncm91bmQtY29sb3IpO30uZGlmZi1jb2RlLWRlbGV0ZXtiYWNrZ3JvdW5kLWNvbG9yOiNmZGVmZjA7YmFja2dyb3VuZC1jb2xvcjp2YXIoLS1kaWZmLWNvZGUtZGVsZXRlLWJhY2tncm91bmQtY29sb3IpO30uZGlmZi1jb2RlLWRlbGV0ZSAuZGlmZi1jb2RlLWVkaXR7YmFja2dyb3VuZC1jb2xvcjojZjM5ZWEyO2JhY2tncm91bmQtY29sb3I6dmFyKC0tZGlmZi1jb2RlLWRlbGV0ZS1lZGl0LWJhY2tncm91bmQtY29sb3IpO30uZGlmZi1jb2RlLXNlbGVjdGVke2JhY2tncm91bmQtY29sb3I6I2ZmZmNlMDtiYWNrZ3JvdW5kLWNvbG9yOnZhcigtLWRpZmYtY29kZS1zZWxlY3RlZC1iYWNrZ3JvdW5kLWNvbG9yKTt9LmRpZmYtd2lkZ2V0LWNvbnRlbnR7dmVydGljYWwtYWxpZ246dG9wO30uZGlmZi1ndXR0ZXItY29se3dpZHRoOjdjaDt9LmRpZmYtZ3V0dGVyLW9taXR7aGVpZ2h0OjA7fS5kaWZmLWd1dHRlci1vbWl0OmJlZm9yZXtjb250ZW50OlwiIFwiO2Rpc3BsYXk6YmxvY2s7d2hpdGUtc3BhY2U6cHJlO3dpZHRoOjJweDtoZWlnaHQ6MTAwJTttYXJnaW4tbGVmdDo0LjZjaDtvdmVyZmxvdzpoaWRkZW47YmFja2dyb3VuZC1jb2xvcjojY2IyYTFkO2JhY2tncm91bmQtY29sb3I6dmFyKC0tZGlmZi1vbWl0LWd1dHRlci1saW5lLWNvbG9yKTt9LmRpZmYtZGVjb3JhdGlvbntsaW5lLWhlaWdodDoxLjU7LXdlYmtpdC11c2VyLXNlbGVjdDpub25lOy1tb3otdXNlci1zZWxlY3Q6bm9uZTstbXMtdXNlci1zZWxlY3Q6bm9uZTt1c2VyLXNlbGVjdDpub25lO30uZGlmZi1kZWNvcmF0aW9uLWNvbnRlbnR7Zm9udC1mYW1pbHk6Q29uc29sYXMsQ291cmllcixtb25vc3BhY2U7Zm9udC1mYW1pbHk6dmFyKC0tZGlmZi1mb250LWZhbWlseSk7cGFkZGluZzowO31cbiJdLCJzb3VyY2VSb290IjoiIn0= */</style><style id="detectElementResize" type="text/css">@keyframes resizeanim { from { opacity: 0; } to { opacity: 0; } } .resize-triggers { animation: 1ms resizeanim; visibility: hidden; opacity: 0; } .resize-triggers, .resize-triggers > div, .contract-trigger:before { content: " "; display: block; position: absolute; top: 0; left: 0; height: 100%; width: 100%; overflow: hidden; z-index: -1; } .resize-triggers > div { background: #eee; overflow: auto; } .contract-trigger:before { width: 200%; height: 200%; }</style><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-add:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eb0a'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-close:before { content: '\ea76'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.monaco-editor .findOptionsWidget { background-color: #f3f3f3; }
.monaco-editor .findOptionsWidget { color: #616161; }
.monaco-editor .findOptionsWidget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .on-type-rename-decoration { background: rgba(255, 0, 0, 0.3); border-left-color: rgba(255, 0, 0, 0.3); }
.monaco-editor, .monaco-editor-background, .monaco-editor .inputarea.ime-input { background-color: #fffffe; }
.monaco-editor, .monaco-editor .inputarea.ime-input { color: #000000; }
.monaco-editor .margin { background-color: #fffffe; }
.monaco-editor .rangeHighlight { background-color: rgba(253, 255, 0, 0.2); }
.monaco-editor .symbolHighlight { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .mtkw { color: rgba(51, 51, 51, 0.2) !important; }
.monaco-editor .mtkz { color: rgba(51, 51, 51, 0.2) !important; }
.monaco-editor .line-numbers { color: #237893; }
.monaco-editor .current-line ~ .line-numbers { color: #0b216f; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .lines-content .cigr { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .lines-content .cigra { box-shadow: 1px 0 0 0 #939393 inset; }
.monaco-editor .minimap-slider .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.2); }
.monaco-editor .minimap-slider:hover .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.35); }
.monaco-editor .minimap-slider.active .minimap-slider-horizontal { background: rgba(0, 0, 0, 0.3); }
.monaco-editor .minimap-shadow-visible { box-shadow: #dddddd -6px 0 6px -6px inset; }
.monaco-editor .view-ruler { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .scroll-decoration { box-shadow: #dddddd 0 6px 6px -6px inset; }
.monaco-editor .focused .selected-text { background-color: #add6ff; }
.monaco-editor .selected-text { background-color: #e5ebf1; }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e9a700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%2375beff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor.showDeprecated .squiggly-inline-deprecated { text-decoration: line-through; text-decoration-color: #000000}
.monaco-diff-editor .diff-review-line-number { color: #237893; }
.monaco-diff-editor .diff-review-shadow { box-shadow: #dddddd 0 -6px 6px -6px inset; }
.monaco-editor .line-insert, .monaco-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-diff-editor .line-insert, .monaco-diff-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .inline-added-margin-view-zone { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .line-delete, .monaco-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor .line-delete, .monaco-diff-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-editor .inline-deleted-margin-view-zone { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px -5px #dddddd; }

			.monaco-diff-editor .diffViewport {
				background: rgba(100, 100, 100, 0.4);
			}
		

			.monaco-diff-editor .diffViewport:hover {
				background: rgba(100, 100, 100, 0.7);
			}
		

			.monaco-diff-editor .diffViewport:active {
				background: rgba(0, 0, 0, 0.6);
			}
		

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	

.mtk1 { color: #000000; }
.mtk2 { color: #fffffe; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #383838; }
.mtk11 { color: #cd3131; }
.mtk12 { color: #863b00; }
.mtk13 { color: #af00db; }
.mtk14 { color: #800000; }
.mtk15 { color: #e00000; }
.mtk16 { color: #3030c0; }
.mtk17 { color: #666666; }
.mtk18 { color: #778899; }
.mtk19 { color: #ff00ff; }
.mtk20 { color: #a31515; }
.mtk21 { color: #4f76ac; }
.mtk22 { color: #008080; }
.mtk23 { color: #001188; }
.mtk24 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }</style><style>
div.tm-lang .mtk1 { color: #000000; }
div.tm-lang .mtk2 { color: #FFFFFF; }
div.tm-lang .mtk3 { color: #0451A5; }
div.tm-lang .mtk4 { color: #008000; }
div.tm-lang .mtk5 { color: #0000FF; }
div.tm-lang .mtk6 { color: #09885A; }
div.tm-lang .mtk7 { color: #811F3F; }
div.tm-lang .mtk8 { color: #800000; }
div.tm-lang .mtk9 { color: #FF0000; }
div.tm-lang .mtk10 { color: #CD3131; }
div.tm-lang .mtk11 { color: #000080; }
div.tm-lang .mtk12 { color: #A31515; }
div.tm-lang .mtki { font-style: italic; }
div.tm-lang .mtkb { font-weight: bold; }
div.tm-lang .mtku { text-decoration: underline; text-underline-position: under; }</style><link rel="prefetch" as="script" href="https://codeocean.com/rollbarReporter.216a37.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/auth.d09a90.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/virtual-list.ea4904.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/publisher-signup.7e58a3.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/dashboard.f63e57.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/peerReview.110152.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/explore.24eed6.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/ide.f22cc0.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/account.fb788b.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/admin.d73558.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/admin-join.0589d3.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/organization-page.c619e5.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/groups-page.ec43d4.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/datasets.744143.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/exampleCapsule.78f90f.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/recent-capsules.4c734b.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/dta-viewer.5601d0.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/excel-viewer.fb6e1f.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/csv-viewer.71065b.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/notebook-viewer.88db69.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/code-viewer.a2fcd1.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/log-container.0bf396.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-include-loader_node_modules_monaco-editor_esm_vs_editor_editor_api_js.b8e592.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_react-dnd-html5-backend_dist_esm_getEmptyImage_js-node_modules_react-dnd_dist_-14b1b4.e459e8.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_lodash__baseDifference_js-node_modules_lodash_fp_compact_js-node_modules_lodas-4d5294.8a4eea.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_lodash_differenceWith_js-node_modules_lodash_fp_flatMap_js-node_modules_lodash-796622.c1cc15.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_lodash_findKey_js-node_modules_vscode-oniguruma_release_main_js-node_modules_v-ba46e1.76c82d.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_lodash_find_js-node_modules_react-responsive_dist_react-responsive_js.9079f6.chunk.js"><link rel="prefetch" as="script" href="./mvla_files/v-node_modules_babel_runtime_helpers_esm_taggedTemplateLiteral_js-node_modules_axios_index_js-22565d.d96df6.js.download"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_file-selector_dist_es5_index_js-node_modules_js-yaml_dist_js-yaml_mjs-node_mod-4ef8e0.521225.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_katex_dist_contrib_auto-render_js-node_modules_katex_dist_katex_css.181157.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_rollbar_src_browser_core_js-node_modules_rollbar_src_browser_telemetry_js-node-b745e9.684d5a.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_xterm_css_xterm_css-node_modules_xterm-addon-fit_lib_xterm-addon-fit_js-node_m-22ee07.5b789d.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_react-image-crop_dist_ReactCrop_min_js-node_modules_react-image-crop_dist_Reac-2f1af7.ed4215.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/v-node_modules_dompurify_dist_purify_js-node_modules_marked_lib_marked_js.0433bb.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/packages_app_src_shared_modals_deleteConfirmation_index_tsx-packages_app_src_shared_modals_wa-267af4.33ebc2.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/packages_app_src_shared_SortedColumHeader_index_tsx-packages_components_src_foundation_Badge_-d96b9d.37fd67.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/packages_app_src_shared_peerReview_sagas_openInviteAuthorModal_ts-packages_app_src_shared_pee-cc1375.2b0749.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/packages_app_src_pages_admin_redux_index_ts-packages_app_src_pages_admin_sagas_index_ts.c55293.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/packages_app_src_shared_datasets_CreateDatasetBtn_index_tsx-packages_app_src_shared_datasets_-da7c46.80b99e.chunk.js"><link rel="prefetch" as="script" href="https://codeocean.com/packages_app_src_pages_teams_shared_MemberRowActions_RowActions_js-packages_app_src_pages_tea-2c6167.6cd1df.chunk.js"></head><body class="" style=""><div class="appWrapper"><div id="unsupportedBrowsers"></div><div id="codeoceanApp"><div><div direction="row" class="Flex-sc-10ouakr-0 Container-sc-61h8pz-0 doHqVb hQurca"><a class="RouterLink-sc-140uhv1-0 esDnnh" href="https://codeocean.com/dashboard"></a><div direction="column" class="Flex-sc-10ouakr-0 fdMhmd" style="min-width: 0px;"><div direction="row" class="Flex-sc-10ouakr-0 CapsuleDetails-sc-61h8pz-1 wEhBM hEMMPP"><div color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 Badge-sc-1kefzaj-0 ivGlbj fbqdlH kXIwzm jLdMHF"><svg data-test="co-AccessPrivate" size="1.2" class="SvgIcon-sc-13apni9-0 eASQYR dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M92.7 115.8H35.3a14.5 14.5 0 01-14.5-14.5V68.2a14.4 14.4 0 0112-14.2V43.2a31.1 31.1 0 0132.1-30.9c16.7.4 30.3 14.6 30.3 31.6V54a14.4 14.4 0 0112 14.2v33a14.6 14.6 0 01-14.5 14.6zM35.3 61.3a7 7 0 00-7.1 6.9v33.1a7 7 0 007.1 6.9h57.4a7 7 0 007.1-7v-33a7 7 0 00-7.1-6.9zm5-7.5h47.4v-9.9c0-13-10.3-23.8-23-24.1a23.4 23.4 0 00-17.2 6.7 23.1 23.1 0 00-7.2 16.7z"></path></svg> Private</div><div class="NameWrap-sc-9ibn0y-0 iXqJGj"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB bEjlxL IKVxD zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div class="DummyInput-hu10jk-1 iuKnpq"><span>Vishaka</span></div></div></div></div><div direction="row" class="Flex-sc-10ouakr-0 MenuAndStatus-p92jlx-0 UhuBA"><ul data-test="ide-menu" class="Root-sc-1w3m1gu-0 khfeaf"><li class="MenuItemContainer-sc-1w3m1gu-2 gGDuvt"><span>Capsule</span></li><li class="MenuItemContainer-sc-1w3m1gu-2 gGDuvt"><span>File</span></li><li class="MenuItemContainer-sc-1w3m1gu-2 gGDuvt"><span>Help</span></li></ul><div direction="row" class="Flex-sc-10ouakr-0 StatusContainer-ot7evd-0 jGPGHu hywGmB"><span class="Span-ot7evd-2 kqYwHc">All changes saved</span></div></div></div><div direction="row" class="Flex-sc-10ouakr-0 HeaderButtons-sc-61h8pz-2 fuXDFW cKqWjN"><button data-test="collaborate-button" color="primary" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH lhKrnT"><svg data-test="co-Share" size="1.5" stroke-width="0" class="SvgIcon-sc-13apni9-0 cbeyPJ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M93.6 115.8a21 21 0 01-20.9-21 19.6 19.6 0 01.9-5.9L50.8 77a20.9 20.9 0 11-16.4-33.9 20.7 20.7 0 0116.5 8.2l22.8-11.9a18.7 18.7 0 01-1-6.2A20.9 20.9 0 1177.1 46L54.4 57.9a20.5 20.5 0 01.9 6.1 22.5 22.5 0 01-1 6.4L77 82.2a20.9 20.9 0 1116.6 33.6zm0-34.4A13.4 13.4 0 10107 94.8a13.5 13.5 0 00-13.4-13.4zM34.4 50.6A13.4 13.4 0 1047.8 64a13.4 13.4 0 00-13.4-13.4zm59.2-30.8A13.4 13.4 0 10107 33.2a13.4 13.4 0 00-13.4-13.4z"></path></svg><span>Share</span></button></div><div class="MenuMargin-sc-1uljm0-0 hvbCym"><div><button color="primary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gZcoeQ sc-4y585q-0 MenuDropdown-sc-1uljm0-1 cWGzON fJYfYW" type="button"><div data-test="profile-icon" class="ProfileIcon-sc-1uljm0-4 emELyc"></div></button></div></div></div><div class="LayoutContainer-djse1m-0 hnjdZm"><div class="TabsContainer-sc-1j51uwg-2 cUmjgW"><ul class="TabsList-sc-1j51uwg-0 cxexBw"><li data-test="ide-side-tab" class="TabButton-sc-1j51uwg-1 bLMNzx">Files</li><li data-test="ide-side-tab" class="TabButton-sc-1j51uwg-1 fcWXtv">App Panel</li><li data-test="ide-side-tab" class="TabButton-sc-1j51uwg-1 fcWXtv">Tabs</li></ul></div><div class="PanelsContainer-djse1m-1 dcESIC"><div class="SplitPane PaneContainer-sc-1oi00eg-0 hsxbrs vertical " style="display: flex; flex: 1 1 0%; height: initial; position: absolute; outline: none; overflow: hidden; user-select: text; inset: 0px; flex-direction: row;"><div class="Pane vertical Pane1  " style="flex: 0 0 auto; position: relative; outline: none; width: 50px; min-width: 30rem;"><div class="EdgePanel-sc-8kz175-0 bhaYhi"><div><div direction="column" data-test="ide-file-browser" class="Flex-sc-10ouakr-0 FileBrowserContainer-sc-1e4j3h3-0 izNRpz"><div class="ToolbarStyle-sc-1df6uu1-0 eyJUsi"><div direction="row" class="Flex-sc-10ouakr-0 jkUzJL"><button color="info" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH lnTSxa sc-192dixh-0 ljYVxy" data-analytics="[&quot;Click toolbar - Create Blank File&quot;,{&quot;category&quot;:&quot;Capsule&quot;,&quot;capsuleId&quot;:&quot;e40b6e27-34bb-469e-86ed-d9d87880e11b&quot;}]" type="button"><svg data-test="co-JpAdd" size="1.5" stroke-width="0" class="SvgIcon-sc-13apni9-0 cbeyPJ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M116.1 72h-45v44h-14V72h-45V57h44V12h15v45h45z"></path></svg></button><button color="info" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH lnTSxa sc-192dixh-0 ljYVxy" data-analytics="[&quot;Click toolbar - Create New Folder&quot;,{&quot;category&quot;:&quot;Capsule&quot;,&quot;capsuleId&quot;:&quot;e40b6e27-34bb-469e-86ed-d9d87880e11b&quot;}]" type="button"><svg data-test="co-JpNewFolder" size="1.5" stroke-width="0" class="SvgIcon-sc-13apni9-0 cbeyPJ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M115.8 25h-52l-13-13h-39a13 13 0 00-13 13v78a13 13 0 0013 13h104a13 13 0 0013-13V38a13 13 0 00-13-13zm-23 54h-22v22h-13V79h-22V66h22V44h13v22h22z"></path></svg></button><button color="info" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH lnTSxa sc-192dixh-0 ljYVxy" data-analytics="[&quot;Click toolbar - Upload Files&quot;,{&quot;category&quot;:&quot;Capsule&quot;,&quot;capsuleId&quot;:&quot;e40b6e27-34bb-469e-86ed-d9d87880e11b&quot;}]" type="button"><svg data-test="co-JpUpload" size="1.5" stroke-width="0" class="SvgIcon-sc-13apni9-0 cbeyPJ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M50.5 75h29V45h19.3L64.7 11.1 31.2 45h19.3zm-20 13h68v13h-68z"></path></svg></button><button color="info" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH lnTSxa sc-192dixh-0 ljYVxy" data-analytics="[&quot;Click toolbar - Delete Files / Folders&quot;,{&quot;category&quot;:&quot;Capsule&quot;,&quot;capsuleId&quot;:&quot;e40b6e27-34bb-469e-86ed-d9d87880e11b&quot;}]" type="button"><svg data-test="co-Delete" size="1.5" stroke-width="0" class="SvgIcon-sc-13apni9-0 cbeyPJ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M107.5 27h-19l-.5-4.2A11 11 0 0077.1 12H50.9A11 11 0 0040 22.8l-.5 4.2h-19v8h5v65a16 16 0 0016 16h45a16 16 0 0016-16V35h5zm-60.8-3.6v-.5a2.9 2.9 0 012.9-2.9H78a2.9 2.9 0 012.8 2.9l.5 4.1h-35zM86.9 107H41.1a7.6 7.6 0 01-7.6-7.6V35h61v64.4a7.6 7.6 0 01-7.6 7.6z"></path><path d="M43.5 48h8v46h-8zM59.5 48h8v46h-8zM75.5 48h8v46h-8z"></path></svg></button></div></div><div class="FileBrowserDropContainer-sc-1e4j3h3-2 gEeRoY" data-path=""><div direction="column" class="Flex-sc-10ouakr-0 StickyContainer-sc-72zn3w-1 eQMAGl dOkIGY"><div class="Flexible-sc-10ouakr-3 Flexible-sc-10ouakr-2 Flexible-sc-10ouakr-1 TreeContainer-sc-17cxd90-0 clBbhm iQaRGQ gjDCFT chBBSV SelectableVirtualTree-sc-1e4j3h3-1 fSSjHA"><div style="overflow: visible; height: 0px; width: 0px;"><div aria-label="grid" aria-readonly="true" class="ReactVirtualized__Grid ReactVirtualized__List navigatedListClass" id="virtual-tree-list-6d689115-9ee4-449e-806e-3aed5e950654" role="grid" tabindex="0" style="box-sizing: border-box; direction: ltr; height: 591px; position: relative; width: 299px; will-change: transform; overflow: hidden;"><div class="ReactVirtualized__Grid__innerScrollContainer" role="rowgroup" style="width: auto; height: 330px; max-width: 299px; max-height: 330px; overflow: hidden; position: relative;"><header class="sc-10h9f64-0 bredol" style="height: 22px; left: 0px; position: absolute; top: 0px; width: 100%;">Core Files <div color="info" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp jdeYfZ sc-2cfrir-2 fktUiV"><span></span> <svg data-test="co-Question" size="1" stroke-width="0" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 115.75A51.75 51.75 0 11115.75 64 51.8 51.8 0 0164 115.75zm0-96A44.25 44.25 0 10108.25 64 44.3 44.3 0 0064 19.75zm3.75 75.18h-7.5v-8.25h7.5zm0-13.4h-7.5v-5.69a18 18 0 017.32-14.52 4.52 4.52 0 01.53-.43 10.53 10.53 0 10-14-15.41l-5.8-4.76a18 18 0 1124.63 26 3.6 3.6 0 01-.52.43 10.52 10.52 0 00-4.63 8.73v5.69z"></path></svg></div></header><div tabindex="0" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 howMsG bQKcrs" data-path="metadata" data-open="false" style="height: 22px; left: 0px; position: absolute; top: 22px; width: 100%;"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><div class="p1rkmd-0 jKEFgu FolderToggle-sc-1olbryb-0 hDxpCt"><svg data-test="co-Arrow" class="SvgIcon-sc-13apni9-0 rcyBm dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M28.3 12a10.1 10.1 0 00-5.6 1.6 11 11 0 00-5.6 9.7v81.4a11.2 11.2 0 005.6 9.7 10.1 10.1 0 005.6 1.6 10.4 10.4 0 005.6-1.6l70.4-40.6a11.3 11.3 0 005.6-9.8 11.5 11.5 0 00-5.6-9.8L33.9 13.6a10.4 10.4 0 00-5.6-1.6z"></path></svg></div><svg data-test="co-Metadata" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M92.2 104.4H12.3C5.5 104.4 0 97.8 0 89.7V38.3c0-8.1 5.5-14.7 12.3-14.7h79.9A10.9 10.9 0 0199 26a4.7 4.7 0 011 1l26.7 33.2a6.3 6.3 0 010 7.6L100 101a4.7 4.7 0 01-1 1 10.9 10.9 0 01-6.8 2.4zM12.3 31c-2.6 0-4.9 3.4-4.9 7.3v51.4c0 3.9 2.3 7.3 4.9 7.3h79.9a4 4 0 002.1-.7L120.2 64 94.3 31.7a4 4 0 00-2.1-.7zm76.6 47.1a14.1 14.1 0 1114-14.1 14.1 14.1 0 01-14 14.1zm0-20.8a6.7 6.7 0 106.6 6.7 6.7 6.7 0 00-6.6-6.7zM64.5 77.1H18.4v-7.4h46.1zm0-18.8H18.4v-7.4h46.1z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">metadata</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">67 B</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-CheckFull" class="SvgIcon-sc-13apni9-0 wDRPs Tracked-a81g04-0 juQUPY" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div><div tabindex="0" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 howMsG bQKcrs" data-path="environment" data-open="false" style="height: 22px; left: 0px; position: absolute; top: 44px; width: 100%;"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><div class="p1rkmd-0 jKEFgu FolderToggle-sc-1olbryb-0 hDxpCt"><svg data-test="co-Arrow" class="SvgIcon-sc-13apni9-0 rcyBm dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M28.3 12a10.1 10.1 0 00-5.6 1.6 11 11 0 00-5.6 9.7v81.4a11.2 11.2 0 005.6 9.7 10.1 10.1 0 005.6 1.6 10.4 10.4 0 005.6-1.6l70.4-40.6a11.3 11.3 0 005.6-9.8 11.5 11.5 0 00-5.6-9.8L33.9 13.6a10.4 10.4 0 00-5.6-1.6z"></path></svg></div><svg data-test="co-Cog" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M46.1 115.8a13.2 13.2 0 01-6.3-1.7l-7.1-4.2A12.2 12.2 0 0128.1 93l2.9-5.1a40.7 40.7 0 01-4.2-7.4h-6A12.5 12.5 0 018.4 68.1v-8.2a12.5 12.5 0 0112.4-12.4h6a45 45 0 014.3-7.3l-3-5.1a12.2 12.2 0 01-1.2-9.5 12.3 12.3 0 015.8-7.6l7.1-4.1a12.3 12.3 0 019.4-1.2 11.8 11.8 0 017.6 5.8l2.9 5.1a40.3 40.3 0 018.5 0l3-5.1a12.4 12.4 0 0117-4.6l7.1 4.2A12.2 12.2 0 0199.9 35L97 40.1a40.7 40.7 0 014.2 7.4h6a12.7 12.7 0 018.9 3.8 12.4 12.4 0 013.5 9v8a12.5 12.5 0 01-12.4 12.4h-6A47.7 47.7 0 0197 88l3 4.9a12.6 12.6 0 011.3 9.5 12.8 12.8 0 01-5.9 7.6l-7.1 4.1a12.3 12.3 0 01-9.4 1.2 12 12 0 01-7.6-5.8l-2.9-5.1a42.2 42.2 0 01-8.7 0l-2.9 5.1a12.4 12.4 0 01-10.7 6.3zm26.2-19.6l5.5 9.5a5.1 5.1 0 003 2.4 5.6 5.6 0 003.8-.5l7.1-4.1a4.9 4.9 0 002.3-3 4.6 4.6 0 00-.5-3.8l-5.7-9.3 1.7-2.1a33.9 33.9 0 005.7-9.7l.9-2.4h11.1a4.9 4.9 0 004.9-4.9v-8.1a5.3 5.3 0 00-1.4-3.7 4.9 4.9 0 00-3.5-1.5H96.1l-.9-2.4a30 30 0 00-5.6-9.6l-1.8-2 5.6-9.7a5.1 5.1 0 00.5-3.8 4.8 4.8 0 00-2.3-2.9l-7.1-4.2a5 5 0 00-6.8 1.8l-5.5 9.6-2.6-.4a30.7 30.7 0 00-11.3 0l-2.6.4-5.4-9.6a5.3 5.3 0 00-3-2.3 5.6 5.6 0 00-3.8.5l-7.1 4.1a5.2 5.2 0 00-2.3 3 5 5 0 00.5 3.8l5.5 9.6-1.6 2a35.3 35.3 0 00-5.7 9.7l-.9 2.4H20.8a4.9 4.9 0 00-4.9 4.9v8.2a4.9 4.9 0 004.9 4.9h11.1l.9 2.4a30 30 0 005.6 9.6l1.8 2-5.6 9.7a5.1 5.1 0 00-.5 3.8 4.4 4.4 0 002.3 2.9l7.1 4.2a5 5 0 006.8-1.8l5.5-9.6 2.6.4a30.7 30.7 0 0011.3 0zm-8.2-14.4a17.6 17.6 0 1117.5-17.6 17.6 17.6 0 01-17.5 17.6zm0-27.7a10.1 10.1 0 1010 10.1 10.1 10.1 0 00-10-10.1z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">environment</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">309 B</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-CheckFull" class="SvgIcon-sc-13apni9-0 wDRPs Tracked-a81g04-0 juQUPY" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div><div tabindex="0" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 howMsG bQKcrs" data-path="code" data-open="true" style="height: 22px; left: 0px; position: absolute; top: 66px; width: 100%;"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><div class="p1rkmd-0 hqlnGZ FolderToggle-sc-1olbryb-0 hDxpCt"><svg data-test="co-Arrow" open="" class="SvgIcon-sc-13apni9-0 rcyBm dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M28.3 12a10.1 10.1 0 00-5.6 1.6 11 11 0 00-5.6 9.7v81.4a11.2 11.2 0 005.6 9.7 10.1 10.1 0 005.6 1.6 10.4 10.4 0 005.6-1.6l70.4-40.6a11.3 11.3 0 005.6-9.8 11.5 11.5 0 00-5.6-9.8L33.9 13.6a10.4 10.4 0 00-5.6-1.6z"></path></svg></div><svg data-test="co-JpDirectory" fill="#616262" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M110.2 25H73.5a6.6 6.6 0 01-4.7-1.8l-9.5-9.5-.8-.6a4.6 4.6 0 00-2.6-1H18a6.3 6.3 0 00-5.9 5.9v91.6a6.5 6.5 0 006.5 6.5h91a6.6 6.6 0 006.5-6.5l.6-78a6.6 6.6 0 00-6.5-6.6zm-3.6 82H20.1V44h87z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">code</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">486.68 KB</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-EllipsisFull" class="SvgIcon-sc-13apni9-0 ctkRGu Modified-a81g04-3 ediivM" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 52 52 0 00-52-52zM33 72a8 8 0 118-8 8 8 0 01-8 8zm31 0a8 8 0 118-8 8 8 0 01-8 8zm31 0a8 8 0 118-8 8 8 0 01-8 8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div><div tabindex="0" class="DragContainer-sc-1uzndug-2 kCzTVX fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 88px; width: 100%;"><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 cBDKFr eCOPCK" data-path="code/AM_HELP.alp" draggable="true"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><svg data-test="co-JpFile" fill="#757575" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M101.9 115.8H26.1c-7.6 0-13.9-5.3-13.9-11.8V24c0-6.5 6.3-11.8 13.9-11.8h48.6a8.8 8.8 0 015.1 1.8l.3.3 33.2 33a6.4 6.4 0 012.5 5V104c0 6.5-6.3 11.8-13.9 11.8zm-75.8-96c-3.4 0-6.3 1.9-6.3 4.2v80c0 2.3 2.9 4.2 6.3 4.2h75.8c3.4 0 6.3-1.9 6.3-4.2V59H80.6a11 11 0 01-11.2-10.8V19.8zm50.8 1.9v26.5a3.6 3.6 0 003.7 3.3h26.3z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">AM_HELP.alp</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">451.44 KB</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-EllipsisFull" class="SvgIcon-sc-13apni9-0 ctkRGu Modified-a81g04-3 ediivM" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 52 52 0 00-52-52zM33 72a8 8 0 118-8 8 8 0 01-8 8zm31 0a8 8 0 118-8 8 8 0 01-8 8zm31 0a8 8 0 118-8 8 8 0 01-8 8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div><div tabindex="0" class="DragContainer-sc-1uzndug-2 kCzTVX fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 110px; width: 100%;"><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 cBDKFr eCOPCK" data-path="code/LICENSE" draggable="true"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><svg data-test="co-JpFile" fill="#757575" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M101.9 115.8H26.1c-7.6 0-13.9-5.3-13.9-11.8V24c0-6.5 6.3-11.8 13.9-11.8h48.6a8.8 8.8 0 015.1 1.8l.3.3 33.2 33a6.4 6.4 0 012.5 5V104c0 6.5-6.3 11.8-13.9 11.8zm-75.8-96c-3.4 0-6.3 1.9-6.3 4.2v80c0 2.3 2.9 4.2 6.3 4.2h75.8c3.4 0 6.3-1.9 6.3-4.2V59H80.6a11 11 0 01-11.2-10.8V19.8zm50.8 1.9v26.5a3.6 3.6 0 003.7 3.3h26.3z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">LICENSE</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">7.47 KB</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-CheckFull" class="SvgIcon-sc-13apni9-0 wDRPs Tracked-a81g04-0 juQUPY" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div><div tabindex="0" class="DragContainer-sc-1uzndug-2 kCzTVX fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 132px; width: 100%;"><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 cBDKFr eCOPCK" data-path="code/run" draggable="true"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><svg data-test="co-Start" size="1.1" class="SvgIcon-sc-13apni9-0 hUkFZl RunIcon-tvvwt1-0 jytFxR" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M53.7 52l-13.5 2.4-2.4-13.6 13.5-2.4zm16.1 11.3l-2.4-13.6-13.6 2.4 2.4 13.6zM34.2 86.1l4.8 27.4-11.7 2.1L12 28.9l11.7-2.1 81.8-14.4L116 71.7zm-1-4.4l11.2-2-2-11.2L56.1 66l2 11.2 13.7-2.4-2-11.2 13.7-2.5 1.9 11.2 13.7-2.4-2-11.3 11.3-1.9-2.5-13.7-11.2 2-2.5-13.7 11.2-2-1.7-11.4-11.2 1.9 2 11.2-13.7 2.5-2-11.2-13.7 2.5 2 11.2-13.7 2.4-1.9-11.2-13.7 2.5 2 11.2-11.3 2L29 56.5l11.1-2 2.5 13.6-11.3 2zM81 47.2l-2.4-13.6L65 36l2.4 13.6zm16 11.3l-2.4-13.6L81 47.3l2.4 13.6z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">run</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">295 B</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-EllipsisFull" class="SvgIcon-sc-13apni9-0 ctkRGu Modified-a81g04-3 ediivM" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 52 52 0 00-52-52zM33 72a8 8 0 118-8 8 8 0 01-8 8zm31 0a8 8 0 118-8 8 8 0 01-8 8zm31 0a8 8 0 118-8 8 8 0 01-8 8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div><div tabindex="0" class="DragContainer-sc-1uzndug-2 kCzTVX fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 154px; width: 100%;"><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 cBDKFr CCbEf" data-path="code/untitled" draggable="true"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><svg data-test="co-JpFile" fill="#757575" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M101.9 115.8H26.1c-7.6 0-13.9-5.3-13.9-11.8V24c0-6.5 6.3-11.8 13.9-11.8h48.6a8.8 8.8 0 015.1 1.8l.3.3 33.2 33a6.4 6.4 0 012.5 5V104c0 6.5-6.3 11.8-13.9 11.8zm-75.8-96c-3.4 0-6.3 1.9-6.3 4.2v80c0 2.3 2.9 4.2 6.3 4.2h75.8c3.4 0 6.3-1.9 6.3-4.2V59H80.6a11 11 0 01-11.2-10.8V19.8zm50.8 1.9v26.5a3.6 3.6 0 003.7 3.3h26.3z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">untitled</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">27.47 KB</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-EllipsisFull" class="SvgIcon-sc-13apni9-0 ctkRGu Modified-a81g04-3 ediivM" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 52 52 0 00-52-52zM33 72a8 8 0 118-8 8 8 0 01-8 8zm31 0a8 8 0 118-8 8 8 0 01-8 8zm31 0a8 8 0 118-8 8 8 0 01-8 8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div><div tabindex="0" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 howMsG bQKcrs" data-path="data" data-open="true" style="height: 22px; left: 0px; position: absolute; top: 176px; width: 100%;"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><div class="p1rkmd-0 hqlnGZ FolderToggle-sc-1olbryb-0 hDxpCt"><svg data-test="co-Arrow" open="" class="SvgIcon-sc-13apni9-0 rcyBm dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M28.3 12a10.1 10.1 0 00-5.6 1.6 11 11 0 00-5.6 9.7v81.4a11.2 11.2 0 005.6 9.7 10.1 10.1 0 005.6 1.6 10.4 10.4 0 005.6-1.6l70.4-40.6a11.3 11.3 0 005.6-9.8 11.5 11.5 0 00-5.6-9.8L33.9 13.6a10.4 10.4 0 00-5.6-1.6z"></path></svg></div><svg data-test="co-JpDirectory" fill="#616262" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M110.2 25H73.5a6.6 6.6 0 01-4.7-1.8l-9.5-9.5-.8-.6a4.6 4.6 0 00-2.6-1H18a6.3 6.3 0 00-5.9 5.9v91.6a6.5 6.5 0 006.5 6.5h91a6.6 6.6 0 006.5-6.5l.6-78a6.6 6.6 0 00-6.5-6.6zm-3.6 82H20.1V44h87z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">data</div><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ManageDatasetsButton-mo6o39-0 ivGlbj fbqdlH gZcoeQ kXsZwC TREE_NODE_STOP_CLICK" color="primary" type="button">Manage Datasets</button></div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">0 B</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-CheckFull" class="SvgIcon-sc-13apni9-0 wDRPs Tracked-a81g04-0 juQUPY" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div><header class="sc-10h9f64-0 bredol" style="height: 22px; left: 0px; position: absolute; top: 198px; width: 100%;">Results <div color="info" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp jdeYfZ sc-2cfrir-2 fktUiV"><span></span> <svg data-test="co-Question" size="1" stroke-width="0" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 115.75A51.75 51.75 0 11115.75 64 51.8 51.8 0 0164 115.75zm0-96A44.25 44.25 0 10108.25 64 44.3 44.3 0 0064 19.75zm3.75 75.18h-7.5v-8.25h7.5zm0-13.4h-7.5v-5.69a18 18 0 017.32-14.52 4.52 4.52 0 01.53-.43 10.53 10.53 0 10-14-15.41l-5.8-4.76a18 18 0 1124.63 26 3.6 3.6 0 01-.52.43 10.52 10.52 0 00-4.63 8.73v5.69z"></path></svg></div></header><div tabindex="0" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 howMsG bQKcrs" data-path="results" data-open="false" style="height: 22px; left: 0px; position: absolute; top: 220px; width: 100%;"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><div class="p1rkmd-0 jKEFgu FolderToggle-sc-1olbryb-0 hDxpCt"><svg data-test="co-Arrow" class="SvgIcon-sc-13apni9-0 rcyBm dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M28.3 12a10.1 10.1 0 00-5.6 1.6 11 11 0 00-5.6 9.7v81.4a11.2 11.2 0 005.6 9.7 10.1 10.1 0 005.6 1.6 10.4 10.4 0 005.6-1.6l70.4-40.6a11.3 11.3 0 005.6-9.8 11.5 11.5 0 00-5.6-9.8L33.9 13.6a10.4 10.4 0 00-5.6-1.6z"></path></svg></div><svg data-test="co-Result" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M99.6 115.8H28.2c-7.3 0-13.2-5.3-13.2-11.8V24c0-6.5 5.9-11.8 13.2-11.8h48a7.8 7.8 0 015 1.9l29.1 24.7a6.2 6.2 0 012.5 5.1V104c0 6.5-5.9 11.8-13.2 11.8zm-77.1-11.5c.2 2.2 2.7 3.9 5.7 3.9h71.4c3.1 0 5.7-1.9 5.7-4.2V59.9l-37 37-19.2-19.1zm5.7-84.5c-3.1 0-5.7 1.9-5.7 4.2v69.7l26.6-26.5 19.2 19.1 33.8-33.8H81a9.6 9.6 0 01-9.5-9.6V19.8zM79 22v20.9a2 2 0 002 2.1h24.3v-.6z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">results</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">2.71 KB</span><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div><header class="sc-10h9f64-0 bredol" style="height: 22px; left: 0px; position: absolute; top: 242px; width: 100%;">Other Files <div color="info" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp jdeYfZ sc-2cfrir-2 fktUiV"><span></span> <svg data-test="co-Question" size="1" stroke-width="0" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 115.75A51.75 51.75 0 11115.75 64 51.8 51.8 0 0164 115.75zm0-96A44.25 44.25 0 10108.25 64 44.3 44.3 0 0064 19.75zm3.75 75.18h-7.5v-8.25h7.5zm0-13.4h-7.5v-5.69a18 18 0 017.32-14.52 4.52 4.52 0 01.53-.43 10.53 10.53 0 10-14-15.41l-5.8-4.76a18 18 0 1124.63 26 3.6 3.6 0 01-.52.43 10.52 10.52 0 00-4.63 8.73v5.69z"></path></svg></div></header><div tabindex="0" class="DragContainer-sc-1uzndug-2 kCzTVX fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 264px; width: 100%;"><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 howMsG bQKcrs" data-path="3d" data-open="false" draggable="true"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><div class="p1rkmd-0 jKEFgu FolderToggle-sc-1olbryb-0 hDxpCt"><svg data-test="co-Arrow" class="SvgIcon-sc-13apni9-0 rcyBm dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M28.3 12a10.1 10.1 0 00-5.6 1.6 11 11 0 00-5.6 9.7v81.4a11.2 11.2 0 005.6 9.7 10.1 10.1 0 005.6 1.6 10.4 10.4 0 005.6-1.6l70.4-40.6a11.3 11.3 0 005.6-9.8 11.5 11.5 0 00-5.6-9.8L33.9 13.6a10.4 10.4 0 00-5.6-1.6z"></path></svg></div><svg data-test="co-JpDirectory" fill="#616262" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M110.2 25H73.5a6.6 6.6 0 01-4.7-1.8l-9.5-9.5-.8-.6a4.6 4.6 0 00-2.6-1H18a6.3 6.3 0 00-5.9 5.9v91.6a6.5 6.5 0 006.5 6.5h91a6.6 6.6 0 006.5-6.5l.6-78a6.6 6.6 0 00-6.5-6.6zm-3.6 82H20.1V44h87z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">3d</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">42.44 KB</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-CheckFull" class="SvgIcon-sc-13apni9-0 wDRPs Tracked-a81g04-0 juQUPY" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div><div tabindex="0" class="DragContainer-sc-1uzndug-2 kCzTVX fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 286px; width: 100%;"><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 howMsG bQKcrs" data-path="database" data-open="false" draggable="true"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><div class="p1rkmd-0 jKEFgu FolderToggle-sc-1olbryb-0 hDxpCt"><svg data-test="co-Arrow" class="SvgIcon-sc-13apni9-0 rcyBm dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M28.3 12a10.1 10.1 0 00-5.6 1.6 11 11 0 00-5.6 9.7v81.4a11.2 11.2 0 005.6 9.7 10.1 10.1 0 005.6 1.6 10.4 10.4 0 005.6-1.6l70.4-40.6a11.3 11.3 0 005.6-9.8 11.5 11.5 0 00-5.6-9.8L33.9 13.6a10.4 10.4 0 00-5.6-1.6z"></path></svg></div><svg data-test="co-JpDirectory" fill="#616262" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M110.2 25H73.5a6.6 6.6 0 01-4.7-1.8l-9.5-9.5-.8-.6a4.6 4.6 0 00-2.6-1H18a6.3 6.3 0 00-5.9 5.9v91.6a6.5 6.5 0 006.5 6.5h91a6.6 6.6 0 006.5-6.5l.6-78a6.6 6.6 0 00-6.5-6.6zm-3.6 82H20.1V44h87z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">database</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">258.43 KB</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-CheckFull" class="SvgIcon-sc-13apni9-0 wDRPs Tracked-a81g04-0 juQUPY" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div><div tabindex="0" class="DragContainer-sc-1uzndug-2 kCzTVX fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 308px; width: 100%;"><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 sPNsn eCOPCK" data-path="AM_HELP.alp" draggable="true"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><svg data-test="co-JpFile" fill="#757575" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M101.9 115.8H26.1c-7.6 0-13.9-5.3-13.9-11.8V24c0-6.5 6.3-11.8 13.9-11.8h48.6a8.8 8.8 0 015.1 1.8l.3.3 33.2 33a6.4 6.4 0 012.5 5V104c0 6.5-6.3 11.8-13.9 11.8zm-75.8-96c-3.4 0-6.3 1.9-6.3 4.2v80c0 2.3 2.9 4.2 6.3 4.2h75.8c3.4 0 6.3-1.9 6.3-4.2V59H80.6a11 11 0 01-11.2-10.8V19.8zm50.8 1.9v26.5a3.6 3.6 0 003.7 3.3h26.3z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">AM_HELP.alp</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">439.63 KB</span><div class="Status-f0f658-1 ioMRvP"><svg data-test="co-CheckFull" class="SvgIcon-sc-13apni9-0 wDRPs Tracked-a81g04-0 juQUPY" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg></div><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div></div></div></div><div class="resize-triggers"><div class="expand-trigger"><div style="width: 300px; height: 600px;"></div></div><div class="contract-trigger"></div></div></div></div></div></div></div></div></div><span role="presentation" class="Resizer vertical "></span><div class="Pane vertical Pane2  " style="flex: 1 1 0%; position: relative; outline: none;"><div class="SplitPane PaneContainer-sc-1oi00eg-0 hsxbrs vertical " style="display: flex; flex: 1 1 0%; height: initial; position: absolute; outline: none; overflow: hidden; user-select: text; inset: 0px; flex-direction: row;"><div class="Pane vertical Pane1  " style="flex: 1 1 0%; position: relative; outline: none; min-width: 5rem;"><div class="SplitPane PaneContainer-sc-1oi00eg-0 hsxbrs CenterEditor-sc-15six7i-1 cJMKTj vertical " style="display: flex; flex: 1 1 0%; height: initial; position: absolute; outline: none; overflow: hidden; user-select: text; inset: 0px; flex-direction: row;"><div class="Pane vertical Pane1  " style="flex: 1 1 0%; position: relative; outline: none; min-width: 5rem;"><div class="Flex-sc-10ouakr-0 Container-sc-4kyrt4-0 dYsnoi iOEmLy" direction="column"><ul class="Tabs-sc-4kyrt4-4 kkqCII"><li data-test="ide-tab" class="TabButton-sc-4kyrt4-6 ihrwTX" draggable="true"><div direction="row" class="Flex-sc-10ouakr-0 TabItem-sc-4kyrt4-5 doHqVb iZNxCA"><svg data-test="co-Cog" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M46.1 115.8a13.2 13.2 0 01-6.3-1.7l-7.1-4.2A12.2 12.2 0 0128.1 93l2.9-5.1a40.7 40.7 0 01-4.2-7.4h-6A12.5 12.5 0 018.4 68.1v-8.2a12.5 12.5 0 0112.4-12.4h6a45 45 0 014.3-7.3l-3-5.1a12.2 12.2 0 01-1.2-9.5 12.3 12.3 0 015.8-7.6l7.1-4.1a12.3 12.3 0 019.4-1.2 11.8 11.8 0 017.6 5.8l2.9 5.1a40.3 40.3 0 018.5 0l3-5.1a12.4 12.4 0 0117-4.6l7.1 4.2A12.2 12.2 0 0199.9 35L97 40.1a40.7 40.7 0 014.2 7.4h6a12.7 12.7 0 018.9 3.8 12.4 12.4 0 013.5 9v8a12.5 12.5 0 01-12.4 12.4h-6A47.7 47.7 0 0197 88l3 4.9a12.6 12.6 0 011.3 9.5 12.8 12.8 0 01-5.9 7.6l-7.1 4.1a12.3 12.3 0 01-9.4 1.2 12 12 0 01-7.6-5.8l-2.9-5.1a42.2 42.2 0 01-8.7 0l-2.9 5.1a12.4 12.4 0 01-10.7 6.3zm26.2-19.6l5.5 9.5a5.1 5.1 0 003 2.4 5.6 5.6 0 003.8-.5l7.1-4.1a4.9 4.9 0 002.3-3 4.6 4.6 0 00-.5-3.8l-5.7-9.3 1.7-2.1a33.9 33.9 0 005.7-9.7l.9-2.4h11.1a4.9 4.9 0 004.9-4.9v-8.1a5.3 5.3 0 00-1.4-3.7 4.9 4.9 0 00-3.5-1.5H96.1l-.9-2.4a30 30 0 00-5.6-9.6l-1.8-2 5.6-9.7a5.1 5.1 0 00.5-3.8 4.8 4.8 0 00-2.3-2.9l-7.1-4.2a5 5 0 00-6.8 1.8l-5.5 9.6-2.6-.4a30.7 30.7 0 00-11.3 0l-2.6.4-5.4-9.6a5.3 5.3 0 00-3-2.3 5.6 5.6 0 00-3.8.5l-7.1 4.1a5.2 5.2 0 00-2.3 3 5 5 0 00.5 3.8l5.5 9.6-1.6 2a35.3 35.3 0 00-5.7 9.7l-.9 2.4H20.8a4.9 4.9 0 00-4.9 4.9v8.2a4.9 4.9 0 004.9 4.9h11.1l.9 2.4a30 30 0 005.6 9.6l1.8 2-5.6 9.7a5.1 5.1 0 00-.5 3.8 4.4 4.4 0 002.3 2.9l7.1 4.2a5 5 0 006.8-1.8l5.5-9.6 2.6.4a30.7 30.7 0 0011.3 0zm-8.2-14.4a17.6 17.6 0 1117.5-17.6 17.6 17.6 0 01-17.5 17.6zm0-27.7a10.1 10.1 0 1010 10.1 10.1 10.1 0 00-10-10.1z"></path></svg><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 Title-sc-4kyrt4-7 kRsLfZ kspcUv">Environment</span><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gZcoeQ StyledCloseButton-sc-13clwi6-0 dmjmoz" type="button" color="primary"><svg data-test="co-Close" stroke-width="10" size="1" class="SvgIcon-sc-13apni9-0 joedTZ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M102.3 107.7L65 70.3l-37.3 37.4-5.4-5.4L59.7 65 22.3 27.7l5.4-5.4L65 59.7l37.3-37.4 5.4 5.4L70.3 65l37.4 37.3-5.4 5.4z"></path></svg></button></div></li><li title="Name: AM_HELP.alp
Path: /AM_HELP.alp" data-test="ide-tab" class="TabButton-sc-4kyrt4-6 ihrwTX" draggable="true"><div direction="row" class="Flex-sc-10ouakr-0 TabItem-sc-4kyrt4-5 doHqVb iZNxCA"><svg data-test="co-File" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M94.3 115.8H33.7a12 12 0 01-11.9-11.9V24.1a12 12 0 0111.9-11.9h40.7a7.2 7.2 0 014.8 2L104.1 39a7.1 7.1 0 012.1 4.9v60a12 12 0 01-11.9 11.9zm-60.6-96a4.4 4.4 0 00-4.4 4.3v79.8a4.4 4.4 0 004.4 4.3h60.6a4.4 4.4 0 004.4-4.3V48H78a8.7 8.7 0 01-8.7-8.7V19.8zm43.1 2.7v16.8a1.2 1.2 0 001.2 1.2h17zm3.4 62.9H47.8v-7.5h32.4zm0-13.1H47.8v-7.5h32.4z"></path></svg><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 Title-sc-4kyrt4-7 kRsLfZ kspcUv">AM_HELP.alp</span><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gZcoeQ StyledCloseButton-sc-13clwi6-0 dmjmoz" type="button" color="primary"><svg data-test="co-Close" stroke-width="10" size="1" class="SvgIcon-sc-13apni9-0 joedTZ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M102.3 107.7L65 70.3l-37.3 37.4-5.4-5.4L59.7 65 22.3 27.7l5.4-5.4L65 59.7l37.3-37.4 5.4 5.4L70.3 65l37.4 37.3-5.4 5.4z"></path></svg></button></div></li><li data-test="ide-tab" class="TabButton-sc-4kyrt4-6 ihrwTX" draggable="true"><div direction="row" class="Flex-sc-10ouakr-0 TabItem-sc-4kyrt4-5 doHqVb iZNxCA"><svg data-test="co-Globe" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 00-32.9 92.3 52.4 52.4 0 0059.3 4.6c18.7-11.1 28.9-33.4 24.6-54.8C110.2 30 88.5 12 64 12zm7.2 8c-.7 2.1-4.2.7-5.8.7 1.3-.5 8.5-3.5 4.4-1l1.4.3c-.7 2.1-.4-.1 0 0zm-18.2.9c.4.4 8-2 8.6-2.1s-9.1 2.7-4.5 3.4c-.9-.3-1.5-.2-1.9.6-1-1.5-2.1-1.3-3 0 .7.5 2.7 3.9.5 3a.9.9 0 01.2-1.5c-.8-.4-1.9-1.2-2.6-.3s1.6.7.6 1.1-1.6-.1-2.8 0-4.1 1-5.8-.4c1.4-1.4 6.4.6 6.5-1.9-1.5-.3-1.3-.7-2.3-1.3a52.4 52.4 0 016.4-2 1.4 1.4 0 00.1 1.4zM18.1 64.1a47 47 0 013.8-18.4c1.1-2.5 2.9-7 5.1-8.8s2.5-1 4.6 1.7.6 7 2.4 10.8c.9 2 2.7 3.1 4.1 4.7s2.4 5 4.7 6.4c-.9-.5-1.9-4.4-2.9-5.5 3.6.8 4.7 6.3 7.3 8.6s4 1.4 5.8 2.1 2 1.1 3.2 1.7 2.7 1.9 4.1 2.6 2.6.7 3.1 1.1c3.3 2.4-.4 4.2-.3 7.9s1.8 5 3.9 7.2 3.2 4 2.7 8.8-.7 7.3-1.3 10.5a12.5 12.5 0 00-.3 1.9 8 8 0 01-1.3 1.9c.8-.1 1 .2.9.8-26.4 2.5-49.6-20.3-49.6-46zM72.6 109c-1.4-1.3 1.5-4.2 2.5-5s4.4-1.5 3.4-4.2c.7 2.9 7.2-6.9 6.6-6.3.9-1.6 3.2-1.6 4.4-3.1s1.3-4.2 2.5-6.3 3-3.7-.6-5.5c-1.3-.7-6.3-2.4-6.8-.8a4.3 4.3 0 01-1-.9 1.1 1.1 0 001.3-.6 8.3 8.3 0 01-2.2.3c.9-4-1.1-3.7-4.4-5.3s-4.9-2.6-8-2.6-3.5 1.3-5.5 1.4c-4.8.3-2.1-2.5-3.9-4s-2.5-.1-2.9-.8 1.1-2.4.9-2.5c-2.2-2.5-3 2.6-6.4.3s1.1-6.8 3.9-7.4c1.1-.2 2.8-.7 4-.1s1.7 2.9 2.6 3 .6-4.8 1.3-5.5 5.4-10.7 9.8-8.9a9.4 9.4 0 00-1.8 1.2c-.5.8 3.8-1.1 3.1-.8 2.4-.9 3.5-2.1 6.2-1.5-1.5-.4-.2-3.1-2.8-2.6-.5.1-1.8 2.7-2.7 3.1s-2-1.8-1.9-1.8c-1.5-.4-1.9.3-3.8.9.6-4.3 8.6-.1 9.4-3.7.3-.9-3-3.4-3.5-4.1s-.8-2.4-1.7-2.6-1.6.9-1.4 1c-1.5-.4-1.7-.7-3.6-1.8s-3.8-1.7-4.7.2 1 2 .9 2.9a17 17 0 00-.7 2.1c.1-.6-1.8 2.9-.5 2.3-1.9 1-1-.2-2.1-.8a21.1 21.1 0 00-4.1-2.4c-5.4-2-5-3.2-1.3-6.5a18.6 18.6 0 013.1-2.6c.4-.4 1.4.2 2.1-.4s.2-1.9.7-2.3c3-2.1 8.4 1.7 2.8 4.6 2.9 0 5 2.2 7.8 2.2-.1-.7-1.5-.5-1.4-1.3s1.7.6 2.1.3-2.1-2-1.6-3.1 2.7 2.9 3.3 0c-.9-.5-4.3-1.4-3.9-2.9 1.4.9 2.8 1.9 4.3 2.7s2.6 1.1 1.5 2.1 2.6-.4 3.1.9-2.1-.1-2.5.4c4.8 1.5 1.2.8.3 3.3 2.3-.8 2.9 10.1 8.2 4.4 2.4-2.6 1.3-2.5 5.2-3.9s5.7-1.1 9 3.3c2 2.8 4.5 6.2 5.4 9.7s-.7 2.4-.6 4.4 1.6 2.2 2.7 4.1.1 3.3-1.8 5.5-4.9 7.2-2.2 11.6 4.7 2 2.8 6.8a45.4 45.4 0 01-4.2 8.2A46 46 0 0172.6 109c-.2-.1 17.4-3.4 0 0z"></path></svg><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 Title-sc-4kyrt4-7 kRsLfZ kspcUv">Pre submit</span><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gZcoeQ StyledCloseButton-sc-13clwi6-0 dmjmoz" type="button" color="primary"><svg data-test="co-Close" stroke-width="10" size="1" class="SvgIcon-sc-13apni9-0 joedTZ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M102.3 107.7L65 70.3l-37.3 37.4-5.4-5.4L59.7 65 22.3 27.7l5.4-5.4L65 59.7l37.3-37.4 5.4 5.4L70.3 65l37.4 37.3-5.4 5.4z"></path></svg></button></div></li><li title="Name: run
Path: /code/run" data-test="ide-tab" class="TabButton-sc-4kyrt4-6 ihrwTX" draggable="true"><div direction="row" class="Flex-sc-10ouakr-0 TabItem-sc-4kyrt4-5 doHqVb iZNxCA"><svg data-test="co-File" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M94.3 115.8H33.7a12 12 0 01-11.9-11.9V24.1a12 12 0 0111.9-11.9h40.7a7.2 7.2 0 014.8 2L104.1 39a7.1 7.1 0 012.1 4.9v60a12 12 0 01-11.9 11.9zm-60.6-96a4.4 4.4 0 00-4.4 4.3v79.8a4.4 4.4 0 004.4 4.3h60.6a4.4 4.4 0 004.4-4.3V48H78a8.7 8.7 0 01-8.7-8.7V19.8zm43.1 2.7v16.8a1.2 1.2 0 001.2 1.2h17zm3.4 62.9H47.8v-7.5h32.4zm0-13.1H47.8v-7.5h32.4z"></path></svg><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 Title-sc-4kyrt4-7 kRsLfZ kspcUv">run</span><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gZcoeQ StyledCloseButton-sc-13clwi6-0 dmjmoz" type="button" color="primary"><svg data-test="co-Close" stroke-width="10" size="1" class="SvgIcon-sc-13apni9-0 joedTZ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M102.3 107.7L65 70.3l-37.3 37.4-5.4-5.4L59.7 65 22.3 27.7l5.4-5.4L65 59.7l37.3-37.4 5.4 5.4L70.3 65l37.4 37.3-5.4 5.4z"></path></svg></button></div></li><li title="Name: untitled
Path: /code/untitled" data-test="ide-tab" class="TabButton-sc-4kyrt4-6 gxktEA" draggable="true"><div direction="row" class="Flex-sc-10ouakr-0 TabItem-sc-4kyrt4-5 doHqVb iZNxCA"><svg data-test="co-File" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M94.3 115.8H33.7a12 12 0 01-11.9-11.9V24.1a12 12 0 0111.9-11.9h40.7a7.2 7.2 0 014.8 2L104.1 39a7.1 7.1 0 012.1 4.9v60a12 12 0 01-11.9 11.9zm-60.6-96a4.4 4.4 0 00-4.4 4.3v79.8a4.4 4.4 0 004.4 4.3h60.6a4.4 4.4 0 004.4-4.3V48H78a8.7 8.7 0 01-8.7-8.7V19.8zm43.1 2.7v16.8a1.2 1.2 0 001.2 1.2h17zm3.4 62.9H47.8v-7.5h32.4zm0-13.1H47.8v-7.5h32.4z"></path></svg><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 Title-sc-4kyrt4-7 kRsLfZ kspcUv">untitled</span><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gZcoeQ StyledCloseButton-sc-13clwi6-0 dmjmoz" type="button" color="primary"><svg data-test="co-Close" stroke-width="10" size="1" class="SvgIcon-sc-13apni9-0 joedTZ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M102.3 107.7L65 70.3l-37.3 37.4-5.4-5.4L59.7 65 22.3 27.7l5.4-5.4L65 59.7l37.3-37.4 5.4 5.4L70.3 65l37.4 37.3-5.4 5.4z"></path></svg></button></div></li></ul><div class="Editors-sc-4kyrt4-1 iliuHR"><div class="Content-sc-4kyrt4-3 bbAkrs"><div><div class="PortaledContent-sc-4kyrt4-2 cGMKcS"><div data-test="environment-editor" direction="column" class="Flex-sc-10ouakr-0 JpMain-sc-1dqymty-0 fECnti fmfmoA"><div direction="column" class="Flex-sc-10ouakr-0 JpContent-zle587-0 czVBaH gmYwuA jp-widget co-widget-content"><div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><h3 class="EnvironmentHeaderLayout-nhplgu-1 jRVqzM">Environment</h3></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><div class="Collapsible-sc-15k4khe-0 eaZNYx"><div data-test="env-item" tabindex="0" class="ItemRow-sc-1yymkq8-0 eicJgC"><h5 class="m0d606-0-h5 ItemName-sc-1yymkq8-1 kkojNB iXnmGZ"> Java (9)</h5><div direction="column" class="Flex-sc-10ouakr-0 ItemDesc-sc-1yymkq8-2 izNRpz kYvwfc"><span>Zulu OpenJDK</span><div direction="row" class="Flex-sc-10ouakr-0 cfJwhX"><button color="secondary" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 Keyword-sc-1yymkq8-3 ivGlbj fbqdlH flwjri lahMlU">Ubuntu</button><button color="secondary" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 Keyword-sc-1yymkq8-3 ivGlbj fbqdlH flwjri lahMlU">16.04</button><button color="secondary" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 Keyword-sc-1yymkq8-3 ivGlbj fbqdlH flwjri lahMlU">Java</button></div></div><div class="SelectArea-sc-1yymkq8-4 dNgqoJ"><div class="SelectArea-sc-1yymkq8-4 dNgqoJ"><button data-analytics="[&quot;Clicked Change Base Environment&quot;,{&quot;category&quot;:&quot;EnvironmentEditor&quot;,&quot;capsuleId&quot;:&quot;e40b6e27-34bb-469e-86ed-d9d87880e11b&quot;,&quot;existingBaseEnvironment&quot;:&quot;Java (9)&quot;}]" color="primary" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH lhKrnT">Change</button></div></div></div></div></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><h4><div color="text" disabled="" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp kaGQsO sc-2cfrir-2 fktUiV"><span>Additional Packages</span> <svg data-test="co-Question" size="1" stroke-width="0" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 115.75A51.75 51.75 0 11115.75 64 51.8 51.8 0 0164 115.75zm0-96A44.25 44.25 0 10108.25 64 44.3 44.3 0 0064 19.75zm3.75 75.18h-7.5v-8.25h7.5zm0-13.4h-7.5v-5.69a18 18 0 017.32-14.52 4.52 4.52 0 01.53-.43 10.53 10.53 0 10-14-15.41l-5.8-4.76a18 18 0 1124.63 26 3.6 3.6 0 01-.52.43 10.52 10.52 0 00-4.63 8.73v5.69z"></path></svg></div></h4></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><div>Customize the selected environment with any other packages you need. You can also use these package managers to install other package managers, such as for different languages. Packages will be installed on the next capsule run. <a href="https://help.codeocean.com/getting-started/the-computational-environment/the-package-management-system" target="_blank" rel="noreferrer noopener" color="primary" type="button" class="sc-1l31c07-0 iJmlhm">Learn more.</a></div><div id="scrolled-pkg-suggestions-05x3qItauuwHB-Q-w4o70"><div direction="row" class="Flex-sc-10ouakr-0 PackageTableRow-sc-1fzxlwr-2 gqtCWT hLsFDA"><div class="InstallerCol-sc-1fzxlwr-3 dvWYnt"><div class="PackagesColHeader-sc-1fzxlwr-5 fxfSlv">Package Managers</div></div><div direction="row" class="Flex-sc-10ouakr-0 PackagesCol-sc-1fzxlwr-4 fBLLPt ijfhfB"><div class="PackagesColHeader-sc-1fzxlwr-5 fxfSlv">Packages</div></div></div><div direction="row" class="Flex-sc-10ouakr-0 PackageTableRow-sc-1fzxlwr-2 gqtCWT hLsFDA"><div class="InstallerCol-sc-1fzxlwr-3 dvWYnt"><span>apt-get</span><button data-test="apt-dropdown" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" data-analytics="[&quot;Manage Packages&quot;,{&quot;category&quot;:&quot;EnvironmentEditor&quot;,&quot;name&quot;:&quot;apt-get&quot;,&quot;pkgCount&quot;:1}]" color="secondary" type="button"><span><svg data-test="co-Cog" size="1.5" stroke-width="0" class="SvgIcon-sc-13apni9-0 cbeyPJ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M46.1 115.8a13.2 13.2 0 01-6.3-1.7l-7.1-4.2A12.2 12.2 0 0128.1 93l2.9-5.1a40.7 40.7 0 01-4.2-7.4h-6A12.5 12.5 0 018.4 68.1v-8.2a12.5 12.5 0 0112.4-12.4h6a45 45 0 014.3-7.3l-3-5.1a12.2 12.2 0 01-1.2-9.5 12.3 12.3 0 015.8-7.6l7.1-4.1a12.3 12.3 0 019.4-1.2 11.8 11.8 0 017.6 5.8l2.9 5.1a40.3 40.3 0 018.5 0l3-5.1a12.4 12.4 0 0117-4.6l7.1 4.2A12.2 12.2 0 0199.9 35L97 40.1a40.7 40.7 0 014.2 7.4h6a12.7 12.7 0 018.9 3.8 12.4 12.4 0 013.5 9v8a12.5 12.5 0 01-12.4 12.4h-6A47.7 47.7 0 0197 88l3 4.9a12.6 12.6 0 011.3 9.5 12.8 12.8 0 01-5.9 7.6l-7.1 4.1a12.3 12.3 0 01-9.4 1.2 12 12 0 01-7.6-5.8l-2.9-5.1a42.2 42.2 0 01-8.7 0l-2.9 5.1a12.4 12.4 0 01-10.7 6.3zm26.2-19.6l5.5 9.5a5.1 5.1 0 003 2.4 5.6 5.6 0 003.8-.5l7.1-4.1a4.9 4.9 0 002.3-3 4.6 4.6 0 00-.5-3.8l-5.7-9.3 1.7-2.1a33.9 33.9 0 005.7-9.7l.9-2.4h11.1a4.9 4.9 0 004.9-4.9v-8.1a5.3 5.3 0 00-1.4-3.7 4.9 4.9 0 00-3.5-1.5H96.1l-.9-2.4a30 30 0 00-5.6-9.6l-1.8-2 5.6-9.7a5.1 5.1 0 00.5-3.8 4.8 4.8 0 00-2.3-2.9l-7.1-4.2a5 5 0 00-6.8 1.8l-5.5 9.6-2.6-.4a30.7 30.7 0 00-11.3 0l-2.6.4-5.4-9.6a5.3 5.3 0 00-3-2.3 5.6 5.6 0 00-3.8.5l-7.1 4.1a5.2 5.2 0 00-2.3 3 5 5 0 00.5 3.8l5.5 9.6-1.6 2a35.3 35.3 0 00-5.7 9.7l-.9 2.4H20.8a4.9 4.9 0 00-4.9 4.9v8.2a4.9 4.9 0 004.9 4.9h11.1l.9 2.4a30 30 0 005.6 9.6l1.8 2-5.6 9.7a5.1 5.1 0 00-.5 3.8 4.4 4.4 0 002.3 2.9l7.1 4.2a5 5 0 006.8-1.8l5.5-9.6 2.6.4a30.7 30.7 0 0011.3 0zm-8.2-14.4a17.6 17.6 0 1117.5-17.6 17.6 17.6 0 01-17.5 17.6zm0-27.7a10.1 10.1 0 1010 10.1 10.1 10.1 0 00-10-10.1z"></path></svg></span><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div><div data-test="apt" direction="row" class="Flex-sc-10ouakr-0 PackagesCol-sc-1fzxlwr-4 fBLLPt ijfhfB"><div class="Flex-sc-10ouakr-0 cfJwhX sc-1l5zvn7-0 fWAtAw" direction="row"><div class="PillBasic-wdqudc-0 wdqudc-1 PillItem-doll9c-3 PillItem-doll9c-2 PillItem-doll9c-1 izzToO hTBOze fScQDz cAcAIK dzSMAN"><div role="button" tabindex="-1" class="PillItemButton-doll9c-7 bFfgch"><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 PillItemName-doll9c-5 kRsLfZ kQGmNY">anylogic</span> <span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 PillItemSmall-doll9c-6 kRsLfZ erbSGN">latest</span></div><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gZcoeQ StyledCloseButton-sc-13clwi6-0 PillItemRemove-doll9c-4 dmjmoz laBOBG" type="button" color="primary"><svg data-test="co-Close" stroke-width="10" size="1" class="SvgIcon-sc-13apni9-0 UPmjA" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M102.3 107.7L65 70.3l-37.3 37.4-5.4-5.4L59.7 65 22.3 27.7l5.4-5.4L65 59.7l37.3-37.4 5.4 5.4L70.3 65l37.4 37.3-5.4 5.4z"></path></svg></button><div direction="row" class="Flex-sc-10ouakr-0 MultiInputActions-doll9c-0 jbMqSw hnSVCk"><button type="button" color="primary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH dsCGwh"><svg data-test="co-CheckCircle" size="1.7" stroke-width="0" class="SvgIcon-sc-13apni9-0 hbbhVY" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 115.75A51.75 51.75 0 11115.75 64 51.8 51.8 0 0164 115.75zm0-96A44.25 44.25 0 10108.25 64 44.3 44.3 0 0064 19.75z"></path><path d="M56.59 84.33L39.01 66.87l5.28-5.32 12.29 12.2L83.6 46.72l5.3 5.3-32.31 32.31z"></path></svg></button><button type="button" color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH dPmAkb"><svg data-test="co-CloseCircle" size="1.7" stroke-width="0" class="SvgIcon-sc-13apni9-0 hbbhVY" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 117.15a51.75 51.75 0 1151.75-51.75A51.8 51.8 0 0164 117.15zm0-96a44.25 44.25 0 1044.25 44.25A44.3 44.3 0 0064 21.15z"></path><path d="M80.84 87.57L63.95 70.66 47.06 87.57l-5.31-5.3 16.9-16.92-16.9-16.92 5.31-5.3 16.89 16.91 16.89-16.91 5.3 5.3-16.89 16.92 16.89 16.92-5.3 5.3z"></path></svg></button></div></div><button type="button" class="PillBasic-wdqudc-0 wdqudc-1 ButtonPill-xbmbh7-1 ButtonPill-xbmbh7-0 izzToO gQXhgI ffvYXZ gZvgKr uf1qt7-0 cYHrA"><svg data-test="co-JpAdd" stroke-width="0" class="SvgIcon-sc-13apni9-0 bKiGZf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M116.1 72h-45v44h-14V72h-45V57h44V12h15v45h45z"></path></svg><span>Add</span></button></div></div></div></div></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr hySGNx"><h4><div color="text" disabled="" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp kaGQsO sc-2cfrir-2 fktUiV"><span>Post-Install Script</span> <svg data-test="co-Question" size="1" stroke-width="0" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 115.75A51.75 51.75 0 11115.75 64 51.8 51.8 0 0164 115.75zm0-96A44.25 44.25 0 10108.25 64 44.3 44.3 0 0064 19.75zm3.75 75.18h-7.5v-8.25h7.5zm0-13.4h-7.5v-5.69a18 18 0 017.32-14.52 4.52 4.52 0 01.53-.43 10.53 10.53 0 10-14-15.41l-5.8-4.76a18 18 0 1124.63 26 3.6 3.6 0 01-.52.43 10.52 10.52 0 00-4.63 8.73v5.69z"></path></svg></div></h4></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><div>If a package isn’t available via the above package managers, use this script to download, extract and install it. Please note: this script should not be used to download data and cannot access any capsule folders. <a href="https://help.codeocean.com/getting-started/the-computational-environment/using-the-setup-script-for-further-customization" target="_blank" rel="noreferrer noopener" color="primary" type="button" class="sc-1l31c07-0 iJmlhm">Learn more.</a></div><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH dsCGwh OpenPostInstallScript-sc-12jwbbv-0 djthsC" color="primary" type="button"><span>Edit Post-Install Script <svg data-test="co-Export" size="1.2" stroke-width="0" class="SvgIcon-sc-13apni9-0 eASQYR" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M115.9 15.9c0-.2-.1-.3-.1-.4s-.1-.4-.2-.5a.8.8 0 00-.2-.5l-.2-.3-.6-.8-.8-.6-.3-.2-.5-.2-.5-.2H81a5 5 0 00-4.9 3.8 4.9 4.9 0 004.7 5.9h18.7L61.8 59.5a5.1 5.1 0 00-.7 6.2 4.7 4.7 0 004 2.2 4.5 4.5 0 003.4-1.5l37.8-37.9V47a5 5 0 003.9 4.9 4.9 4.9 0 005.8-4.7V16.8a2.8 2.8 0 00-.1-.9z"></path><path d="M115.6 68.1c-4.2-4.3-9.3-1.4-9.3 2.7v31.9a3.6 3.6 0 01-3.6 3.6H32.3a10.5 10.5 0 01-10.6-10.6V25.3a3.6 3.6 0 013.6-3.6h33.2a2.7 2.7 0 001.9-.8c3.6-4.2.8-8.9-3.2-8.9H20.5a8.5 8.5 0 00-8.5 8.5v75.2A20.3 20.3 0 0032.3 116h75.2a8.5 8.5 0 008.5-8.5V69a1 1 0 00-.4-.9z"></path></svg></span></button></div></div></div></div></div></div></div><div class="Content-sc-4kyrt4-3 bbAkrs"><div><div class="PortaledContent-sc-4kyrt4-2 cGMKcS"></div></div></div><div class="Content-sc-4kyrt4-3 bbAkrs"><div><div class="PortaledContent-sc-4kyrt4-2 cGMKcS"><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr hySGNx"><h2>Before You Submit...</h2><div>To ensure a smooth verification process,
       please complete these last few steps before submitting:</div><div class="ListSection-dsm638-4 fpnKZp"><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_7b73dbfc-4078-49ff-b8b9-61f4d8edd7f9" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_7b73dbfc-4078-49ff-b8b9-61f4d8edd7f9" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Ensure your code runs successfully.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob">Look for any error messages in your<button disabled="" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">output</button>file and fix your code if necessary.</div><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_2710c572-928c-4731-9562-6202924ae84e" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_2710c572-928c-4731-9562-6202924ae84e" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Set up the code to save any results to the <pre>../results</pre> folder.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob">Because Code Ocean<a href="https://help.codeocean.com/en/articles/2465269-running-your-code-headlessly" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">runs heedlessly</a>by default (that is, without the option for user input during runtime), files should be saved explicitly.<br>See how to<a href="https://help.codeocean.com/en/articles/1087133-saving-files" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">save your results.</a></div><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_efea3a74-dabf-4a6b-ab3a-506131d044fb" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_efea3a74-dabf-4a6b-ab3a-506131d044fb" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Ensure the capsule’s title is meaningful, to give readers a better sense of what the capsule contains.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob">You can use the manuscript title or see examples on the<a href="https://codeocean.com/explore/capsules" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">Explore page.</a></div><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_197c5f57-ec13-4556-b382-feff3f07e844" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_197c5f57-ec13-4556-b382-feff3f07e844" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Upload all necessary data files to the <pre>../data</pre> folder.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob">To ensure clarity for the reader and to simplify<a href="https://help.codeocean.com/en/articles/2887105-version-control-on-code-ocean-an-overview" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">Git tracking</a>in Code Ocean, data <strong><u>should not go</u></strong> in the <pre>../code</pre> folder.<br>Because URLs and download syntax tend to change over time, data should also not be downloaded during runtime.</div><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_4c654232-ba75-4a71-822e-6f9c9382fa11" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_4c654232-ba75-4a71-822e-6f9c9382fa11" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Install all libraries and dependencies via the<a color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">environment editor</a>, and not during runtime.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob">See how to<a href="https://help.codeocean.com/en/articles/1374271-configuring-your-computational-environment-an-overview" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">configure your computational environment.</a></div><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_e7f1d98e-af6e-48f2-a2b7-608041c22500" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_e7f1d98e-af6e-48f2-a2b7-608041c22500" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Upload source code rather than compiled binaries, and then compile binaries during runtime.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob">Read<a href="https://help.codeocean.com/en/articles/1419368-binaries-on-code-ocean-compiling-and-executing-e-g-mex-files-in-matlab" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">Binaries on Code Ocean: compiling and executing</a>for more information.</div><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_3d98b561-f7d2-4564-8036-00452e3e7b28" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_3d98b561-f7d2-4564-8036-00452e3e7b28" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Write a main script to reproduce your analysis as completely as possible.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob">If you have multiple analysis scripts, your main script should run them all in sequence.<br>If you have multiple datasets, your code should analyze them all by default (whenever possible).</div><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_d346a8f2-e981-4f2f-b6c5-1bf4bec40335" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_d346a8f2-e981-4f2f-b6c5-1bf4bec40335" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Provide sufficient metadata for widespread intelligibility, including:<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob"><li>Any appropriate tags;</li><li>A few lines from your abstract, or the entire thing, in the description pane;</li><li>Any information about an associated publication;</li><li>All affiliations for authors (use N/A if none is available);</li><li>If you wish to change the default licenses (MIT for code, CC0 for data), new licenses;</li><li>A representative image (hover over the language symbol in metadata - Upload Image).</li></div><div class="TitleWrapper-dsm638-0 gYlVMA"><div class="BooleanInput-vmgnf-0 eYkWCx n2hd7h-0 cygisz"><input id="checkbox_9aa20fd8-077e-466a-8192-5a2da8f71119" tabindex="0" type="checkbox" class="InputCommon-sc-10cpax4-1 CheckboxInput-kz1v70-1 etLtaJ gzFGM"><label for="checkbox_9aa20fd8-077e-466a-8192-5a2da8f71119" class="LabelCommon-sc-10cpax4-0 CheckboxLabel-kz1v70-0 gztACi dXppLt"></label></div><span wai-aria="button">Delete unnecessary files.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 kgmMIM"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 kintob">e.g., logs, ./__pycache__, temp, empty files, etc.</div><div class="TitleWrapper-dsm638-0 kjODdI"><svg data-test="co-Info" size="1.2" stroke-width="0" class="SvgIcon-sc-13apni9-0 cfxtLW" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 116a52 52 0 1152-52 52 52 0 01-52 52zm17.8-29.9a2.2 2.2 0 00-2.1-2.1h-6.9V49.1a2.2 2.2 0 00-2.1-2.1H48.9a2.2 2.2 0 00-2.1 2.1v10.8a2.2 2.2 0 002.1 2.1h6.9v22h-6.9a2.2 2.2 0 00-2.1 2.1v10.8a2.2 2.2 0 002.1 2.1h30.8a2.2 2.2 0 002.1-2.1zM72.9 25a2 2 0 00-2-2h-13a2.2 2.2 0 00-2.1 2.1v10.8a2.2 2.2 0 002.1 2.1h12.8a2.2 2.2 0 002.1-2.1V25z"></path></svg><span>See <a href="https://help.codeocean.com/en/articles/1120151-code-ocean-s-verification-process-for-computational-reproducibility" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">Code Ocean’s required guidelines for verification</a> for more information.</span></div><h3 class="SectionTitle-dsm638-5 inhdPe">Final Steps</h3><div class="TitleWrapper-dsm638-0 kjODdI"><svg data-test="co-CheckFull" size="1.2" class="SvgIcon-sc-13apni9-0 cJBnUm FulfilledIcon-dsm638-1 cVmKoN" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg><span wai-aria="button">Fill out required metadata.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 bRmuek"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor" open=""><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 jbqVqN">Metadata includes key information about your capsule,<a color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">Go to metadata.</a></div><div class="TitleWrapper-dsm638-0 kjODdI"><svg data-test="co-CheckFull" size="1.2" class="SvgIcon-sc-13apni9-0 cJBnUm FulfilledIcon-dsm638-1 cVmKoN" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg><span wai-aria="button">Perform a reproducible run that includes all the latest changes.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 bRmuek"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor" open=""><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 jbqVqN">It looks like you've made changes to your capsule since the last run.<br>Please perform a reproducible run to ensure the results reflect your latest changes,<a color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">Run now.</a></div><div class="TitleWrapper-dsm638-0 kjODdI"><svg data-test="co-CheckFull" size="1.2" class="SvgIcon-sc-13apni9-0 cJBnUm FulfilledIcon-dsm638-1 cVmKoN" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 12a52 52 0 1052 52 51.9 51.9 0 00-52-52zm-4 71.4l-.5.5a5.3 5.3 0 01-3.1 1.1 4.8 4.8 0 01-3.4-1.4L34.5 64.9l6.8-6.8 15.1 15.1L86.6 43l6.8 6.8z"></path></svg><span wai-aria="button">Ensure all files in your capsule are either tracked in Git or intentionally excluded from Git.<button color="primary" type="button" class="sc-1l31c07-0 fCGlBT"><div class="p1rkmd-0 bRmuek"><svg data-test="co-Collapse" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor" open=""><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></div></button></span></div><div class="CollapsableDetails-dsm638-2 jbqVqN">All files important to the reproducibility of your code should be tracked in Git but we encourage you to exclude data and results,<a href="https://help.codeocean.com/articles/3294147-best-practices-in-git-on-code-ocean" color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">Here's why.</a><a color="primary" type="button" target="_blank" class="sc-1l31c07-0 GoToLink-dsm638-3 iJmlhm cMUikm">See changes</a></div></div><button disabled="" color="primary" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH ftCwkD">Submit</button></div></div></div></div><div class="Content-sc-4kyrt4-3 bbAkrs"><div><div class="PortaledContent-sc-4kyrt4-2 cGMKcS"></div></div></div><div class="Content-sc-4kyrt4-3 iGxDmR"><div><div class="PortaledContent-sc-4kyrt4-2 cGMKcS"><div><div class="react-monaco-editor-container" data-keybinding-context="1" data-mode-id="plaintext" style="width: 426px; height: 598.797px;"><div class="monaco-editor sc-1vkn94v-0 bwuspm  no-user-select  showUnused showDeprecated vs focused" role="code" data-uri="file:///code/untitled" style="width: 426px; height: 598px;"><div data-mprt="3" class="overflow-guard" style="width: 426px; height: 598px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: -17249px; height: 18031px; width: 64px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 18031px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays focused" role="presentation" aria-hidden="true" style="position: absolute; width: 64px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; height: 18031px;"><div style="position:absolute;top:17366px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">585</div></div><div style="position:absolute;top:17385px;width:100%;height:19px;"></div><div style="position:absolute;top:17404px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">586</div></div><div style="position:absolute;top:17423px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">587</div></div><div style="position:absolute;top:17442px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">588</div></div><div style="position:absolute;top:17461px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">589</div></div><div style="position:absolute;top:17480px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">590</div></div><div style="position:absolute;top:17499px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">591</div></div><div style="position:absolute;top:17518px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">592</div></div><div style="position:absolute;top:17537px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">593</div></div><div style="position:absolute;top:17556px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">594</div></div><div style="position:absolute;top:17575px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">595</div></div><div style="position:absolute;top:17594px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">596</div></div><div style="position:absolute;top:17613px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">597</div></div><div style="position:absolute;top:17632px;width:100%;height:19px;"></div><div style="position:absolute;top:17651px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">598</div></div><div style="position:absolute;top:17670px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">599</div></div><div style="position:absolute;top:17689px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">600</div></div><div style="position:absolute;top:17708px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">601</div></div><div style="position:absolute;top:17727px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">602</div></div><div style="position:absolute;top:17746px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">603</div></div><div style="position:absolute;top:17765px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">604</div></div><div style="position:absolute;top:17784px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">605</div></div><div style="position:absolute;top:17803px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">606</div></div><div style="position:absolute;top:17822px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">607</div></div><div style="position:absolute;top:17841px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">608</div></div><div style="position:absolute;top:17309px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">582</div></div><div style="position:absolute;top:17328px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">583</div></div><div style="position:absolute;top:17347px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">584</div></div><div style="position:absolute;top:17233px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">578</div></div><div style="position:absolute;top:17252px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">579</div></div><div style="position:absolute;top:17271px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">580</div></div><div style="position:absolute;top:17290px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">581</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 64px; width: 362px; height: 598px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; transform: translate3d(0px, 0px, 0px); contain: strict; top: -17249px; left: 0px;"><div class="view-overlays focused" role="presentation" aria-hidden="true" style="position: absolute; height: 0px; width: 362px;"><div style="position:absolute;top:17366px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17385px;width:100%;height:19px;"></div><div style="position:absolute;top:17404px;width:100%;height:19px;"></div><div style="position:absolute;top:17423px;width:100%;height:19px;"></div><div style="position:absolute;top:17442px;width:100%;height:19px;"></div><div style="position:absolute;top:17461px;width:100%;height:19px;"></div><div style="position:absolute;top:17480px;width:100%;height:19px;"></div><div style="position:absolute;top:17499px;width:100%;height:19px;"><div class="cigra" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17518px;width:100%;height:19px;"><div class="cigra" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17537px;width:100%;height:19px;"><div class="cigra" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17556px;width:100%;height:19px;"><div class="cigra" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17575px;width:100%;height:19px;"><div class="cigra" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17594px;width:100%;height:19px;"><div class="cigra" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17613px;width:100%;height:19px;"><div class="cigra" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17632px;width:100%;height:19px;"><div class="current-line" style="width:362px; height:19px;"></div></div><div style="position:absolute;top:17651px;width:100%;height:19px;"></div><div style="position:absolute;top:17670px;width:100%;height:19px;"></div><div style="position:absolute;top:17689px;width:100%;height:19px;"></div><div style="position:absolute;top:17708px;width:100%;height:19px;"></div><div style="position:absolute;top:17727px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17746px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17765px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17784px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17803px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17822px;width:100%;height:19px;"></div><div style="position:absolute;top:17841px;width:100%;height:19px;"></div><div style="position:absolute;top:17309px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17328px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17347px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17233px;width:100%;height:19px;"></div><div style="position:absolute;top:17252px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17271px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div><div style="position:absolute;top:17290px;width:100%;height:19px;"><div class="cigr" style="left:0px;height:19px;width:30.78125px"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; width: 362px; height: 18031px;"><div style="top:17366px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sheet10.write(vt,&nbsp;2,&nbsp;str(node_xtruth</span></span></div><div style="top:17385px;height:19px;" class="view-line"><span><span class="mtk1">[float(x[0])]))</span></span></div><div style="top:17404px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:17423px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:17442px;height:19px;" class="view-line"><span><span class="mtk1">vy&nbsp;=&nbsp;1</span></span></div><div style="top:17461px;height:19px;" class="view-line"><span><span class="mtk1">sheet11&nbsp;=&nbsp;book.add_sheet("Sheet&nbsp;11")&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:17480px;height:19px;" class="view-line"><span><span class="mtk1">for&nbsp;n&nbsp;in&nbsp;range(0,len(id_inside)):</span></span></div><div style="top:17499px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;vy&nbsp;=&nbsp;vy+1#row&nbsp;number</span></span></div><div style="top:17518px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;gg&nbsp;=&nbsp;id_time_arr[n]</span></span></div><div style="top:17537px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;=&nbsp;gg.split(';')</span></span></div><div style="top:17556px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;h=id_inside[gg]&nbsp;</span></span></div><div style="top:17575px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sheet11.write(vy,&nbsp;0,&nbsp;gg)</span></span></div><div style="top:17594px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sheet11.write(vy,&nbsp;1,str(h))</span></span></div><div style="top:17613px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sheet11.write(vy,&nbsp;2,&nbsp;str(node_xtruth</span></span></div><div style="top:17632px;height:19px;" class="view-line"><span><span class="mtk1">[float(x[0])]))</span></span></div><div style="top:17651px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;</span></span></div><div style="top:17670px;height:19px;" class="view-line"><span><span class="mtk1">bc&nbsp;=&nbsp;1</span></span></div><div style="top:17689px;height:19px;" class="view-line"><span><span class="mtk1">sheet12&nbsp;=&nbsp;book.add_sheet("Sheet&nbsp;12")&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:17708px;height:19px;" class="view-line"><span><span class="mtk1">for&nbsp;n&nbsp;in&nbsp;range(0,len(id_box_area)):</span></span></div><div style="top:17727px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;bc=&nbsp;bc+1#row&nbsp;number</span></span></div><div style="top:17746px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;gg&nbsp;=&nbsp;id_arr[n]</span></span></div><div style="top:17765px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;h&nbsp;&nbsp;=&nbsp;id_box_area[int(gg)]</span></span></div><div style="top:17784px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sheet12.write(bc,&nbsp;0,&nbsp;int(gg))</span></span></div><div style="top:17803px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sheet12.write(bc,&nbsp;1,&nbsp;h)</span></span></div><div style="top:17822px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:17841px;height:19px;" class="view-line"><span><span class="mtk1">ab&nbsp;=&nbsp;1</span></span></div><div style="top:17309px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;h=id_time_est_coord[gg]</span></span></div><div style="top:17328px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sheet10.write(vt,&nbsp;0,&nbsp;gg)</span></span></div><div style="top:17347px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sheet10.write(vt,&nbsp;1,str(h))</span></span></div><div style="top:17233px;height:19px;" class="view-line"><span><span class="mtk1">for&nbsp;n&nbsp;in&nbsp;range(0,len(id_time_est_coord)):</span></span></div><div style="top:17252px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;vt&nbsp;=&nbsp;vt+1#row&nbsp;number</span></span></div><div style="top:17271px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;gg&nbsp;=&nbsp;id_time_arr[n]</span></span></div><div style="top:17290px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;=&nbsp;gg.split(';')</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 17632px; left: 115px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 348px; height: 12px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 12px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 348px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="747" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 598px;"></canvas><div role="presentation" aria-hidden="true" class="visible scrollbar vertical" style="position: absolute; width: 14px; height: 598px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 572px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 20px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 426px;" class="scroll-decoration"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="off" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; top: 383px; left: 179px; width: 1px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover line-numbers"></div><div data-mprt="4" class="overlayWidgets" style="width: 426px;"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 598px;"><div class="minimap-shadow-hidden" style="height: 598px;"></div><canvas width="0" height="747" style="position: absolute; left: 0px; width: 0px; height: 598px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="747" style="position: absolute; left: 0px; width: 0px; height: 598px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; display: none; height: 55px;"><div class="minimap-slider-horizontal" style="position: absolute; left: 0px; width: 0px; top: 0px; height: 0px;"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"></div><div class="context-view" aria-hidden="true" style="display: none;"></div></div></div></div></div></div></div></div></div></div><span role="presentation" class="Resizer vertical "></span><div class="Pane vertical Pane2  " style="flex: 0 0 auto; position: relative; outline: none; width: 50%;"><div class="Flex-sc-10ouakr-0 Container-sc-4kyrt4-0 dYsnoi iOEmLy" direction="column"><ul class="Tabs-sc-4kyrt4-4 kkqCII"><li data-test="ide-tab" class="TabButton-sc-4kyrt4-6 ewxjrq" draggable="true"><div direction="row" class="Flex-sc-10ouakr-0 TabItem-sc-4kyrt4-5 doHqVb iZNxCA"><svg data-test="co-Metadata" class="SvgIcon-sc-13apni9-0 jrJThu dc1ola-0 dLHXzw" stroke-width="0" size="1" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M92.2 104.4H12.3C5.5 104.4 0 97.8 0 89.7V38.3c0-8.1 5.5-14.7 12.3-14.7h79.9A10.9 10.9 0 0199 26a4.7 4.7 0 011 1l26.7 33.2a6.3 6.3 0 010 7.6L100 101a4.7 4.7 0 01-1 1 10.9 10.9 0 01-6.8 2.4zM12.3 31c-2.6 0-4.9 3.4-4.9 7.3v51.4c0 3.9 2.3 7.3 4.9 7.3h79.9a4 4 0 002.1-.7L120.2 64 94.3 31.7a4 4 0 00-2.1-.7zm76.6 47.1a14.1 14.1 0 1114-14.1 14.1 14.1 0 01-14 14.1zm0-20.8a6.7 6.7 0 106.6 6.7 6.7 6.7 0 00-6.6-6.7zM64.5 77.1H18.4v-7.4h46.1zm0-18.8H18.4v-7.4h46.1z"></path></svg><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 Title-sc-4kyrt4-7 kRsLfZ kspcUv">Metadata</span><button class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gZcoeQ StyledCloseButton-sc-13clwi6-0 dmjmoz" type="button" color="primary"><svg data-test="co-Close" stroke-width="10" size="1" class="SvgIcon-sc-13apni9-0 joedTZ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M102.3 107.7L65 70.3l-37.3 37.4-5.4-5.4L59.7 65 22.3 27.7l5.4-5.4L65 59.7l37.3-37.4 5.4 5.4L70.3 65l37.4 37.3-5.4 5.4z"></path></svg></button></div></li></ul><div class="Editors-sc-4kyrt4-1 iliuHR"><div class="Content-sc-4kyrt4-3 iGxDmR"><div><div class="PortaledContent-sc-4kyrt4-2 cGMKcS"><div direction="column" class="Flex-sc-10ouakr-0 JpContent-zle587-0 czVBaH gmYwuA jp-widget co-widget-content"><div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL pvs7za-0 dOMxHZ"><div class="RequiredNote-sc-1dl46pm-0 fgtreM"><div color="info" class="Flex-sc-10ouakr-0 AlertWrapper-sc-1l4ex1w-2 dzxuxa fiSyIk Alert-ul6fg8-0 cBMXwt" direction="row"><div class="Text-sc-1l4ex1w-0 boqGvT"><b>*</b> <small>Required for capsule publication</small></div></div></div><h3>Metadata</h3></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><div class="PreviewContainer-yi707z-8 ktA-dby"><div class="ImageContainer-yi707z-6 esbzXe"><div color="14250023" class="CapsuleField-yi707z-0 kirnsI">Engineering</div><div class="CapsuleImage-yi707z-3 creWHb"><img src="./mvla_files/co-placeholder.054c52.jpg" alt="capsule" width="100%"><div direction="column" class="Flex-sc-10ouakr-0 UploadImage-yi707z-2 fECnti dIyBOV"><div class="FileContainer-sc-1t0lq8s-0 fsbZim StyleFileInput-sc-1lsapd-0 gOlQeY own-padd"><label for="metadataImage"><input accept="image/*" aria-label="Upload capsule image" type="file" id="metadataImage" tabindex="0"><div direction="column" class="Flex-sc-10ouakr-0 eRHBkM"><svg data-test="co-Camera" size="3.4" stroke-width="0" class="SvgIcon-sc-13apni9-0 dDvVAB" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M107.4 115.8H20.6A18.5 18.5 0 011.9 97.3V45.4a18.7 18.7 0 0118.7-18.6h15.8l5.3-10.1a8.4 8.4 0 017.4-4.5h29.8a8.4 8.4 0 017.3 4.3v.2l5.3 10.1h15.8A18.7 18.7 0 01126 45.4v52.1a18.6 18.6 0 01-18.6 18.3zM20.6 34.3A11.2 11.2 0 009.4 45.4v51.9a11.1 11.1 0 0011.2 10.8h43.3l43.5.2c6.1 0 11.2-4.9 11.2-10.7V45.4a11.2 11.2 0 00-11.2-11.1H87l-7.3-14a.8.8 0 00-.8-.5H49.1a1.2 1.2 0 00-.8.3L41 34.3zM64 100.7a29.1 29.1 0 1129.2-29.1A29.2 29.2 0 0164 100.7zM64 50a21.6 21.6 0 1021.7 21.6A21.7 21.7 0 0064 50z"></path></svg><span>Upload Image</span></div></label></div></div></div></div><div class="DetailsContainer-yi707z-7 evGfZV"><h5><span>Vishaka</span></h5><div class="DescriptionContainer-yi707z-10 lbslRD"><div class="TextContainer-sc-1wt0ka6-0 kLhCMh m0d606-0 kRsLfZ"><span class="Text-yi707z-9 htuJof"><span>wireless networking</span></span></div></div></div></div></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><h4>Capsule</h4><div label="Name" data-fieldgroup="Name" direction="row" class="RowField-sc-17d8gj1-4 feuNBy sc-1wvqd1o-0 hNgisa sc-1ypy9ju-0 kNawyu"><div font-size="" required="" color="text" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp bSufOa sc-2cfrir-2 fktUiV GroupLabel-sc-17d8gj1-0 cijgjo"><span>Name</span> </div><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 fmKMyV dZQCmB erFQtC cbyzTe zmqwez-4 hqqUlO"><input type="text" required="" name="name" placeholder="Capsule name" class="InputField-hu10jk-0 eLLgWM" value="Vishaka"></div></div><div label="Research Field" data-fieldgroup="Research Field" direction="row" class="RowField-sc-17d8gj1-4 feuNBy sc-1wvqd1o-0 hNgisa tp1jev-0 ezQdSI"><div font-size="" required="" color="text" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp bSufOa sc-2cfrir-2 fktUiV GroupLabel-sc-17d8gj1-0 cijgjo"><span>Research Field</span> </div><div class="sc-10xkbib-0 cFeLIq" role="combobox" aria-haspopup="listbox" aria-owns="downshift-1-menu" aria-expanded="false"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 fmKMyV dZQCmB erFQtC cbyzTe zmqwez-4 hqqUlO"><input type="text" id="downshift-1-input" aria-autocomplete="list" aria-controls="downshift-1-menu" aria-labelledby="downshift-1-label" autocomplete="off" name="field" placeholder="Add field" class="InputField-hu10jk-0 eLLgWM" value="Engineering"><div class="OwnPadd-sc-2usn4d-0 hJhYat"><button id="downshift-1-toggle-button" tabindex="-1" color="text" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH dHrAtG"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div><div label="Description" data-fieldgroup="Description" direction="row" class="RowField-sc-17d8gj1-4 ifwxbj sc-1wvqd1o-0 hNgisa sc-4aonie-0 gywgtp"><div font-size="" required="" color="text" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp bSufOa sc-2cfrir-2 fktUiV GroupLabel-sc-17d8gj1-0 cijgjo"><span>Description</span> </div><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 fmKMyV dZQCmB erFQtC cbyzTe gp1ijr-0 eUyajL"><textarea required="" name="description" placeholder="Description" rows="5" type="text" class="TextareaField-sc-1eprz8g-0 dwUQmz">wireless networking</textarea></div></div><div label="Tags" data-fieldgroup="Tags" direction="row" class="RowField-sc-17d8gj1-4 ifwxbj sc-1wvqd1o-0 hNgisa"><div color="text" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp bSufOa sc-2cfrir-2 fktUiV GroupLabel-sc-17d8gj1-0 ffhWWk"><span>Tags</span> </div><div class="Flex-sc-10ouakr-0 TagsWrapper-sc-138z9lm-0 cfJwhX hacWly sc-1dlmhpp-0 bCRFRJ" direction="row"><button type="button" class="PillBasic-wdqudc-0 wdqudc-1 ButtonPill-xbmbh7-1 ButtonPill-xbmbh7-0 izzToO gQXhgI ffvYXZ gZvgKr uf1qt7-0 cYHrA"><svg data-test="co-JpAdd" stroke-width="0" class="SvgIcon-sc-13apni9-0 bKiGZf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M116.1 72h-45v44h-14V72h-45V57h44V12h15v45h45z"></path></svg><span>Add</span></button></div></div></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><h4>Authors and Affiliations</h4><div><div label="Authors" data-fieldgroup="Authors" direction="row" class="RowField-sc-17d8gj1-4 ifwxbj sc-1wvqd1o-0 hNgisa"><div required="" color="text" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp bSufOa sc-2cfrir-2 fktUiV GroupLabel-sc-17d8gj1-0 cijgjo"><span>Authors</span> </div><div class="Flex-sc-10ouakr-0 cfJwhX sc-1l5zvn7-0 MultiInputWide-rsz5sp-0 fWAtAw gKjijA" direction="row"><button type="button" class="PillBasic-wdqudc-0 wdqudc-1 ButtonPill-xbmbh7-1 ButtonPill-xbmbh7-0 izzToO gQXhgI ffvYXZ gZvgKr uf1qt7-0 cYHrA"><svg data-test="co-JpAdd" stroke-width="0" class="SvgIcon-sc-13apni9-0 bKiGZf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M116.1 72h-45v44h-14V72h-45V57h44V12h15v45h45z"></path></svg><span>Add</span></button></div></div><div label="Corresponding contributor" data-fieldgroup="Corresponding contributor" direction="row" class="RowField-sc-17d8gj1-4 ifwxbj sc-1wvqd1o-0 hNgisa"><div color="text" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp bSufOa sc-2cfrir-2 fktUiV GroupLabel-sc-17d8gj1-0 ffhWWk"><span>Corresponding contributor</span> </div><div class="Flex-sc-10ouakr-0 cfJwhX sc-1l5zvn7-0 MultiInputWide-rsz5sp-0 fWAtAw gKjijA" direction="row"><button type="button" class="PillBasic-wdqudc-0 wdqudc-1 ButtonPill-xbmbh7-1 ButtonPill-xbmbh7-0 izzToO gQXhgI ffvYXZ gZvgKr uf1qt7-0 cYHrA"><svg data-test="co-JpAdd" stroke-width="0" class="SvgIcon-sc-13apni9-0 bKiGZf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M116.1 72h-45v44h-14V72h-45V57h44V12h15v45h45z"></path></svg><span>Add</span></button></div></div></div></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><h4>Licenses</h4><div label="Code" data-fieldgroup="Code" direction="row" class="RowField-sc-17d8gj1-4 feuNBy sc-1wvqd1o-0 GroupwAlert-qyv537-5 hNgisa gBrmkN"><div required="" color="text" class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp bSufOa sc-2cfrir-2 fktUiV GroupLabel-sc-17d8gj1-0 cijgjo"><span>Code</span> </div><div class="sc-10xkbib-0 cFeLIq" role="combobox" aria-haspopup="listbox" aria-owns="downshift-2-menu" aria-expanded="false"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 AreaWrap-qyv537-2 fmKMyV dZQCmB erFQtC cbyzTe xIglX"><input id="downshift-2-input" aria-autocomplete="list" aria-controls="downshift-2-menu" aria-labelledby="downshift-2-label" autocomplete="off" name="softwareLicenseId" placeholder="Select a license..." type="text" class="InputField-hu10jk-0 eLLgWM" value="GNU Library General Public License (LGPL)"><div class="Flex-sc-10ouakr-0 kKFSWJ own-padd" direction="row"><button id="downshift-2-toggle-button" tabindex="-1" color="text" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH dHrAtG"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div><div class="UploadContainer-sc-1pcwzog-1 cKCppG own-padd"><div class="FileContainer-sc-1t0lq8s-0 fsbZim StyleFileInput-sc-1lsapd-0 gOlQeY own-padd"><label for="code/LICENSE__custom"><input accept="text/plain" aria-label="Upload Code license" type="file" id="code/LICENSE__custom" tabindex="0"><div class="UploadButton-sc-1pcwzog-0 kpGFXf"><svg data-test="co-Upload" size="1.5" stroke-width="0" class="SvgIcon-sc-13apni9-0 cbeyPJ" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M100.9 110.1H76.3v-7.5H101a19.5 19.5 0 003.6-38.7 3.9 3.9 0 01-3-3 3.6 3.6 0 01.9-3.3 12.5 12.5 0 001.9-8.2 12.9 12.9 0 00-20.9-8.6 3.7 3.7 0 01-3.5.6 3.6 3.6 0 01-2.5-2.4 28.1 28.1 0 00-53.6 8.9 18 18 0 00-.1 4 3.9 3.9 0 01-.9 2.6 3.2 3.2 0 01-1.3 1 24.6 24.6 0 00-14 24c.8 12.9 11.9 23.1 25.3 23.1h18.8v7.5H32.9C15.6 110.1 1.2 96.9.1 80a32.2 32.2 0 0116.1-30.1 21.1 21.1 0 01.2-2.6 35.7 35.7 0 0166.2-14.8 20 20 0 0111.3-1.9 20.5 20.5 0 0118 17.9 21.4 21.4 0 01-1.2 9.4 27 27 0 01-9.7 52.2zm-33.1-.8h-7.6V83L47.3 95.9 42 90.5l19.3-19.3a3.9 3.9 0 015.4 0L86 90.5l-5.3 5.4L67.8 83z"></path></svg></div></label></div></div></div></div></div></div><div class="JpSection-ebzfko-2 JpSection-ebzfko-1 JpSection-ebzfko-0 dQClxX jmkOZr kdzBQL"><h4>Associated publication</h4><div>The publication associated with this compute capsule is:</div><div open="" class="ArticleSelection-a085e9-5 cCMgDo"><div><div class="BooleanInput-vmgnf-0 eYkWCx wsa055-0 cAOGB"><input id="no article" name="articleState" tabindex="0" type="radio" class="InputCommon-sc-10cpax4-1 RadioInput-wl38h0-1 etLtaJ kpWIWT" value="no article" checked=""><label for="no article" class="LabelCommon-sc-10cpax4-0 RadioLabel-wl38h0-0 GTaac fhzFNG">none</label></div><div class="BooleanInput-vmgnf-0 eYkWCx wsa055-0 cAOGB"><input id="article in review" name="articleState" tabindex="0" type="radio" class="InputCommon-sc-10cpax4-1 RadioInput-wl38h0-1 etLtaJ kpWIWT" value="article in review"><label for="article in review" class="LabelCommon-sc-10cpax4-0 RadioLabel-wl38h0-0 GTaac fhzFNG"><div class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp iZvmfu sc-2cfrir-2 LabelTip-a085e9-1 fktUiV ldxHMH"><span>yet to be published</span> <svg data-test="co-Question" size="1" stroke-width="0" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 115.75A51.75 51.75 0 11115.75 64 51.8 51.8 0 0164 115.75zm0-96A44.25 44.25 0 10108.25 64 44.3 44.3 0 0064 19.75zm3.75 75.18h-7.5v-8.25h7.5zm0-13.4h-7.5v-5.69a18 18 0 017.32-14.52 4.52 4.52 0 01.53-.43 10.53 10.53 0 10-14-15.41l-5.8-4.76a18 18 0 1124.63 26 3.6 3.6 0 01-.52.43 10.52 10.52 0 00-4.63 8.73v5.69z"></path></svg></div></label></div><div class="BooleanInput-vmgnf-0 eYkWCx wsa055-0 cAOGB"><input id="article published" name="articleState" tabindex="0" type="radio" class="InputCommon-sc-10cpax4-1 RadioInput-wl38h0-1 etLtaJ kpWIWT" value="article published"><label for="article published" class="LabelCommon-sc-10cpax4-0 RadioLabel-wl38h0-0 GTaac fhzFNG">published</label></div></div></div></div></div></div></div></div></div></div></div></div></div></div><span role="presentation" class="Resizer vertical "></span><div class="Pane vertical Pane2  " style="flex: 0 0 auto; position: relative; outline: none; width: 50px; min-width: 30rem;"><div class="EdgePanel-sc-8kz175-0 gZsvCV"><div><div direction="column" data-test="reproducibility-pane" class="Flex-sc-10ouakr-0 izNRpz"><div class="Flexible-sc-10ouakr-3 Flexible-sc-10ouakr-2 Flexible-sc-10ouakr-1 jfIeFT bGzaUj gjDCFT"><button color="primary" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 WideButton-sc-161p58u-0 ivGlbj fbqdlH ftCwkD gVfPsr"><svg data-test="co-Play" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M32.1 116a13.8 13.8 0 01-7.4-2.1 14.7 14.7 0 01-7.3-12.7V26.8A14.7 14.7 0 0139.5 14l64.4 37.2a14.8 14.8 0 017.3 12.8 14.5 14.5 0 01-7.4 12.8l-64.3 37.1a13.8 13.8 0 01-7.4 2.1zm.1-95.1a5.3 5.3 0 00-2.8.7h-.2a5.8 5.8 0 00-2.8 5.1v74.4a6 6 0 002.9 5.1h.1a5.6 5.6 0 005.6 0L99.5 69a5.7 5.7 0 002.9-5 6.1 6.1 0 00-2.9-5.1L34.9 21.6a5 5 0 00-2.7-.7z"></path></svg><span>Reproducible Run</span></button></div><div class="ButtonStripContainer-sc-1yij9iv-5 ifWbZF"><b>or launch a cloud workstation</b><div class="ButtonStrip-sc-1yij9iv-6 fipbLB"><button data-test="CW-btn-JupyterLab" type="button" class="BasicButton-sc-158odgo-0 IdeButton-sc-1yij9iv-3 ivGlbj gksAoq"><div class="IdeIcon-sc-1yij9iv-2 enMMaa"></div></button><button data-test="CW-btn-RStudio" type="button" class="BasicButton-sc-158odgo-0 IdeButton-sc-1yij9iv-3 ivGlbj gksAoq"><div class="IdeIcon-sc-1yij9iv-2 lnZdDK"></div></button><button data-test="CW-btn-Jupyter" type="button" class="BasicButton-sc-158odgo-0 IdeButton-sc-1yij9iv-3 ivGlbj gksAoq"><div class="IdeIcon-sc-1yij9iv-2 hgxmpJ"></div></button><button data-test="CW-btn-Terminal" type="button" class="BasicButton-sc-158odgo-0 IdeButton-sc-1yij9iv-3 ivGlbj gksAoq"><div class="IdeIcon-sc-1yij9iv-2 kGZVGo"></div></button><button data-test="CW-btn-Shiny" type="button" class="BasicButton-sc-158odgo-0 IdeButton-sc-1yij9iv-3 ivGlbj gksAoq"><div class="IdeIcon-sc-1yij9iv-2 bPMJTl"></div></button></div></div><div direction="column" data-test="timeline" class="Flex-sc-10ouakr-0 TimelineWrapper-b7we87-0 izNRpz hDCnCJ"><header class="sc-10h9f64-0 TimelineHeader-b7we87-1 bredol gMpqOo">Timeline </header><div class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 Box-fq9y0z-0 EdnWb dPvMor fOjIRp"><div class="Axis-sc-18nbs32-0 cZhCtt"></div><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 hVQMof hveCgH" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"><div color="info" class="Circle-sc-18nbs32-2 dupXbj"></div></div><div direction="column" class="Flex-sc-10ouakr-0 Layout-w5js3e-0 dYsnoi hLOvCu"><div direction="row" class="Flex-sc-10ouakr-0 dnsvpq"><span>You have</span><span> </span><button color="primary" type="button" class="sc-1l31c07-0 InlineLink-sc-1l1ebop-0 fCGlBT ZyGKt">3 uncommitted changes</button><div class="Label-sc-2cfrir-1 Label-sc-2cfrir-0 koEAMp iZvmfu sc-2cfrir-2 fktUiV"><span></span> <svg data-test="co-Question" size="1.2" stroke-width="0" class="SvgIcon-sc-13apni9-0 eASQYR" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 115.75A51.75 51.75 0 11115.75 64 51.8 51.8 0 0164 115.75zm0-96A44.25 44.25 0 10108.25 64 44.3 44.3 0 0064 19.75zm3.75 75.18h-7.5v-8.25h7.5zm0-13.4h-7.5v-5.69a18 18 0 017.32-14.52 4.52 4.52 0 01.53-.43 10.53 10.53 0 10-14-15.41l-5.8-4.76a18 18 0 1124.63 26 3.6 3.6 0 01-.52.43 10.52 10.52 0 00-4.63 8.73v5.69z"></path></svg></div></div><label for="commitMessageArea">Describe what changed:</label><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 fmKMyV dZQCmB erFQtC cbyzTe gp1ijr-0 eUyajL gf4h4l-0 cfghbN"><textarea rows="1" id="commitMessageArea" placeholder="Added AM_HELP.alp, run, untitled" type="text" class="TextareaField-sc-1eprz8g-0 dwUQmz" style="height: 30px;"></textarea></div><button color="success" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH gVLCkU WrappingButton-stji5q-1 kjAWdf ButtonDotsSpinner-sc-1vlm1ij-0 dUuJCn" type="button"><span>Commit Changes</span></button></div></div></div><div class="Flexible-sc-10ouakr-3 Flexible-sc-10ouakr-2 Flexible-sc-10ouakr-1 TreeContainer-sc-17cxd90-0 clBbhm iQaRGQ gjDCFT chBBSV FlexibleVirtualTree-b7we87-2 jhorcd"><div style="overflow: visible; height: 0px; width: 0px;"><div aria-label="grid" aria-readonly="true" class="ReactVirtualized__Grid ReactVirtualized__List PreparedForScrollList-sc-1stmtrw-0 kGLNOv navigatedListClass" id="virtual-tree-list-bd8c9c9c-7464-40f3-8f76-65abc3fff17e" role="grid" tabindex="0" style="box-sizing: border-box; direction: ltr; height: 352px; position: relative; width: 299px; will-change: transform; overflow: auto; --max-width:282px;"><div class="ReactVirtualized__Grid__innerScrollContainer" role="rowgroup" style="width: auto; height: 551px; max-width: 299px; max-height: 551px; overflow: hidden; position: relative;"><div class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 EdnWb dPvMor" style="height: 43px; left: 0px; position: absolute; top: 0px; width: 100%;"><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH sc-4w3avt-0 hjLzbU" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"><div color="primary" class="Circle-sc-18nbs32-2 gAoPhB"></div></div><span class="UserDetails-awu0cr-0 jwaNYk"><span class="UserName-sc-1pd2pre-0 hZhtEq">Vishaka Basnayake </span>ran&nbsp;<span>Jun 30, 2021</span></span><span><svg data-test="co-Error" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M113.53 117H14.47A7.48 7.48 0 018 113.31a7.36 7.36 0 010-7.41l49.52-91A7.37 7.37 0 0164 11a7.45 7.45 0 016.56 4l49.56 91a7.36 7.36 0 01-.16 7.28 7.48 7.48 0 01-6.43 3.72zm-2.2-6.2a.25.25 0 000 .07zm-94.59-.12v.06zm2-3.68h90.52L64 23.82zm43-87.3zm4.52-.07s.01.01.02 0zM69 53.35H59v26h10zM69 87H59v9h10z"></path></svg> <span class="Time-ysnrvl-1 cCUDVF">00:00:07</span></span><span data-test="menu-run-5045657" class="MenuContainer-ysnrvl-2 gEHogH"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></span></div></div><div class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 EdnWb cTLofu" style="height: 47px; left: 0px; position: absolute; top: 43px; width: 100%;"><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"></div><div class="ErrorAlert-sc-23gl5p-0 gBLyGO"><div class="ErrorIcon-sc-23gl5p-1 eEpudN"><svg data-test="co-Error" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 cxHAtD" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M113.53 117H14.47A7.48 7.48 0 018 113.31a7.36 7.36 0 010-7.41l49.52-91A7.37 7.37 0 0164 11a7.45 7.45 0 016.56 4l49.56 91a7.36 7.36 0 01-.16 7.28 7.48 7.48 0 01-6.43 3.72zm-2.2-6.2a.25.25 0 000 .07zm-94.59-.12v.06zm2-3.68h90.52L64 23.82zm43-87.3zm4.52-.07s.01.01.02 0zM69 53.35H59v26h10zM69 87H59v9h10z"></path></svg></div><span class="ErrorMessage-sc-23gl5p-2 jspDNe"><b>Run Failed</b> - Run environment setup failed</span></div></div></div><div tabindex="0" class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 EdnWb cTLofu fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 90px; width: 100%;"><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH SelectableRow-sc-1x1ez7m-0 kkijfc" data-node-name="0f419ad8-b063-4a61-9a89-b9231cefd038/Run 5045657" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"></div><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 howMsG bQKcrs" data-path="1625045657.0019581_1_0f419ad8-b063-4a61-9a89-b9231cefd038_computation/results" data-open="true"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 jvmLbT dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><div class="p1rkmd-0 hqlnGZ FolderToggle-sc-1olbryb-0 hDxpCt"><svg data-test="co-Arrow" open="" class="SvgIcon-sc-13apni9-0 rcyBm dc1ola-0 dLHXzw" stroke-width="0" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M28.3 12a10.1 10.1 0 00-5.6 1.6 11 11 0 00-5.6 9.7v81.4a11.2 11.2 0 005.6 9.7 10.1 10.1 0 005.6 1.6 10.4 10.4 0 005.6-1.6l70.4-40.6a11.3 11.3 0 005.6-9.8 11.5 11.5 0 00-5.6-9.8L33.9 13.6a10.4 10.4 0 00-5.6-1.6z"></path></svg></div><svg data-test="co-JpDirectory" fill="#616262" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M110.2 25H73.5a6.6 6.6 0 01-4.7-1.8l-9.5-9.5-.8-.6a4.6 4.6 0 00-2.6-1H18a6.3 6.3 0 00-5.9 5.9v91.6a6.5 6.5 0 006.5 6.5h91a6.6 6.6 0 006.5-6.5l.6-78a6.6 6.6 0 00-6.5-6.6zm-3.6 82H20.1V44h87z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">Run 5045657</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"></div></div></div></div><div tabindex="0" class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 EdnWb cTLofu fileSystemNode-parent" style="height: 22px; left: 0px; position: absolute; top: 112px; width: 100%;"><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH SelectableRow-sc-1x1ez7m-0 kkijfc" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"></div><div tabindex="-1" class="BaseTreeRow-sc-3gmbzi-0 fKBglZ on4ifu-0 TreeNodeWrapper-cj5hnd-0 cBDKFr eCOPCK" data-path="1625045657.0019581_1_0f419ad8-b063-4a61-9a89-b9231cefd038_computation/results/buildLog"><div class="InputWrap-zmqwez-3 InputWrap-zmqwez-2 InputWrap-zmqwez-1 InputWrap-zmqwez-0 fCESOl dZQCmB kvsjoY jUJiTn zmqwez-4 hqqUlO StyledStandaloneInput-emglro-0 dPuPTP"><div direction="row" class="Flex-sc-10ouakr-0 InputChild-sc-2usn4d-1 bDnwJa"><svg data-test="co-JpFile" fill="#757575" size="1.1" stroke-width="0" class="SvgIcon-sc-13apni9-0 kQflBf" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M101.9 115.8H26.1c-7.6 0-13.9-5.3-13.9-11.8V24c0-6.5 6.3-11.8 13.9-11.8h48.6a8.8 8.8 0 015.1 1.8l.3.3 33.2 33a6.4 6.4 0 012.5 5V104c0 6.5-6.3 11.8-13.9 11.8zm-75.8-96c-3.4 0-6.3 1.9-6.3 4.2v80c0 2.3 2.9 4.2 6.3 4.2h75.8c3.4 0 6.3-1.9 6.3-4.2V59H80.6a11 11 0 01-11.2-10.8V19.8zm50.8 1.9v26.5a3.6 3.6 0 003.7 3.3h26.3z"></path></svg></div><div class="DummyInput-hu10jk-1 BjZmO">buildLog</div></div><div class="RightElementStyle-f0f658-2 duneLP TREE_NODE_STOP_CLICK"><span color="info" class="FileSizeStyle-sc-15cmz0c-0 isfKtz">2.71 KB</span><div class="MenuWrapper-f0f658-0 bsVPre"><button color="secondary" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH fEmwor sc-4y585q-0 cWGzON" type="button"><svg data-test="co-Collapse" stroke-width="0" size="1" class="SvgIcon-sc-13apni9-0 jrJThu" focusable="false" viewBox="0 0 128 128" stroke="currentColor"><path d="M64 94.6l-49-49 8-8 41 41.1 41-41.1 8 8-49 49z"></path></svg></button></div></div></div></div></div><div class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 EdnWb dPvMor" style="height: 113px; left: 0px; position: absolute; top: 134px; width: 100%;"><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH sc-4w3avt-0 hjLzbU" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"><div color="success" class="Circle-sc-18nbs32-2 dnGEps"></div></div><div class="CommitWrapper-sc-2tjaon-1 hlTqaX"><span class="UserDetails-awu0cr-0 jwaNYk"><span class="UserName-sc-1pd2pre-0 hZhtEq">Vishaka Basnayake</span><span> </span><button color="primary" type="button" class="sc-1l31c07-0 fCGlBT">committed</button><span> </span><span>Jun 30, 2021</span></span></div></div><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"></div><div class="Flexible-sc-10ouakr-3 Flexible-sc-10ouakr-2 Flexible-sc-10ouakr-1 Message-sc-2tjaon-0 jfIeFT kiEzwY gjDCFT spxel">Added LICENSE; edited metadata.yml</div></div></div><div class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 EdnWb dPvMor" style="height: 95px; left: 0px; position: absolute; top: 247px; width: 100%;"><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH sc-4w3avt-0 hjLzbU" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"><div color="success" class="Circle-sc-18nbs32-2 dnGEps"></div></div><div class="CommitWrapper-sc-2tjaon-1 hlTqaX"><span class="UserDetails-awu0cr-0 jwaNYk"><span class="UserName-sc-1pd2pre-0 hZhtEq">Vishaka Basnayake</span><span> </span><button color="primary" type="button" class="sc-1l31c07-0 fCGlBT">committed</button><span> </span><span>Jun 30, 2021</span></span></div></div><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"></div><div class="Flexible-sc-10ouakr-3 Flexible-sc-10ouakr-2 Flexible-sc-10ouakr-1 Message-sc-2tjaon-0 jfIeFT kiEzwY gjDCFT spxel">Edited Dockerfile</div></div></div><div class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 EdnWb dPvMor" style="height: 95px; left: 0px; position: absolute; top: 342px; width: 100%;"><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH sc-4w3avt-0 hjLzbU" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"><div color="success" class="Circle-sc-18nbs32-2 dnGEps"></div></div><div class="CommitWrapper-sc-2tjaon-1 hlTqaX"><span class="UserDetails-awu0cr-0 jwaNYk"><span class="UserName-sc-1pd2pre-0 hZhtEq">Vishaka Basnayake</span><span> </span><button color="primary" type="button" class="sc-1l31c07-0 fCGlBT">committed</button><span> </span><span>Jun 30, 2021</span></span></div></div><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"></div><div class="Flexible-sc-10ouakr-3 Flexible-sc-10ouakr-2 Flexible-sc-10ouakr-1 Message-sc-2tjaon-0 jfIeFT kiEzwY gjDCFT spxel">Added Dockerfile, metadata.yml</div></div></div><div class="TimelineBase-cp3nt-0 TimelineNode-cp3nt-1 eNFeom dPvMor" style="height: 114px; left: 0px; position: absolute; top: 437px; width: 100%;"><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH sc-4w3avt-0 hjLzbU" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"><div color="warning" class="Circle-sc-18nbs32-2 iKnACH"></div></div><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 kRsLfZ">4 months ago</span></div><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"></div>Capsule imported from:</div><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"></div><a href="https://github.com/Chandrachapa/AM_HELP" color="primary" type="button" target="_blank" rel="noopener noreferrer" class="sc-1l31c07-0 ExternalRepoLink-sc-8cqcya-0 fESpJn fziqEI"><span class="SingleLine-sc-1e214tm-0 fzumHC m0d606-0 kRsLfZ">https://github.com/Chandrachapa/AM_HELP</span></a></div><div class="Flex-sc-10ouakr-0 Layout-sc-1bmk4iu-0 doHqVb hveCgH NodeFooter-sc-1ifomcn-0 kVWJaP" direction="row"><div class="AxisIndent-sc-18nbs32-1 kQPoKN"><div class="FadeUp-sc-18nbs32-4 weljk"></div></div><button color="primary" type="button" class="BasicButton-sc-158odgo-0 sc-158odgo-1 Button-sc-91tziw-0 ivGlbj fbqdlH lhKrnT">Show Prior History</button></div></div></div></div></div><div class="resize-triggers"><div class="expand-trigger"><div style="width: 300px; height: 352px;"></div></div><div class="contract-trigger"></div></div></div></div></div></div></div></div></div></div></div></div><div class="TabsContainer-sc-1j51uwg-2 cZpqEI"><ul class="TabsList-sc-1j51uwg-0 cxexBw"><li data-test="ide-side-tab" class="TabButton-sc-1j51uwg-1 bLMNzx">Reproducibility</li></ul></div></div></div></div></div><script type="text/javascript" async="" src="./mvla_files/analytics.min.js.download"></script><script src="./mvla_files/polyfill.min.js.download"></script><noscript><h1>This web app requires javascript to run.</h1></noscript><script src="./mvla_files/v-node_modules_babel_runtime_helpers_esm_taggedTemplateLiteral_js-node_modules_axios_index_js-22565d.d96df6.js.download"></script><script src="./mvla_files/main.38dee7.js.download"></script><aside class="HoneyToastContainer-sc-8rslgf-0 hunDEf" style=""><div></div></aside><script async="" src="./mvla_files/unsupported.f815f1.js.download"></script><iframe id="intercom-frame" style="position: absolute !important; opacity: 0 !important; width: 1px !important; height: 1px !important; top: 0 !important; left: 0 !important; border: none !important; display: block !important; z-index: -1 !important; pointer-events: none;" aria-hidden="true" tabindex="-1" title="Intercom" src="./mvla_files/saved_resource.html"></iframe><div class="intercom-lightweight-app"><style id="intercom-lightweight-app-style" type="text/css">
  @keyframes intercom-lightweight-app-launcher {
    from {
      opacity: 0;
      transform: scale(0.5);
    }
    to {
      opacity: 1;
      transform: scale(1);
    }
  }

  @keyframes intercom-lightweight-app-gradient {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @keyframes intercom-lightweight-app-messenger {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .intercom-lightweight-app {
    position: fixed;
    z-index: 2147483001;
    width: 0;
    height: 0;
    font-family: intercom-font, "Helvetica Neue", "Apple Color Emoji", Helvetica, Arial, sans-serif;
  }

  .intercom-lightweight-app-gradient {
    position: fixed;
    z-index: 2147483002;
    width: 500px;
    height: 500px;
    bottom: 0;
    right: 0;
    pointer-events: none;
    background: radial-gradient(
      ellipse at bottom right,
      rgba(29, 39, 54, 0.16) 0%,
      rgba(29, 39, 54, 0) 72%);
    animation: intercom-lightweight-app-gradient 200ms ease-out;
  }

  .intercom-lightweight-app-launcher {
    position: fixed;
    z-index: 2147483003;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #0084ea;
    cursor: pointer;
    box-shadow: 0 1px 6px 0 rgba(0, 0, 0, 0.06), 0 2px 32px 0 rgba(0, 0, 0, 0.16);
    animation: intercom-lightweight-app-launcher 250ms ease;
  }

  .intercom-lightweight-app-launcher:focus {
    outline: none;
    
  }

  .intercom-lightweight-app-launcher-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 0;
    left: 0;
    width: 60px;
    height: 60px;
    transition: transform 100ms linear, opacity 80ms linear;
  }

  .intercom-lightweight-app-launcher-icon-open {
    
        opacity: 1;
        transform: rotate(0deg) scale(1);
      
  }

  .intercom-lightweight-app-launcher-icon-open svg {
    width: 28px;
    height: 32px;
  }

  .intercom-lightweight-app-launcher-icon-open svg path {
    fill: rgb(255, 255, 255);
  }

  .intercom-lightweight-app-launcher-icon-self-serve {
    
        opacity: 1;
        transform: rotate(0deg) scale(1);
      
  }

  .intercom-lightweight-app-launcher-icon-self-serve svg {
    height: 56px;
  }

  .intercom-lightweight-app-launcher-icon-self-serve svg path {
    fill: rgb(255, 255, 255);
  }

  .intercom-lightweight-app-launcher-custom-icon-open {
    max-height: 36px;
    max-width: 36px;
    
        opacity: 1;
        transform: rotate(0deg) scale(1);
      
  }

  .intercom-lightweight-app-launcher-icon-minimize {
    
        opacity: 0;
        transform: rotate(-60deg) scale(0);
      
  }

  .intercom-lightweight-app-launcher-icon-minimize svg {
    width: 16px;
  }

  .intercom-lightweight-app-launcher-icon-minimize svg path {
    fill: rgb(255, 255, 255);
  }

  .intercom-lightweight-app-messenger {
    position: fixed;
    z-index: 2147483003;
    overflow: hidden;
    background-color: white;
    animation: intercom-lightweight-app-messenger 250ms ease-out;
    
        width: 376px;
        height: calc(100% - 120px);
        max-height: 704px;
        min-height: 250px;
        right: 20px;
        bottom: 100px;
        box-shadow: 0 5px 40px rgba(0,0,0,0.16);
        border-radius: 8px;
      
  }

  .intercom-lightweight-app-messenger-header {
    height: 75px;
    background: linear-gradient(
      135deg,
      rgb(0, 132, 234) 0%,
      rgb(0, 74, 132) 100%
    );
  }

  @media print {
    .intercom-lightweight-app {
      display: none;
    }
  }
</style><div class="intercom-lightweight-app-launcher intercom-launcher" role="button" tabindex="0" aria-label="Open Intercom Messenger" aria-live="polite"><div class="intercom-lightweight-app-launcher-icon intercom-lightweight-app-launcher-icon-open"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M28 32s-4.714-1.855-8.527-3.34H3.437C1.54 28.66 0 27.026 0 25.013V3.644C0 1.633 1.54 0 3.437 0h21.125c1.898 0 3.437 1.632 3.437 3.645v18.404H28V32zm-4.139-11.982a.88.88 0 00-1.292-.105c-.03.026-3.015 2.681-8.57 2.681-5.486 0-8.517-2.636-8.571-2.684a.88.88 0 00-1.29.107 1.01 1.01 0 00-.219.708.992.992 0 00.318.664c.142.128 3.537 3.15 9.762 3.15 6.226 0 9.621-3.022 9.763-3.15a.992.992 0 00.317-.664 1.01 1.01 0 00-.218-.707z"></path></svg></div><div class="intercom-lightweight-app-launcher-icon intercom-lightweight-app-launcher-icon-minimize"><svg viewBox="0 0 16 14" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M.116 4.884l1.768-1.768L8 9.232l6.116-6.116 1.768 1.768L8 12.768.116 4.884z"></path></svg></div></div></div><div class="PopperContainer-sc-1f2bqxs-0 UGDLy" data-popper-reference-hidden="false" data-popper-escaped="false" data-popper-placement="bottom-start" style="position: absolute; inset: 0px auto auto 0px; transform: translate(916.8px, 540.8px);"></div><div class="PopperContainer-sc-1f2bqxs-0 UGDLy" data-popper-reference-hidden="true" data-popper-escaped="true" data-popper-placement="top-start" style="position: absolute; inset: auto auto 0px 0px; transform: translate(916.8px, 238.4px);"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div></body></html>