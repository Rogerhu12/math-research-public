# R328：另一完整 Gaussian 面积排除无常项的弱幂曲段类

日期：2026-11-15。**独立纸面原式推导。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R325](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md) 已经用真实朝内圆、正幅强块和有限频率校正支付一组原第四必要门。本稿继续检查同一圆未付的面积 $A_{-1,-3}$，而不是把该部分成功当作完整第四。

新面积第零外矩与旧面积共同给一个准确的混合恒等。对当前所有不含内部常数项的左右 $5/2$ 幂曲段，它重新迫原一层严格为正，故整个该类仍被阻断。朝向、分支点正负、反射侧、真实正幅组合和既有强块校正都不能避开这个新门。

范围不扩到一般弱 hook 核。特别，允许
$f=C_\nu+A_\nu|x-b_\nu|^{5/2}$ 时新增项真实不为零；本稿明确保留这一分叉，末节给出其准确原式而不先授可行。

主要来源：[R259 原 cubic 与右尾](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R304 原 Gaussian 门](R304-positive-one-history-remainder-excludes-disjoint-real-rank-one-circles.md)、[R306 弱 hook 身份](R306-derivative-rank-classification-and-overlapping-profile-Gaussian-obstruction.md)、[R317 完整 mixed 一层](R317-exact-weak-hook-mixed-correction-and-nonnegative-branch-obstruction.md)、[R308 真实弱核三阶圆](R308-genuine-derivative-rank-two-circles-with-one-hook-and-complete-third-range.md)、[R320](R320-complete-reflected-area-payment-and-outward-one-history-obstruction.md)及 R325。

## 1. 同一真实门与一般 mixed 记号

保持原实际闭 hook
$$
M=0,\qquad T=\kappa_H\mathfrak H,\quad \kappa_H\ne0,
$$
及小共振 Gaussian 芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100.
\tag{1}
$$
实紧 profiles 满足原三矩圆、共同右锚以及
$$
\mathfrak H(g;f,f)=0.
\tag{2}
$$
不假定第二个 hook。

对 $u=f\cos\theta+g\sin\theta$、$D=f\odot f-u\odot u$，写
$$
p=f',\quad q=f'',\quad v=u',\quad r=u'',\quad
F=q^2,\quad R=r^2,\quad d_0=F-R,\quad A=Jd_0=PD.
$$
完整 $D$ 三矩零保证 $A$ 与下述 $XD$ 真紧，但 $X(f,f)$ 一般有真实左尾。

设
$$
C=\int R\,d_0,\quad D_4=\int d_0^2,\quad
Y=\int vr\,d_0',\quad Z=\int xR\,d_0',
$$
$$
W=vq-pr,\quad
\mathcal J=\int W r q',\quad
\mathcal J_x=\int xWq'r',
$$
并引入一个真正的新混合量
$$
\boxed{\mathcal K=\int q'r'(q u-r f).}
\tag{3}
$$
它包含 profile 的值，不能仅由导数 rank 或旧三矩替代。

弱通量给 R317 的准确身份
$$
Y=-2C/3-2\mathcal J,\qquad
Z+C/2=-3(\mathcal J+\mathcal J_x).
\tag{4}
$$
若旧完整 $A_{-2,-3}$ 第1外矩已为零，则
$$
Z=C,\qquad
\mathcal J_x=-C/2-\mathcal J.
\tag{5}
$$
以上对当前真实 $u$ 成立，不是把各内部非合法单包各自设为三矩零。

## 2. 两个原第零面积，逐项保留非紧 primitive

沿原规范
$$
P=\Phi_{r_0},\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},
$$
$$
\mathcal A_X=I_0\{u,[X,P](u;D)\},\qquad X=L,U.
$$
完整 directed 量是
$$
H_0^X=-I_0(XD,PD)+2I_0\{u,X(u,PD)\}.
$$
因为原 cubic $F_{P,0}(u)=I_0(u,P(u,u))$ 恒零，沿紧方向 $XD$ 变分准确给
$$
-I_0(PD,XD)+2I_0\{u,P(u,XD)\}
=-I_0(XD,P(f,f)).
$$
因此
$$
\boxed{
2\mathcal A_X=H_0^X+I_0(XD,P(f,f)).
}
\tag{6}
$$
此处不能将非紧的 $P(f,f)$ 换成零尾版本。

### 2.1 $L$ 行

