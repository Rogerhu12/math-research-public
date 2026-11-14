# R239 附录：出生一规范相位完整四次中间系数的全参数严格正性

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

状态：本文给出一个全参数的严格代数引理。它保留完整二维行列式中的两个平方项、交叉项和四次负项；不由有限参数扫描推断符号。对下述出生一规范相位，完整四次式的中间系数 $\mathcal P_2$ 严格为正，并有明确正下界。另两个中间系数及实际模型的共同源归一化须分别处理；本文不单凭这一系数宣布整个矩阵比较或普通 ISP 完成。

## 1. 参数、真实低比可行条件及完整四次式

设实数 $n,m\ge2$，$u,\eta,t>0$，并定义
$$
a_0=n-u\eta>0,\qquad b_0=m-\eta>0,
$$
$$
J=u(\eta+m+2)-n>0,\qquad
K=n+2-u(m-\eta)>0.
\tag{1.1}
$$
以下辅助记号 $M=m+1,N=n+1$ 不表示物理位总数。

规范高范数及剪切参数为
$$
a=\frac{m+2}{a_0},\qquad b=1,\qquad
c=\frac NM,\qquad d=\frac{N(n+2)}{M b_0},
$$
$$
X=1-au=-\frac J{a_0}<0,\qquad
Y=\frac d{cu}-1=\frac K{u b_0}>0.
$$
定义
$$
A=\frac c u,\qquad
\ell=-\frac{nX}{Mu},\qquad
\kappa=\frac{muY}{N},
$$
$$
R=A-\ell t>0,\qquad T=A^{-1}-\kappa/t>0.
\tag{1.2}
$$
实际完整低范数严格 log 凸时还有 $R,T<1$；本引理的中间系数正性只需 (1.2) 的正号。

令
$$
p=\frac1{uR},\quad Q=1,\quad r=u,\quad s=\frac{u^2}T,
$$
$$
x=\sqrt{\frac{\eta t}{M}}X,\qquad
y=\sqrt{\frac{\eta}{Mt}}Y.
\tag{1.3}
$$
特别 $xy=\eta XY/M<0$，两个剪切不是独立选取的。

对形式变量 $w$ 定义完整四次式
$$
\Lambda=(ac-b^2)+w(ad-bc)+w^2(bd-c^2),
$$
$$
\Phi=pQ(Qs-r^2)+wQr(ps-Qr)+w^2rs(pr-Q^2),
$$
$$
\begin{aligned}
\mathcal P(w)={}&Q\Lambda\Phi
-wpQ^3r(c+wd)(r+ws)x^2\\
&-wQ^2r^2s(a+wb)(p+wQ)y^2\\
&-2wpQ^2rs(b+wc)(Q+wr)xy
-w^2pQ^3r^2s x^2y^2.
\end{aligned}
\tag{1.4}
$$
这正是[完整 shear 行列式](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)使用的同一四次式。记 $\mathcal P_2=[w^2]\mathcal P(w)$。

**定理。** 对 (1.1)–(1.3) 的全部参数，严格有 $\mathcal P_2>0$。结论不限于整数 $n,m$，不要求对物理组大小取有限样本。

## 2. 中间系数仅含一次 Laurent 参数

先置
$$
L_0=ac-1,\quad L_1=ad-c,\quad L_2=d-c^2,
$$
$$
h_X=\eta X^2/M,\quad h_Y=\eta Y^2/M,\quad h_{XY}=\eta XY/M.
$$
直接从完整 (1.4) 提取 $w^2$，清除正单项式分母，准确得到
$$
\begin{aligned}
\frac{RT}{u}\mathcal P_2={}&
L_0u^2(1-R)+L_1u(1-RT)+L_2(1-T)\\
&-(cu+dT)x^2-u^2(auR+1)y^2\\
&-2u(u+c)xy-u^2x^2y^2.
\end{aligned}
\tag{2.1}
$$

代入 $R=A-\ell t$、$T=A^{-1}-\kappa/t$ 及 (1.3)，只剩
$$
\boxed{\frac{RT}{u}\mathcal P_2=K_+t+K_0+K_-/t.}
\tag{2.2}
$$
其中
$$
K_+=\ell u^2(L_0+L_1/c)-h_Xu(c+d/c),
$$
$$
K_-=\kappa(cL_1+L_2)-h_Yu^2(ac+1),
$$
$$
\begin{aligned}
K_0={}&L_0u^2(1-A)-L_1u\ell\kappa+L_2(1-A^{-1})\\
&+h_Xd\kappa+h_Yau^3\ell-2u(u+c)h_{XY}-u^2h_Xh_Y.
\end{aligned}
\tag{2.3}
$$
最后一项就是完整四次剪切负项，未删除。

## 3. 三个清分母后的准确因子式

