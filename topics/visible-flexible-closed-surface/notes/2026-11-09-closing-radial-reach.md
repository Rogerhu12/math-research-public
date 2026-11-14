# 径向尾帽的全点对 reach 下界：母线锥角法

会话：Astra-visible-flex-4ffd372b / closing_geometry。2026-11-09。
本条是可独立审阅的几何引理，不依赖有限网格点对扫描。
应用范围是旋转对称背景中「尾部连同平圆盘帽」内部的所有点对。
完整闭曲面还须处理其余部分及跨区点对；非轴对称的真实等距修正亦须另付误差。

## 1. 平面母线引理

设平面正则曲线以弧长参数写成 gamma:[0,L]→R²，
且所有单位切向量落在一个张角 A<pi 的闭圆弧内。
设曲率绝对值不超过 K>0。则任意不同点 p=gamma(u),q=gamma(v)
及母线单位法向量 n_p 满足

\[
\frac{|q-p|^2}{2\,|(q-p)\cdot n_p|}
\ge \frac{\cos^2(A/2)}{K}.
\tag{1}
\]

分母为零时比值取无穷大。

证明：仅考虑 u<v，记 ell=v-u。选切向锥的中轴单位向量 e，
则 gamma'(s)·e≥cos(A/2)，从而

\[
|q-p|\ge (q-p)\cdot e\ge\ell\cos(A/2).
\]

另一方面，gamma'(u)·n_p=0，且
|gamma'(s)-gamma'(u)|≤K(s-u)，故

\[
|(q-p)\cdot n_p|
=\left|\int_u^v(\gamma'(s)-\gamma'(u))\cdot n_p\,ds\right|
\le K\ell^2/2.
\]

组合即得(1)。这是全母线的估计，不需要限制 ell、
不需要一条弧内曲率同号，也允许切线角在锥内反复振荡。

对 z=h(r)、0≤h'(r)≤c 的图，全部切线角位于[0,arctan c]。
因此 A=arctan c，(1)化为

\[
R_m=\frac{1+(1+c^2)^{-1/2}}{2K}.
\tag{2}
\]

若 h'≤0，反射 z 坐标即可。平坦帽段 h'=0 可直接接入同一母线。
C²接缝需要 h'和h''都趋于零；当前无限背景尾正是要单独核查这一点。

## 2. 旋转对称图的降维

令
\[
X(r,\theta)=(r\cos\theta,r\sin\theta,h(r)),\qquad
N(r,\theta)=\frac{(-w(r)\cos\theta,-w(r)\sin\theta,1)}
{\sqrt{1+w(r)^2}},\quad w=h'.
\]

取 p=X(r,0)、q=X(s,theta)，记 d=h(s)-h(r)、v=1-cos theta≥0。
则

\[
|q-p|^2=(s-r)^2+d^2+2rs\,v,
\]
\[
(q-p)\cdot N(p)
=\frac{d-w(r)(s-r)+w(r)s\,v}{\sqrt{1+w(r)^2}}.
\]

母线项由(1)控制：

\[
(s-r)^2+d^2
\ge 2R_m\frac{|d-w(r)(s-r)|}{\sqrt{1+w(r)^2}}.
\]

圆周项满足

\[
2rs\,v
=2\frac{r\sqrt{1+w(r)^2}}{|w(r)|}
  \frac{|w(r)|s\,v}{\sqrt{1+w(r)^2}}.
\]

三角不等式于是给出全径向图的任意两点：

\[
\frac{|q-p|^2}{2|(q-p)\cdot N(p)|}
\ge
\min\!\left\{
 R_m,\ \inf_r \frac{r\sqrt{1+w(r)^2}}{|w(r)|}
\right\}.
\tag{3}
\]

r=0与w=0按连续性或直接计算处理；内部平圆盘项不会降低此下界。
第二项就是圆周主曲率绝对值上界的倒数。
若所有非平坦点 r≥r_c>0、|w|≤c，则有易核查的粗界

\[
R_\theta\ge r_c\frac{\sqrt{1+c^2}}{c}.
\tag{4}
\]

(3)通过法向弦长公式贡献完整闭曲面 reach 认证的一组点对下界。
这里不把带边界图块的上述比值偷换成该图块作为闭集的 reach。
相关法向弦长公式的既有核查来源：
本题 notes/2026-11-08-geometry-certification.md §3；
Aamari et al., *Estimating the reach of a manifold*, EJS13(2019), Theorem2.2,
https://doi.org/10.1214/19-EJS1551 。

