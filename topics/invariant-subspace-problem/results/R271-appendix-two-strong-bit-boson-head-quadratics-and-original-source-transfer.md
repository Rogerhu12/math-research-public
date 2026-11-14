# R271 附录：两强位—玻色模型的完整头二次型与原同源运输

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220。

状态：**已证明。** 本稿继续[原尾强位回缩](R271-appendix-original-tail-strong-bit-boson-retraction-and-same-source-high-schur-bound.md)中首次保留两道 primitive 桥的 $k=2,s=0$ 情形。对一个明确的原连续尾源类，保留整个实际头 $A_m$ 及全部头自由度，将模型完整右费化为 $2d-1$ 个标量未知量的正二次最小化，将裸费化为 $d$ 个未知量的正二次最小化。两者都有显式正范数和公式，不先投掉最前两位，也不以自由四头矩阵替换 $A_m$。

本文没有证明这两个头二次型在实际窄源上满足所需一致比较；混合逆 $\lambda_{\rm flat}$ 和固定实际 $W$ 来源仍须另外验证。

## 1. 同一个明确的原源及全部运输常数

保留 $m\ge5,d=2^m$、原合法 $q$ 和原实际头 $A=A_m$。前两个真实尾权为
$$
a=(m+1)^{-2},\qquad b=(m+2)^{-2},\qquad
\gamma=\sqrt{ab},\qquad
\tau=\sqrt{a/b}=\frac{m+2}{m+1}.
$$
在随后 $q$ 个原相邻配对上取上一稿的单位暗向量之积 $h_{\rm mid}$，远尾从
$$
J=m+2+2q
$$
开始。记
$$
S=S_J,\qquad
\beta=\frac{\sqrt S}{\gamma},\qquad
K=\frac A\gamma,\qquad
\epsilon=\frac{4d^2}{J+1}<1.
\tag{1.1}
$$
$K$ 是实际头的准确标量倍数，所有其幂与自由头坐标均保留。

令
$$
f_q=\Omega_{\{m,m+1\}}\otimes h_{\rm mid}\otimes\Omega_{\{j\ge J\}}.
$$
它是原单位 primitive 向量。给定任意
$$
u\in(\ker A)^\perp=\operatorname{span}\{e_1,\ldots,e_{d-1}\},
$$
全文始终使用同一个原首源
$$
\boxed{r(u)=Au\otimes f_q.}
\tag{1.2}
$$
它属于原 $\mathscr R_q$；没有先在未知原源上施加不保 $D$ 的前两位真空投影。

为了得到一个可完全写开的对称模型，先在前两强位作准确的对角交织
$$
B_{\rm str}|i,j\rangle
=(\gamma/a)^i(\gamma/b)^j|i,j\rangle
\qquad(i,j\in\{0,1\}).
$$
其矩阵对角为 $1,\sqrt{b/a},\sqrt{a/b},1$，并且
$$
(aE_1+bE_2)B_{\rm str}
=B_{\rm str}\gamma(E_1+E_2),\qquad
\|B_{\rm str}\|=\|B_{\rm str}^{-1}\|=\tau.
\tag{1.3}
$$
它在真空上为恒等。将它与上一稿的原暗对和远尾回缩组合，再将整个方程除以 $\gamma$，得到标准模型
$$
\boxed{\mathfrak D=E_1+E_2+\beta\mathfrak b,\qquad
\mathfrak L=K+\mathfrak D,\qquad
\widehat r=Ku\otimes\Omega.}
\tag{1.4}
$$
模型总源孔数为零。除以 $\gamma$ 同时作用于头、尾和首源，故不改变一个可行链的物理范数。

模型到原问题的截面及反向回缩统一有界：
$$
\overline\kappa=\frac{\tau}{\sqrt{1-\epsilon}},
\qquad
\overline R=\tau\exp\!\frac2{m+3},
\qquad
\boxed{\chi_2=\overline R\,\overline\kappa.}
\tag{1.5}
$$
尤其
$$
\boxed{
\chi_2^2=
\left(\frac{m+2}{m+1}\right)^4
\frac{\exp(4/(m+3))}{1-4d^2/(m+2q+3)}.
}
\tag{1.6}
$$
这是两真实强位不同权的已付代价。不能因为相邻权接近就直接把 (1.3) 省去。

