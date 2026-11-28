# R150 补充：全部内部 ell 极点排除与 Vbar 正阶的有限权图

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。日期：2026-11-29（Asia/Taipei）。

## 1. 结论及当前范围

沿[全部e、k、u整单位](R150-appendix-unit211-W-b0-entire-positive-e-ray-exclusion-and-e-k-u-integral-units.md)，当前正确W/b0任一原点在每个1009位置满足v(e)=v(k)=v(u)=0，故Q=ek为单位、delta=1-Q整。

本稿证明：
$$
\boxed{v(\ell)\ge0.}
\tag{1}
$$
该证明不需要delta为单位。进一步，若
$$
r=V_{\rm bar}=uk+2,\qquad v(r)>0,
$$
则必有
$$
\bar u=1/2,\qquad \bar k=-4,\qquad\bar Q=2,\qquad\bar\delta=-1.
\tag{2}
$$
令s=2u-1，则z=s/r整，并且
$$
L:=\bar\ell=3/4+\bar z.
\tag{3}
$$
完整原q2/R6还排除
$$
\boxed{L\in\{0,1/4,1/2,7/4\}.}
\tag{4}
$$
因此ell、m、Ast、Phi在这个Vbar图都为单位；M的两个剩余零值及一般mu行为仍待处理。没有宣称整个Vbar边界或W已空。

## 2. 不需 delta 逆的统一极点原式

只假定u、Q为单位且v(ell)=-b<0。置
$$
\beta=u/\ell,\quad e=u-1,\quad
B=M/\ell^2=-Q+2\beta-\beta^2,
$$
$$
A=A_*/\ell=-Q+(4Q+2e)\beta,\quad
C_0=C_*/\ell^3.
$$
原m=ell(beta-1)，且
$$
C_0=A(\beta-1)^2+(Q-2e\beta)\delta.
$$
因此准确有
$$
C_0-BQ=\beta E,\qquad
E=(4Q+2e)(\beta-1)^2-2e\delta.
\tag{5}
$$
v(beta)=b>0，而A、B、Q均为单位，E整。原b0给
$$
T=\frac{uQ}{A}\mu,\qquad\mu=2\lambda-3.
$$
把完整q2除以ell三次，利用
$A_2+(3-4\lambda)=(\mu^2-1)/2$，得
$$
\boxed{
0=BQ(\mu^2-1)+2\beta E A_2
-\frac{8uQ^3\delta\beta^2}{A^2}\mu^2.
}
\tag{6}
$$
这条完整身份没有delta逆、M逆或任何未知首项逆。

若mu有极点，(6)第一项的mu平方严格最低，另两项至少多b、2b，矛盾。因此mu整，(6)又迫bar mu=±1。

若bar mu=1，则A2的剩余为5、B3的剩余为13，T单位。于是
$$
v(D)=-b,\quad v(K)=-2b,\quad v(M)=-2b,\quad v(m)=-b.
$$
R6两项MK平方、4m平方D三次的阶分别-6b、-5b，不可能相消。

若bar mu=-1，(6)及mu-1单位给
$$
v(\mu+1)\ge b.
$$
又
$$
B_3=(\mu+1)(\mu^2+5\mu+7)/2,
$$
故v(B3)≥b，而A2、T单位。于是v(D)=-b、v(K)≥-b，R6两项阶分别至少-4b、准确-5b，仍矛盾。这证明(1)，覆盖任意深delta首值，不需另一个极点计算。

## 3. Vbar 正阶的准确剩余坐标

原权公式为
$$
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)}.
$$
若r正阶，则bar k=-2/bar u。其分子剩余为
$$
4\bar e(2\bar u-1)/\bar u.
$$
e、u、k都已证单位；若bar u不等于1/2，ell必有极点，与(1)矛盾。因此(2)成立。

现在置
$$
s=2u-1,\quad r=uk+2,\quad
u=(1+s)/2,\quad k=2(r-2)/(1+s).
$$
原权式准确化为
$$
\boxed{
\ell=\frac{r^2-(s-1)(s-3)r/2+2s(s-1)}
 {r(r-2)}.
}
\tag{7}
$$
若v(s)<v(r)，其唯一最低项给ell为极点，已经排除。因此z=s/r整；把s=rz代入并准确取消r，得到正则式
$$
\ell=\frac{r-(rz-1)(rz-3)/2+2z(rz-1)}{r-2}.
\tag{8}
$$
取剩余即(3)。这里只取消已显示的r公因子，没有在剩余环中反演r。