## 3. 对真实tail参数的数值预算

本agent已有真实积分重分配背景：
rCut=.6,rCuff=.1,width=.5,K=5,slopeCap=.65。
由公式(2),(4)，

\[
R_m=0.1838443616300637,\qquad
R_\theta\ge0.1834901606442548.
\]

所以一旦整个母线K≤5（含buffer、未改深尾）被连续认证，
尾+平帽内部全点对比值≥0.18349016。
这高于D≤5.2时的目标0.03D≤.156。
这不是单纯局部曲率预算：它已经处理本径向图块内所有远点对。

对root新cut-preserving K=6版本，建议先确认完整profile实际坡度上界。
若可证明c≤.506，且r_c=.25，则
R_m=(1+1/sqrt(1+.506²))/12≈.15769，
而R_theta>.55；因此K6版本也可在D5.2预算下得到正余量。
不要把浅层cap=.02误作全局c；恢复到wCut=.5的端口必须纳入。

## 4. cutoff buffer 的直接连续不等式

这段专指原 f6tail_compact_controlled_tail.mjs constructor，
不自动适用于root新cap恢复函数。

其末端port为原始w(r_old)∝r_old^{-7}，
记S=cellSmooth(x)，chi=1-S，
j0=1+(c_r-1)S，c_r=rCut/oldCut。
写v=|w*dlogw/dx|/(1+w²)^{3/2}，
rx=|dr_old/dx|，b=v/rx。
重分配的实际径向导数是

\[
r_x=rx\,j_0 S+(1-S)v/K+\alpha(1-S)rx/(1+w^2).
\]

故实际母线曲率≤K，只要

\[
S(b-Kj_0)\le K\alpha(1-S)/(1+w^2).
\tag{5}
\]

用b≤B、E≤Emax得到一个显式二次多项式的充分条件：

\[
Q(S)=K(c_r-1)S^2+
 (K-B-K\alpha/Emax)S+K\alpha/Emax\ge0
 \quad(0≤S≤1).
\tag{6}
\]

因而粗raw bufferMaxCurvature>K不等于实际buffer曲率>K。

实际候选a=4,delta0=.1,wCut=.5：
oldCut=.1205147281764、alpha=3.0851784989288、
B可取21.02218、Emax=1.4225。
(6)最小值采样常数计算为1.77324758（顶点S=.67526489）。
将参数向不利方向舍入成c_r≥4.97、alpha≥3.08、B≤21.03
仍有>1.7的余量；最终尚须积分数值给alpha的区间包络。
a=2.75,delta0=.1,wCut=.1候选的(6)余量更大，约9.49783。

深端buffer在第一port为原始w∝r^{-7}、j0=1。
如其raw曲率≤K，chi混合不会增大到K以上。

## 5. 未改无限深尾的一个廉价上界

假设深层cell校准alpha_n∈[1/2,2]（须从既有校准定理引入或独审），
r≥r_c、R=64、delta_n=delta0*2^{-n}、
eta_n=etaRatioAtN0*delta0*2^{-etaPower*n}，
且深层最大log平台为logR。
由max(cellSmooth')=15/8可得

\[
w_n\le \epsilon R\,\delta_n^{a-1}r_c^{-7}=:W_n,
\]

\[
|w_r|\le W_n\left[
 \frac{\sqrt{12}(15/8)(2|\log\delta_n|+\log128)}
 {\eta_n r_c}+\frac7{r_c}
 \right].
\tag{7}
\]

这是有意保守的连续界，非采样最大值。
a=2.75,delta0=.1,wCut=.1,r_c=.1时，N80处(7)仅给52.38，过粗；
N100给2.014，N128给.019857。
故把保护深度加到128可极大简化深尾背景K5证明，
且有限深线性DN的浮点值不变到本次分辨率。
a=4,wCut=.5的N80界约8.69e-29，无此问题。
函数n↦(7)在这些N之后递减，直接由
2^{-n(a-1-etaPower)}乘一个线性n因子验证。

此处完整几何结论所缺的是：alpha_n的统一粗括号、alpha积分的可靠区间，
以及真实非轴对称解的C²误差。全闭曲面还缺跨区点对。