## 2. 模型全部完整链的参数化

用普通多项式写标准玻色空间：
$$
y^r=\sqrt{r!}\,e_r,\qquad \|y^r\|^2=r!.
$$
两个强位变量 $x_1,x_2$ 的次数各至多一，四个强位单项式标准正交。于是
$$
\mathfrak D=\partial_{x_1}+\partial_{x_2}
                     +\beta\partial_y
$$
在这个物理多项式空间上成立。置 $z=y/\beta$。

完整模型右链 $c$ 的首源为 $Ku$；将其与左段 $u$ 拼成
$$
Z=u-c
$$
便有 $\mathfrak LZ=0$。反向同样成立，只要保留原逐头旗与右支撑 $1,\ldots,d$。

两个强位的交换是酉对称，保持源、全部核旗、完整方程和高输入空间。故完整最小链及裸最小链可取在交换固定空间中；任何非对称部分只增加相应正交能量。

在该固定空间内，全部完整链由
$$
v\in\mathbb C^d,\qquad
w\in W_{d-1}:=\operatorname{span}\{e_0,\ldots,e_{d-2}\}
\tag{2.1}
$$
唯一参数化为
$$
\boxed{
Z(y,x_1,x_2)=
e^{-Kz}\left[
u+v(x_1+x_2-2z)
+w(x_1-z)(x_2-z)
\right].
}
\tag{2.2}
$$
右链是 $-P_{>0}Z$。

证明可在 $y=0$ 处读出初值 $u+v(x_1+x_2)+wx_1x_2$。方程
$$
\beta\partial_y Z=-(K+E_1+E_2)Z
$$
有唯一的有限幂解
$e^{-(K+E_1+E_2)y/\beta}$ 作用于此初值，即 (2.2)。
$u$ 的首头自由分量仅产生一个零孔常量，不影响右链；已按原左最小条件把它置零。

原第2段的最高允许头是 $d-2$，所以 $w\in W_{d-1}$ 恰是必须保留的约束；$v$ 的全部 $d$ 个头坐标均自由。因为 $K$ 每次至少降低一个头位置，展开后的第 $p$ 孔项均在头 $W_{d-p+1}$ 中。$K^d=0$ 及 $K^{d-1}w=0$ 还保证最高孔数至多 $d$。

全部逐头删除核也成立：在完整 $\mathfrak L$ 核上
$\mathfrak D^hZ=(-K)^hZ$，而第 $i$ 个头坐标在 $h=d-i$ 时准确为零。反向，上述 $y=0$ 初值读取穷尽了所有物理完整链，没有删去一个高或低自由头。

## 3. 完整右费的显式正二次型

对 $r\ge1$，定义
$$
F_r(u,v,w)=K^ru+2rK^{r-1}v+r(r-1)K^{r-2}w.
\tag{3.1}
$$
$r=1$ 时最后一项按零处理。另记
$$
G_r(v,w)=K^rv+rK^{r-1}w,\qquad G_0(v,w)=v.
$$
按强位占据 $0,1,2$ 分组，(2.2) 的三个物理系数分别为
$$
e^{-Kz}(u-2zv+z^2w),\qquad
e^{-Kz}(v-zw)\ \text{（两份）},\qquad
e^{-Kz}w.
$$
它们按强位正交，各玻色幂也正交。因此同一个完整右范数准确等于
$$
\boxed{
\begin{aligned}
\Phi_u(v,w)={}&
\sum_{r=1}^{d}\frac{\|F_r(u,v,w)\|^2}{r!\,\beta^{2r}}\\
&+2\sum_{r=0}^{d-1}
           \frac{\|G_r(v,w)\|^2}{r!\,\beta^{2r}}\\
&+\sum_{r=0}^{d-2}
           \frac{\|K^rw\|^2}{r!\,\beta^{2r}}.
\end{aligned}
}
\tag{3.2}
$$
于是模型真正完整费为
$$
\boxed{
\widehat\lambda(\widehat r)^2
=\Lambda(u):=
\min_{\substack{v\in\mathbb C^d\\w\in W_{d-1}}}\Phi_u(v,w).
}
\tag{3.3}
$$
这是一个 $2d-1$ 维正二次最小化。零阶项含
$2\|v\|^2+\|w\|^2$，故其自由变量的 Hessian 正定，最小者唯一。实际头幂中的全部长跃迁、carry 和原自由头仍在 (3.2) 中。