原二导与 cubic 是
$$
(L(f,f))''=(f-xp)q'-\frac{xF+P(f,f)}2,\qquad
F_{L,0}(u)=-\frac12\int vr^2.
$$
R325 已保真变分得
$$
H_0^L=Y-D_4/2+
\int d_0'(f-xp)q'-\frac12\int xF d_0'.
\tag{7}
$$
将原 $LD$ 二导代入(6)。两个最高导项合成
$$
2\int q'r'\{q u-r f-x(vq-pr)\}
=2\mathcal K-2\mathcal J_x.
$$
其余项中使用的是
$$
\int F'Jd_0=\int Fd_0=D_4+C,
$$
以及
$$
\frac12\int x(F'd_0-Fd_0')=-Z-C/2.
$$
二者均来自真实同锚积分；只有 $d_0$ 紧，不要求 $P(f,f)$ 紧。最终
$$
\boxed{
2\mathcal A_L=Y-Z+2\mathcal K-2\mathcal J_x.
}
\tag{8}
$$

### 2.2 $U$ 行

原二导为
$$
(U(f,f))''=(2xp-3x^2q)q'+2pq-2xF,
$$
且
$$
F_{U,0}(u)=\int(vr^2-xr^3).
$$
在(6)里保留全部 $d_0'$ 与 $F'$。含两个三阶导的项准确为
$4\mathcal J_x$；其余导数交叉为
$$
4\int qrW'-4\int xqr(rq'-qr').
$$
弱通量给
$$
\int qrW'=-\int(q'r+qr')W=-2\mathcal J,
$$
而第二个积分由(4)的原前一式化为 $-4Z-2C$。于是
$$
\boxed{
2\mathcal A_U
=4\mathcal J_x-8\mathcal J-2Y-Z-3C.
}
\tag{9}
$$
这一步没有把 $\int Wqr'$ 自动等同于 $\mathcal J$；该等同恰由原 $A_fW=0$ 与曲段边界分部积分支付。

将(4)、(5)代入(8)、(9)，得到
$$
\boxed{
\mathcal A_L=\mathcal K-\frac C3,\qquad
\mathcal A_U=-4\mathcal J-\frac{7C}{3}.
}
\tag{10}
$$

## 3. 真正的新 Gaussian 面积条件

原
$$
B_{-1}=d_*L+e_*U,\qquad B_{-3}=c_PP
$$
中
$$
d_*=\frac{6\kappa^3}{h_e},\quad
e_*=-\frac{\kappa(15t+1)}{4h_e},\quad
c_P=-\frac{\kappa(41t^2+27)}{216h_e^3}\ne0.
$$
由(10)，其完整第零外矩除去非零 $c_P$ 后是
$$
\boxed{
\mathcal A_Z
=d_*\mathcal K-4e_*\mathcal J
-\frac{d_*+7e_*}{3}C.
}
\tag{11}
$$
完整第四要求它为零。它没有在 R325 的三条 directed 行中自动被支付：单个 directed 行零不等于对应的对称与反对称两个部分分别零。

式(11)是作用于整个实际 profiles 的准确身份；没有只保最高导，没有舍去 $C^2$ 余项，也没有把单个原对角 self 直接外推到 mixed。

## 4. 无常项的左右幂曲段给同一个严格比值

现在只取必要相位 $\theta=\pi/2$，所以 $u=g$。考虑下列明确类：

- $W$ 的支撑包含于有限个严格内部曲段；
- 每个曲段上
  $$
  f(x)=A_\nu|x-b_\nu|^{5/2},
  $$
  $x-b_\nu$ 的符号在该段固定，且 $g=w_\nu$ 内部紧支撑；
- 外 cutoff 区上 $g=0$；
- 其它修正区域由真实 rank-one 紧 profiles 组成，所以那里
  $g'f''-f'g''=0$ 且 $f''g-g''f=0$。

这是 R308 的无常项幂段、R320／R325 的强矩补包和高频强控制块所满足的真实类。任意有限完整副本、两种朝向、反射侧或正四次组合仍在此类。不把一般 $W=0$ 的仿射偏移区域冒成这里的 rank-one profiles。

置 $s=|x-b_\nu|$。两种朝向都给
$$
qq'=\pm\frac{225A_\nu^2}{32},\qquad
pq'=\frac{75A_\nu^2}{16}s,
$$
故
$$
\mathcal J_\nu
=-\frac{75A_\nu^2}{16}\int s(w_\nu'')^2<0
$$
只要该曲段 $w_\nu\ne0$。