完整原剩余权量为
$$
\begin{aligned}
u&=1/2,&Q&=2,&\delta&=-1,\\
m&=1/2-L,&M&=-2L^2+L-1/4,\\
A_*&=(7-4L)/2,&J&=1/2+2L,\\
T_0=\Phi&=1/2-2L,&P_{02}&=-1/4-L.
\end{aligned}
\tag{9}
$$
下文仅在明确相应单位后才作恢复；P02首值零并未预先删除。

## 4. 整个 L=0 与整个 Ast 深中心

### L=0

令b=v(ell)>0。由(9)，m、M、Ast均单位，C*剩余7/8。b0给v(T)≥b+v(mu)。完整q2的mu平方头为单位，先排mu极点；有限mu又由q2迫
$$
v(A_2)\ge b.
$$
因此bar A2=0，B3剩余为-lambda且非零。原
$$
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3
$$
给v(D)≥2b、v(K)=2b。R6第一项阶4b，而第二项至少6b，矛盾。这里保ell任意正阶。

### L=7/4

此时v(Ast)=gamma>0，ell、m、M仍单位，且
$$
\bar m=-5/4,\quad\bar M=-37/8,\quad
v(T)=v(\mu)-\gamma.
$$
若v(mu)≤0，q2的T平方项唯一最低，矛盾；mu=0也在下述常数项中排除。完整q2迫v(mu)=gamma、T单位，且
$$
\bar T^2=-41/16.
\tag{10}
$$
具体q2剩余为287/8+14T平方。由(9)的完整原D/K，
$$
\bar D=111/16,\qquad
\bar K=343/32-(73/4)\bar T.
$$
R6及(10)给
$$
588539+801248\bar T=0,
$$
模1009等价于 $146+51\bar T=0$。将其代入(10)，需
$$
16\cdot146^2+41\cdot51^2=447697\equiv710\ne0\pmod{1009},
$$
矛盾。没有倒Ast首值，全部深Ast层均排。

## 5. 整个深 m 与整个深 Phi 中心

### L=1/2

此时m的剩余为零，但M=-1/4、Ast=5/2仍为单位。q2的mu平方头为-43/200单位，故mu整。完整原剩余满足
$$
43\mu^2+100\mu+75=0,\qquad
1000K=-9\mu^3+150\mu^2+750\mu+875.
\tag{11}
$$
R6因M单位和m剩余零迫K=0。在(11)的二次商中，K的分子化为
$$
680775\mu+1066625,
$$
模1009为 $709\mu+112$。若它为零，二次式要求
$$
43\cdot112^2-100\cdot112\cdot709+75\cdot709^2
=30299667\equiv406\ne0\pmod{1009}.
$$
矛盾。因此全部深m阶数排除，没有除m。

### L=1/4

此时Phi剩余为零，但q2/R6没有Phi逆。q2的mu平方头为5/36单位，故mu整；其剩余准确给
$$
5\mu^2+27\mu+36=(5\mu+12)(\mu+3)=0.
$$
两个可能剩余及原R6值为
$$
\begin{array}{c|c|c|c}
\mu&D&K&R_6\\ \hline
-3&3/16&3/32&-45/16384\\
-12/5&21/200&151/4000&-59845/128000000
\end{array}
$$
两项均为1009单位，第二分子59845模1009为314，故都不可能为零。lambda剩余零的第一行完整保留，未提前将lambda当单位。此排全部Phi深相消。

## 6. 后继范围与保存

(4)现已全部证明。在Vbar正阶的剩余图，ell、m、Ast、Phi单位，而
$$
M=0\quad\Longleftrightarrow\quad8L^2-4L+1=0
$$
的两个剩余值尚未在本稿排除。一般L上mu仍可能有极点，必须用完整q/R的最高项先支付；不能直接假定lambda整。其余完整N5及singleton值必须继续同点保留。

本稿完全是新的原式纸面推理，没有执行旧射线、旧q/R投影、Phi链或任何冻结计算。统一极点引理与并行delta边界共用，避免同一已成门重复计算。原公式和本稿的各明确有理身份足以重建推导；未保存大系数或编码对象。普通ISP未完成。