## 4. 高输入是逐孔一条明确的原度量直线

模型 primitive 出生只有 $0,1,2$。第 $p\ge2$ 孔层的高输入
$$
\ker\mathfrak D^{p-1}\cap\mathsf H_p
$$
是一维，生成元为
$$
(x_1-z)(x_2-z)y^{p-2}.
\tag{4.1}
$$
这也可由模型满射和层维数 $1,3,4,4,\ldots$ 直接验证。

在交换固定块中，用强位占据 $0$、对称占据 $1$、占据 $2$ 的标准正交基，(4.1) 的方向可写成
$$
\boxed{
g_p=
\left(
\frac{\sqrt{p(p-1)}}{\beta^2},
-\frac{\sqrt{2(p-1)}}{\beta},
1
\right).
}
\tag{4.2}
$$
其头系数必须属于 $W_{d-p+1}$；这正是原第 $p$ 段的高输入头旗。

(2.2) 中由 $w$ 产生的全部右链，在每一孔层都沿 (4.1) 的高方向。因此原低投影把这个完整 $w$ 列准确杀掉。计算裸费时仍须在每个孔层使用 (4.2) 的**正交**投影，不可仅删去物理双强位坐标。

## 5. 裸费的 d 维正范数和

现在令 $w=0$，并记
$$
Y_p(v)=K^{p-1}v,
$$
$$
F_p^0(u,v)=K^pu+2pK^{p-1}v,\qquad
T_p(u,v)=K^pu+pK^{p-1}v.
$$
第1孔层没有高输入，其能量为
$$
\beta^{-2}\|Ku+2v\|^2+2\|v\|^2.
\tag{5.1}
$$
对 $p\ge2$，提出共同因子
$(-1)^p/(\sqrt{p!}\,\beta^p)$ 后，物理向量为
$$
\bigl(F_p^0,-\sqrt{2p}\,\beta Y_p,0\bigr).
$$
将 (4.2) 乘 $\beta^2$，其平方范数为
$$
\boxed{\Delta_p=p(p-1)+2(p-1)\beta^2+\beta^4>0.}
\tag{5.2}
$$
与该向量的内积是
$\sqrt{p(p-1)}(F_p^0+2\beta^2Y_p)$。所以去掉高投影后的平方能量为
$$
\frac1{p!\beta^{2p}}
\left[
\|F_p^0\|^2+2p\beta^2\|Y_p\|^2
-\frac{p(p-1)}{\Delta_p}
             \|F_p^0+2\beta^2Y_p\|^2
\right].
$$
完整展开并合并交叉项，得到无减法损失的准确正式
$$
\boxed{
\frac{\beta^{2-2p}}{p!\Delta_p}
\left[
2(p-1)\|T_p\|^2
+\beta^2\|F_p^0\|^2
+2p\beta^4\|Y_p\|^2
\right].
}
\tag{5.3}
$$
定义
$$
\boxed{
\begin{aligned}
\Psi_u(v)={}&
\beta^{-2}\|Ku+2v\|^2+2\|v\|^2\\
&+\sum_{p=2}^d
\frac{\beta^{2-2p}}{p!\Delta_p}
\left[
2(p-1)\|K^pu+pK^{p-1}v\|^2\right.\\
&\hspace{35mm}
+\beta^2\|K^pu+2pK^{p-1}v\|^2\\
&\hspace{35mm}
\left.+2p\beta^4\|K^{p-1}v\|^2
\right].
\end{aligned}
}
\tag{5.4}
$$
则真正模型裸费为
$$
\boxed{
\widehat\alpha(\widehat r)^2
=\mathcal A(u):=\min_{v\in\mathbb C^d}\Psi_u(v).
}
\tag{5.5}
$$
零阶 $2\|v\|^2$ 保证这个最小化严格正定。这里不要求各 $K^{p*}K^p$ 交换，亦未限制 $v$ 的自由头位置。