定义正分母和辅助正数
$$
D=b_0M^2a_0,\qquad
V=1+u(\eta+1),\qquad \Delta=Mu-N,
$$
$$
H_+=M+N+\eta N,\qquad H_-=M+N+\eta uM,
$$
$$
C_0=V+3(n+m)+4=3(M+N)-1+u+u\eta.
$$
准确有
$$
J=V+\Delta,\qquad K=V-\Delta.
$$

式 (2.3) 逐项清分母给
$$
\boxed{N_+:=DK_+=u(2M+b_0)JH_+>0,}
\tag{3.1}
$$
$$
\boxed{N_-:=DK_-=(2N+a_0)KH_->0,}
\tag{3.2}
$$
以及下列保留全部项的常数分解：
$$
\boxed{
N_0:=DK_0=-C_0JK+
V\left[Jb_0(u\eta+1)+Ku(m+2)(\eta+1)\right].
}
\tag{3.3}
$$
这些都是有理函数恒等式。可直接把 (1.1)–(1.3) 代入核验；也可先以 $\Delta$ 为变量，将 $N_0$ 的三次多项式按 $V^2-\Delta^2=JK$ 相除，余式恰为 (3.3) 所列的两个正项。

(3.1)–(3.3) 是完整系数的分解，没有引入对低范数或剪切的额外放松。

## 4. 可行的两个低比支付唯一负部

由 (1.2) 的两个正号，
$$
A\kappa<t<A/\ell,
$$
故 $\ell\kappa<1$。利用实际定义，
$$
\ell\kappa=\frac{nmJK}{MNu a_0b_0}.
$$
因此
$$
\boxed{JK<\frac{MNu a_0b_0}{nm}.}
\tag{4.1}
$$
这个约束来自同一个 $t$ 的两个低比；不能把它换成独立局部正数的自由选择。

由 $0<a_0<n$、$0<b_0<m$，(3.1)、(3.2)、(4.1) 给
$$
\begin{aligned}
\frac{N_+N_-}{(JK)^2}
&=\frac{u(2M+b_0)(2N+a_0)H_+H_-}{JK}\\
&>\frac{nm}{a_0b_0}
\frac{(2M+b_0)(2N+a_0)}{MN}H_+H_-\\
&>4H_+H_-.
\end{aligned}
$$
即
$$
\boxed{2\sqrt{N_+N_-}>4JK\sqrt{H_+H_-}.}
\tag{4.2}
$$

还须明确支付右侧与 (3.3) 负系数的比较。
由 $u\eta<n$ 以及 $K>0$，
$$
um=u(m-\eta)+u\eta<n+2+n=2N.
$$
因为 $m\ge2$，得到 $u<N$，特别 $u<MN$。
令 $S_0=M+N$。准确计算
$$
H_+H_--\left(S_0+\eta\sqrt{uMN}\right)^2
=S_0\eta\left(\sqrt N-\sqrt{uM}\right)^2\ge0.
$$
故
$$
\sqrt{H_+H_-}\ge S_0+\eta\sqrt{uMN}\ge S_0+\eta u.
$$
于是
$$
\boxed{
4\sqrt{H_+H_-}-C_0
\ge S_0+1-u+3\eta u>0.
}
\tag{4.3}
$$
每一项只用已列的真实参数条件；没有隐藏随高度变化的常数。

## 5. 严格中间系数与显式正下界

由标量 AM–GM，
$$
N_+t+N_-/t\ge2\sqrt{N_+N_-}.
$$
将 (3.3)、(4.2)、(4.3) 合并，得到
$$
\boxed{
\begin{aligned}
\frac{DRT}{u}\mathcal P_2
>{}&JK\left[M+N+1-u+3\eta u\right]\\
&+V\left[Jb_0(u\eta+1)+Ku(m+2)(\eta+1)\right]>0.
\end{aligned}
}
\tag{5.1}
$$
因为 $D,R,T,u>0$，定理得证。

这个证明处理所有可行 $t$，不是只检查区间端点或对称点。它也没有先假定另两个中间系数为正。

## 6. 应用范围和独立核验

[实际三正参数归一化](R239-appendix-birth-one-actual-three-positive-parameter-normalization.md) §§1–4 已从同一个实际 $Z_j$ 推出 (1.1)–(1.3)，并付清同一个完整源的合同及逐层共同几何因子。因此本稿支付任意两个等权组加一异常位、出生一、$n,m\ge2$ 的规范完整四次式 $w^2$ 系数。$z=1$ 已由两权全高度定理覆盖，$0<z<1$ 由该归一化稿的实际组交换处理。其余 $w$、$w^3$ 系数仍须各自证明；一般其他出生不自动具备本稿参数关系。

[配套精确恒等式程序](../notes/2026-11-14-birth-one-normalized-middle-quartic-identity-check-0c.py)从通用完整四次式独立提取 $w^2$ 系数，断言 (2.1)、(2.2)、(3.1)–(3.3) 和 (4.1) 所用等式。所有运算为 SymPy 有理函数恒等式；全参数符号结论由 §§4–5 的不等式证明承担，无有限取样或浮点判号。
