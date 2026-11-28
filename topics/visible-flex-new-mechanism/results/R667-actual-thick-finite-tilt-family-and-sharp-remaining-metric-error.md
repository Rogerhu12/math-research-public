# R667：实际宏观倾斜厚闭族及其唯一剩余度量缺陷

2026-11-28。固定 $a=3/40,b=11/50,T=.03,\sin\vartheta=.36$。以下给一个显式的真实 $C^2$ 闭族：开握持区逐点固定且直径至少 $.201$，无对齐整像位移至少 $.3$，全相位 reach 至少 $.03$，整个族 $D<1$。它采用 [R655](R655-offset-rigid-cap-and-thick-inner-hold.md) 的两个实际刚件、[R662](R662-tilted-two-plane-global-tube-and-offset-cap-clearance.md) 的全法管定理，连接环带是准确指定的转动圆纬圈。归一目标 $\delta_{\rm hold}/D\ge.3$、reach$/D\ge.03$ 与固定握持三项已在同一个实物几何上成立。其唯一剩余的 $rr$ 度量各向异性，在最佳共同度量下全点误差小于 $.1003$、大于 $.05$。因此这给满足全部宏观几何约束的起点；它仍未达到题目的 $10^{-6}$ 等距门和同度量精化门。

## 实际姿态和全相位位置

令 $d_0=4/125=.032$，$H(t)=3t^2-2t^3$。规定
$$
 k(r)=\begin{cases}
 H((r-a)/d_0),&a\le r\le a+d_0,\\
 1,&a+d_0\le r\le b-d_0,\\
 H((b-r)/d_0),&b-d_0\le r\le b ,
 \end{cases}\qquad
 M=\frac{\vartheta}{\int_a^b k(s)\,ds/s},\qquad
 \omega(r)=M\int_r^b k(s)\,ds/s .
$$
$k$ 全局 $C^1$，两端 $k=k'=0$。令 $p=r\omega'=-Mk$、$Q=R_y(\omega)$，基相位为
$$
 X(r,\varphi)=rQ(r)e_r(\varphi),\qquad
 X_\alpha=R_z(\alpha)X(r,\varphi-\alpha),\quad 0\le\alpha\le\pi .
$$
准确内中心 $C=0$，$\omega(a)=\vartheta,\omega(b)=0$，$\omega',\omega''$ 在两个接圈均为零，因此实位置和全部二阶 jets 与刚性平盘匹配。接上 R655 的偏心刚外帽和回转刚内握柄，再对每一相位施以 $[R_z(\alpha)R_y(\vartheta)R_z(-\alpha)]^T$ 冻结握柄。三块在同一固定参数球面上组成随 $\alpha$ 在 $C^2$ 连续的真实闭族。

用 $0\le k\le1$、$\max |H'|=3/2$，可将全部费用用有理余量估计。因为两个过渡段 $H$ 的平均各为 $1/2$，
$$
\int_a^b k(s)\,ds/s
\ge \log(188/107)+.016/.107+.016/.22 .
$$
由 $\log x\ge2[y+y^3/3]$（$y=(x-1)/(x+1)>0$，此处 $y=81/295$）及 $\arcsin(.36)<.37$，得 $M<.472$。

## 真正第一、第二基本形式与全法管

令 $c=\cos\varphi,s=\sin\varphi,W=1+p^2c^2$。基相位有
$$
X_r=Q(e_r-pc\,e_z),\quad X_\varphi=rQe_\varphi,\quad
n=Q(e_z+pc\,e_r)/\sqrt W,\qquad g_X=Wdr^2+r^2d\varphi^2 .
$$
在正交单位切向 $X_r/\sqrt W,X_\varphi/r$ 上，第二基本形式的矩阵为
$$
 -\frac{pc}{r\sqrt W}I+
 \begin{pmatrix}
 -p'c/W^{3/2}&p s/(rW)\\
 p s/(rW)&0
 \end{pmatrix}.