证明 (5.5) 使用上一稿的准确距离刻画：裸费是完整可行链到整个高输入空间的最小距离。式 (4.1)–(4.2) 精确算出各孔的距离；$w$ 列已经处于该高空间，所以没有剩余的 $w$ 最小化。两条自由位反对称部分与源及所有显示项正交，故最小者中为零。

特别，$\Lambda(u)-\mathcal A(u)$ 就是模型同源完整高能量。完整问题只能用一个共同的 $w$ 经各次 $K^{p-2}$ 调整所有孔；裸问题允许对各孔独立取高方向的距离。这一相容性差已全部保留在 (3.3)、(5.5) 中。

## 6. 回到原尾的同一首源和新 H2° 能量

模型左侧仅有零孔层；因 $u\perp\ker K$，其真正左最小费准确为
$$
\widehat\mu(\widehat r)^2=\|u\|^2.
\tag{6.1}
$$
应用上一稿的精确回缩与 (1.3) 的强位交织，对 (1.2) 的**同一个原源**有
$$
\boxed{
\overline R^{-2}\Lambda(u)\le\lambda(r(u))^2
                   \le\overline\kappa^2\Lambda(u),
}
$$
$$
\boxed{
\overline R^{-2}\mathcal A(u)\le\alpha(r(u))^2
                   \le\overline\kappa^2\mathcal A(u),
}
$$
$$
\boxed{
\overline R^{-2}\|u\|^2\le\mu(r(u))^2
                   \le\overline\kappa^2\|u\|^2.
}
\tag{6.2}
$$
这些费用中的原有限头均为原 $A_m$。

记原新末块能量
$$
\mathcal E_H(r)=
\left\langle
(H_2^\circ)^{-1}\mathcal R\mathcal G^\dagger\zeta(r),
\mathcal R\mathcal G^\dagger\zeta(r)
\right\rangle
=\lambda(r)^2-\alpha(r)^2.
$$
则
$$
\boxed{
\overline R^{-2}\Lambda(u)
-\overline\kappa^2\mathcal A(u)
\le\mathcal E_H(r(u))
\le
\overline\kappa^2\Lambda(u)
-\overline R^{-2}\mathcal A(u).
}
\tag{6.3}
$$
左界可以再与零取最大；不把能量差的加性失真删去。

同样，原两形式比与两个准确头二次型满足
$$
\boxed{
\chi_2^{-2}
\frac{\Lambda(u)+\|u\|^2}{\mathcal A(u)+\|u\|^2}
\le
\frac{\lambda(r(u))^2+\mu(r(u))^2}
     {\alpha(r(u))^2+\mu(r(u))^2}
\le
\chi_2^2
\frac{\Lambda(u)+\|u\|^2}{\mathcal A(u)+\|u\|^2}.
}
\tag{6.4}
$$
当 $m\to\infty$ 且 $d^2/q\to0$ 时，显示的 $\chi_2\to1$。这只说明本稿的全部回传费用趋近等距；它不预先控制中间那个真实比值。

## 7. 仍须解决的实际内容

式 (3.3)、(5.5) 把本明确原源类的高费用变成两个保留完整 $A_m$ 的有限正二次型。可继续研究的对象是它们在
$$
K=A_m/\sqrt{a_ma_{m+1}},\qquad
\beta^2=S_{m+2+2q}/(a_ma_{m+1})
$$
这些**相互绑定的原参数**上的准确比较，而不是自由改变头 carry 与玻色强度后的有限反例。

本稿没有把同源混合量
$\|F_{\rm right}^*J_{\rm left}^{-1}r(u)\|$
改成另一个模型源的费用；也没有证明 $r(u)$ 来自固定实际 $W$。最前两位在完整模型中始终保留全部占据态，不能把其源端真空条件升级为一个保 $D$ 或保 $W$ 的投影。

新 $H_2^\circ$ 能量含原零首源低自由度的最优调整；它仍不等于只用纯高输入修复的
$\|S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)\|^2$。
一般实际窄源、无权 $N=M$ 及普通 Hilbert ISP 继续开放。