另一方面
$$
\mathcal K_\nu
=\int qq'w_\nu w_\nu'''
-\int f q'w_\nu''w_\nu'''.
$$
第一项是常数乘 $\int w_\nu w_\nu'''=0$，第二项准确分部积分给
$$
\mathcal K_\nu
=\frac12\int(fq')'(w_\nu'')^2
=\frac{15A_\nu^2}{8}\int s(w_\nu'')^2.
$$
因此
$$
\boxed{
\mathcal K_\nu=-\frac25\mathcal J_\nu,\qquad
\mathcal K=-\frac25\mathcal J,\qquad \mathcal J<0.
}
\tag{12}
$$
左右朝向的符号在两处导数中准确补偿。所有其它 rank-one 区域对 $\mathcal J,\mathcal K$ 都为零。八副本的实幅度可能为负，但这两个量的原四次权仍为正；十二个 $g$ 翻号副本也保持(12)。

## 5. 新面积迫旧完整一层严格为正

由(11)、(12)，新面积零等价于
$$
\frac{\kappa}{h_e}
\left\{
\frac{5+63t}{5}\mathcal J+
\frac{7+81t}{12}C
\right\}=0.
$$
所以
$$
\boxed{
C=-\frac{12(5+63t)}{5(7+81t)}\mathcal J.
}
\tag{13}
$$
这不是可独立选择的 quartic 常数，而是同一实际圆新增的必要关系。

若原三条 directed 门也零，则 R317/R325 的完整一层为
$$
[\sigma h^{-2}j^0]\mathscr R_{-3,\pi/2}
=B_\kappa\Psi,
$$
$$
\Psi=\frac{N(t)}{24P(t)}D_4+\mathcal J+\frac7{12}C,
$$
$$
B_\kappa=
\frac{(41t^2+27)P(t)}
{2592h_e^3(51t^2+2t+8)}>0,
$$
$$
N(t)=16+184t-1713t^2-2475t^3-4590t^4,
$$
$$
P(t)=8+114t-169t^2+231t^3-612t^4.
$$
代入(13)得到
$$
\boxed{
\Psi=
\frac{N(t)}{24P(t)}D_4
-\frac{36t}{5(7+81t)}\mathcal J>0.
}
\tag{14}
$$
这里 $D_4=\int\{(f'')^2-(g'')^2\}^2\ge0$，
$N,P>0$，$t>0$，而(12)给 $\mathcal J<0$。特别有明确严格下界
$$
[\sigma h^{-2}j^0]\mathscr R_{-3,\pi/2}
\ge
B_\kappa\frac{36t}{5(7+81t)}(-\mathcal J)>0.
\tag{15}
$$
该值保留真实 local、chain、history 及原 gauge 偶部商，不会被其它 Gaussian 字或中心入值吸收。

**定理。** 第4节无常项的真实弱幂曲段类，在(1)的小共振芽上不能满足完整第四 ruling。若旧面积、新面积或三条 directed 门任一不满足，已失败；若它们全部满足，(15)仍失败。该结论不限制分支点正负，也不限制曲段相对于反射中心朝内或朝外。

R325 的构造不受逻辑否定：它确实支付了其明确列出的门。但在该构造已令 $\Psi=0$ 时，本稿证明新面积(11)必然非零。不能从 R325 的部分支付越过这一后继门。

## 6. 一般弱核还有一个真实不同的自由

$A_f=0$ 的非仿射曲段一般允许
$$
f(x)=C_\nu+A_\nu|x-b_\nu|^{5/2}.
\tag{16}
$$
内部常数 $C_\nu$ 不改 $p,q,q'$，所以弱 hook 通量、$\mathcal J$ 与 R319 的方向第零矩仍不变。但它改变(3)：
$$
\boxed{
\Delta\mathcal K_\nu
=\frac{C_\nu}{2}\int q''(w_\nu'')^2
=-\frac{15A_\nu C_\nu}{32}
\int |x-b_\nu|^{-3/2}(w_\nu'')^2.
}
\tag{17}
$$
该系数对非零曲段严格非零，且可随实际内部常数改变符号。因此不能把(12)或(14)外推到(16)。

实际紧 profile 必须把这个内部常数接回零 collar。它会改变原三矩和其它 quartic 值，不能任意指定(17)而不支付这些变化。后继需把常数的真实 cutoff、矩回补、旧面积、兼容量和同一有限频率控制联合起来。

本稿只完成新原面积身份、无常项类的严格第四否定，以及(17)这个准确未排通道。没有把一个可调局部系数当作完整第四可行性。