$$
例如 $Q^TX_{rr}=-(p'+p/r)c e_z-(p^2/r)c e_x$，$Q^TX_{r\varphi}=e_\varphi+p s e_z$，$Q^TX_{\varphi\varphi}=-r e_r$，逐一与真单位法向内积即得。用 $|s|+|c|\le\sqrt2$，
$$
 \max_i|\kappa_i|\le |p'|+\sqrt2|p|/r
 <.472[(3/2)/.032+\sqrt2/.075]<31.1<100/3 .
$$
在外、内两个刚框中实际法向分别满足
$$
 \sqrt W\,n\cdot e_z=\cos\omega-p c^2\sin\omega>0,\qquad
 \sqrt W\,n\cdot R_y(\vartheta)e_z
      =\cos(\vartheta-\omega)+p c^2\sin(\vartheta-\omega)
      >.93-.472(.36)>0 .
$$
因此 R662 已给出整环带 $|t|<.03$ 的法管一一、内圈外侧与外圈内侧的全部偏移分隔。环带 $t=0$ 的外框柱半径不超过 $b$、高度满足 $|z|\le b\sin\vartheta=.0792$。内中心 $d=h=0$ 位于 R662 已核算的握柄实际姿态矩形内，故整个运动盘在 $.22$ 圆柱、$[-.08,.315]$ 高度内，且握柄全部真实偏移离外顶平面有正半径余量。R662 的凸外帽净空、R655 握柄自身的极点与柱段法管、真正外帽的法管逐项适用。因此全闭面嵌入，保持上述 reach、直径和固定开握持区。外帽的两个真球片分别支撑两个整像，有符号支撑差准确 $2(5/12)(.36)=.3$。这些都是整像及所有相位的结论。

## 两个宏观分离的端嵌入对一个固定材料度量准确等距

因为 $\cos^2(\varphi-\pi)=\cos^2\varphi$，在同一个材料球面上的 $\alpha=0,\pi$ 有
$$
 g_{rr}=1+p^2\cos^2\varphi,\quad
 g_{r\varphi}=0,\quad g_{\varphi\varphi}=r^2
$$
三张分量逐点相同。外帽使用同一材料参数，内握柄在两端只是其各自刚姿下的同一个带材料标识的刚件；二阶接圈保持同一材料经度。把各幅像刚性移到固定内握持框架也保持这些分量。因此已经得到**一对同一材料球上的精确等距、厚且宏观分离的完整闭嵌入**，其固定握持整像距离至少 $.3$。对中间 $0<\alpha<\pi$，旋转各向异性项通常改变；上述一对端点尚无达到题目指标的已知连续等距路径。

## 最佳共同度量、无法用重调圆倾斜率消掉的缺陷

在材料点 $(r,\varphi)$ 沿全部 $\alpha$，$g_{\alpha,rr}=1+p^2\cos^2(\varphi-\alpha)$ 遍历 $[1,1+p^2]$；$g_{r\varphi}=0,g_{\varphi\varphi}=r^2$ 全程准确。任意共同正定度量 $g_*$，即使允许非旋转或非对角形式，在向量 $\partial_r$ 上也须以一个正数 $e=g_{*,rr}$ 比较区间两个端值。最小化 $\max(|1/e-1|,|(1+p^2)/e-1|)$ 的解为 $e=1+p^2/2$。取整个目标
$$
g_0=(1+p^2/2)dr^2+r^2d\varphi^2
$$
正好达到该下界；真刚件上取自身固有度量即可与平边准确拼接。全域、全相位、最佳共同度量的最大相对二次型误差恰等于
$$
\varepsilon_{\rm opt}=M^2/(2+M^2)<.1003 .
$$
对同样两刚姿的任一同心转动圆纬圈角率有 $\vartheta\le\|r\omega'\|_\infty\log(b/a)$，因此整个该圆圈类的精确共同误差至少
$$
 \frac{\vartheta^2}{2\log^2(b/a)+\vartheta^2}>.05 .
$$
末式可用 $\vartheta>.36,~\log(44/15)<1.1$ 验证。取圆纬圈和角率的更细网格不能使其成为题目要求的等距解。

**对后继的真实固定度量门。** $g_0$ 的半径经线长甚至不足以支撑上述实际倾斜端姿。因为 $\int_0^1H^2=13/35$ 及 $\sqrt{1+x}\le1+x/2$，
$$
 S_0=\int_a^b\sqrt{1+p^2/2}\,dr
 \le .145+\frac{M^2}{4}\left(.145-\frac{44}{35}(.032)\right)<.151 .
$$
但 [R665](R665-end-tangent-and-length-cost-for-finite-tilt.md) 的平移无关裸弦 $L$ 满足
$$
 L^2=.145^2+2(.075)(.22)(1-\cos\vartheta)
 >.145^2+2(.075)(.22)(.066)>(.152)^2 .
$$
更厚的端切向转动还要求额外长度。这一结论对任何与 $g_0$ 真等距且有规定端姿的替代环带均成立。要以已证厚闭族出发求同一旋转度量，必须开放非圆纬圈，并在设计阶段同时取得足够的真实经线长再冻结。R659 的有符号双坡可提供独立正长度余量；其实际新形状、度量、曲率及全相位误差仍以其自身求值决定。
