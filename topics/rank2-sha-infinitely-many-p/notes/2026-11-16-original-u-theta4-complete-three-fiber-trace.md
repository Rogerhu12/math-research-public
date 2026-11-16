# 原 UΘ⁴ 的完整三纤维迹与真实质量

日期：2026-11-16。**状态：同原来源的完整有限代数计算已成功；下列质量和两层迹身份已付。没有给任何新余项赋算术中央零。**

## 实际来源与回执

[公开 run43870426107](https://github.com/Rogerhu12/math-research-public/actions/runs/43870426107)、
job133309825034于2026-11-16 12:52:02 UTC成功；源提交
[d5e37c59b7c93488772d4319e41d9a55a4429bde](https://github.com/Rogerhu12/math-research-public/commit/d5e37c59b7c93488772d4319e41d9a55a4429bde)。
producer为 ../scripts/check-r884-original-u-theta4-norm-three-trace.py，
无参数，只用标准库 Fraction 的有理运算，执行位置仅为公开 Actions。

输入恰为R884(C5)–(C6)的同一原U及全部因子。令X=x³，计算
\[
Q_{48}=\mathrm T_{\delta,48}(U\Theta^4)=\sigma^{48}q_b(X).
\]
原同源三纤维满足
\[
(X+4b)^3+27a^3X^2=0,\qquad a=x(\delta z).
\]
除以原线丛倍率$(\delta x)^{48}=3^{24}X^{16}$后，
全部正、负Newton矩逐项返回同一迹；未选取一根或替换来源。
b=1的每个X^j系数按b^{7-j}准确返回一般原单位b。

程序还用原四纤维
$x^4-4ax^3-8bx-4ab=0$
及$(x-4a)(x^3+b)=9bx$，独立计算目标degree48的完整二挠迹。
这些验证包括所有系数，并非数值取点或目标素数扫描。

结果摘要SHA256：
5e2e9bdafb00b70178499294aba0ff58588000a6fd7f748815440595d970b71b。
producer SHA256：
a943b4c799af265c703248ee9cf5abffe0b571023e534ddbef69ba4fe9d160fb。
完整八／九系数留在同次公开日志；此处只保存数学身份、来源和哈希。

## 由完整来源得到的身份

设$R_3=\sigma^3y$，保R884的原规范
\[
\mathcal U^{\rm new}_{144}=U\Theta^4+\frac{[4]^*C_9}{19656},
\qquad
\mathrm T_{\delta,3}C_9=-\frac{R_3}{4b}.
\]
则同一个实际迹为
\[
W_{48}:=\mathrm T_{\delta,48}\mathcal U^{\rm new}_{144}
=Q_{48}-\frac{[4]^*R_3}{78624b}.
\]
全计算给
\[
\deg q_b=7,\qquad q_b(0)=-\frac{1024}{819}b^7,
\qquad
\varepsilon(Q_{48})=0,\qquad
\varepsilon(W_{48})=\frac1{78624b},
\]
以及
\[
\mathrm T_{2,12}Q_{48}
=-\frac{\sigma^{12}(X^2+20bX-8b^2)}{19656b}
=\frac{[2]^*R_3}{19656b},
\qquad
\mathrm T_{2,12}W_{48}=0 .
\]
质量的正号也从准确的
$[4]^*R_3=-\sigma^{48}K_8(X)$
直接可见：$K_8$为首一八次多项式。
因此二挠new并不意味着这个原三挠迹的质量为零。

## 同一个除p行必须保留质量减项

R856(19)–(24)适用于这个原whole degree48偶截面。
对$p=6s-1>211$，原单位b及
$c_p=\binom{3s-1}{2s-1}b^s$，严格有
\[
j_{p+1}(W_{48})
\equiv48c_p\,\varepsilon(W_{48})
=\frac{c_p}{1638b}\ne0\pmod p.
\]
所以不能给$W_{48}$套用只在准确零质量格上定义的
$j_{p+1}/p$。合法的整数行是R856(39)的同一完整行
\[
\mathcal D_{48,p,1}(W)
=\frac{J_{p+1}(W)-H_pJ_2(W)-48C_pJ_0(W)}p,
\qquad C_p=L_2H_p
\]
并且须先在特征零中固定这一提升，再作约化。

尤其在原CM纤维，R856(36)及$L_2=-24b\,\partial_{g_2}$给
\[
H_p=0,\qquad C_p=(p+1)c_p^{\rm int},
\quad
c_p^{\rm int}=\binom{3s-1}{2s-1}b^s.
\]
把$C_p$提前换成只同余的$c_p^{\rm int}$会在除p后改变该行；
该改变不是可以忽略的高精度项。

上述事实没有使原四个中央读数互相矛盾。
它确定的是原U余项的真实质量和完整输入，
后续仍须与同一S/T/V低配对、全部cross及原高精度缺陷联立。
