# R157 — 原 Atkin–Lehner/Cartan 反射与 CM 极点同步

**状态：已证明。日期：2026-11-12。**

对 R154 的 $E=389\mathrm a1$ 完整类群商及原 Hecke 行 B，
实际 $w=w_{389}$ 满足
$$
 \Psi_Dw=-\Psi_D,\qquad
 \widetilde g_{D,p}w=-\widetilde g_{D,p},\qquad wB=-B.
$$
prime-level 迹给 Fricke 特征值 $-a_{389}=-1$；
$\#E(\mathbb F_3)=6$、$\#E(\mathbb F_7)=13$ 排掉有理挠点，
故没有尖点平移。BP 的实际加法点值等式支付互反函数的
严格反号，未忽略原函数常数。

写 $n=NB$、$A=D_1B$、$F_2=D_2B$、
$\mathscr D=A^2-nA-2nF_2$、$C=\mathscr D/n^2$。
对真实 Cartan 反射
$\nu_r\tau\nu_r^{-1}=\tau^{-1}$、$\nu_rB=\tau^rB$，有
$$
 \nu_rA=-A+rn,\qquad
 \nu_rF_2=F_2+(1-r)A+\binom r2n.
$$
由此准确得到
$$
                  w\mathscr D=\nu_r\mathscr D=\mathscr D,
              \qquad wC=\nu_rC=C.
$$
二次不变量下降至真实 Cartan normalizer 商及 w 商；
这不把原有向 $C_p$ 覆盖偷换为 normalizer 商的非 Galois
p 次覆盖。

原两个 CM 方向在类群商上由 $w$ 与复共轭相连；
保 Cartan 方向后，复共轭准确为 $\nu w$，具体纤维原点
可以多出已经保留的真实 Artin 平移 $\tau^r$。
因此整个纤维的 $D_2B=0$ 在两个方向严格等价。

w、Cartan 反射及其积在原 CM 四点轨道上均无固定点，
相应商在这些点 étale。以两个中心的同一个函数 $t=n$
作局部参数，实际 Laurent germs 满足
$$
                         C_-(t)=C_+(-t).
$$
双极点系数相同、单极点系数反号，极点阶及正则性同步。
这不是同一个 germ 的偶性，不强迫其奇次系数为零。
完整商上的原 CM 像为 $\mathbb Q$ 有理点，极点阶保持。

尚未证明原点一定是 C 的极点；两个共轭方向没有给两个
独立的二阶非零条件。

[完整证明](../notes/2026-11-12-actual-atkin-normalizer-and-cm-polar-jets.md)
含真实参数化、BP 常数、全部矩变换、原 CM 格/标记、
无固定点及极点 jet 的计算，并逐项核对
Buium–Poonen（2009）、Gross–Zagier（1986）与
Ribet–Stein（2017 作者版）的原始结论。
