# R223 — 原 M12 从中央到真正平接头的共同 C² 材料图

2026-11-26，Astra-visible-flex-6a65e705 / g5_and_exact。**可信度：已证明。** 本文是完整的坐标接合引理与求解器接口定义，不是新的等距存在性断言，也不是已执行的全尾数值结果。

当前已恢复的全 prefix 求解器在 \(r=c=0.6\) 保留旧 common-cut 端迹；该圆是内部尾接口。下述构造把这个接口移入同一个全局 Cartesian 修正场的内部，同时只在真正中央端和 \(r=c_f\) 平接头固定完整二阶端迹。它不改原 \(g\)，不把尾的物理弧长换成下面的坐标长度。

输入沿用：

- [原精确桥与度量传递](../notes/2026-11-09-db6f-exact-bridge-and-metric-transfer.md)；
- [原 common-cut 和闭合位置图](../notes/2026-11-09-db6f-common-cut-and-closed-map.md)；
- [原 M12 尾定义清单](../notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json)；
- [精确积分尾读取器](../scripts/db6f_tail_integrated.py)；
- [实际非圆角规读取器](../scripts/fd2d-metric-noncircle-gauge-screen.py) 中 `Tail` 的深 collar 位置定义；
- [冻结背景源](../scripts/db6f_tail_interval_source.py)、[有限源精确二进校准常数](../notes/2026-11-09-db6f-tail-finite-source-calibrations.json) 与 [原精确 alpha 包](../notes/2026-11-09-db6f-tail-tight-alpha.json)。

## 1. 固定的原度量与真实接口

令原 prefix 的物理弧长端点为 \(S_*\)，由原唯一精确桥根定义。它的度量是
\[
g=ds^2+f(s)^2du^2,\qquad 0\le s\le S_* .
\]
在 common cut，原尾的度量是
\[
g=(1+w(r)^2)\,dr^2+r^2du^2,\qquad c_f\le r\le c .
\]
这里 \(w(r)\) 是原固定解析背景，\(\alpha\) 仍是原精确 A/B 积分归一化；本文没有把任何包的中心值重定义成新背景。

两个原二进实数为
\[
c=\frac{5404319552844595}{9007199254740992},\qquad
c_f=\frac{2702159776422297}{18014398509481984}.
\]
因此
\[
h=c-c_f=\frac{8106479329266893}{18014398509481984}>0.
\]
原 cut 的数据是 \(w(c)=1/2,\ w_r(c)=-7/(2c)\)。向平接头增加的物理弧长满足
\[
r_s=-\frac1{\sqrt{1+w^2}},\qquad
r_{ss}=-\frac{w w_r}{(1+w^2)^2}.
\]
特别地，
\[
r_s(c)=-\frac2{\sqrt5},\qquad r_{ss}(c)=\frac{28}{25c}.
\tag{1}
\]
原 common-cut-v2 正是以这些真实链式导数匹配位置的完整二阶端迹。材料角 \(u\) 在这里没有另换一条曲线。

## 2. 显式全尾坐标及严格单调性

在 prefix 上令 \(q=s\)。尾上令
\[
q=S_*+ht,\quad 0\le t\le1,\qquad r(q)=c-hR(t),
\]
记
\[
k=\frac2{\sqrt5},\quad a=1-k,\quad b=\frac{28h}{25c},
\]
并定义
\[
R(t)=kt-\frac b2t^2+
(6a+\tfrac32b)t^3-(8a+\tfrac32b)t^4+
(3a+\tfrac12b)t^5.
\tag{2}
\]
直接代入得到
\[
R(0)=0,\quad R(1)=1,\quad
R'(0)=k,\ R''(0)=-b,\quad R'(1)=1,\ R''(1)=0.
\]
所以 \(r\) 在 common cut 的 0/1/2 jets 恰是式 (1)，在真正平接头满足
\[
r=c_f,\quad r_q=-1,\quad r_{qq}=0.
\tag{3}
\]

式 (2) 的导数在四次 Bernstein 基中的五个系数是
\[
k,\quad k-\frac b4,\quad 3-2k+\frac b4,\quad1,\quad1.
\tag{4}
\]
这给出整个连续区间的单调性，无需只检查有限节点。确切有理比较给出
\[
\frac{749}{1000}<\frac hc<\frac{751}{1000}.
\]
而 \((8944/10000)^2<4/5<(8945/10000)^2\)，故
\[
.8944<k<.8945,\qquad .20972<\frac b4<.21028.
\]
于是式 (4) 的每个系数都严格落在 \((.684,1.422)\)，Bernstein 基非负且和为一给出
\[
.684<R'(t)<1.422\quad (0\le t\le1).
\tag{5}
\]
因此 \(q\mapsto r\) 是整个尾的严格单调光滑微分同胚，没有坐标退化或折叠。这里没有使用 binary64 舍入后的最后一位作为严格端点。

## 3. 同一 g 的完整链式变换

尾上定义
\[
H(q)=-r_q(q)\sqrt{1+w(r(q))^2}>0.
\]
共同坐标里的原度量恰为
\[
g=H(q)^2dq^2+r(q)^2du^2.
\tag{6}
\]
prefix 上仍为 \(H=1,\ f(q)=f(s)\)。这只是原 \(g\) 的坐标表达，尾的真正弧长仍是
\[
\int_{S_*}^{S_*+h}H(q)\,dq
=\int_{c_f}^{c}\sqrt{1+w(r)^2}\,dr,
\]
一般并不等于 \(h\)。

沿尾
\[
H_q=-r_{qq}\sqrt{1+w^2}
      -\frac{r_q^2ww_r}{\sqrt{1+w^2}}.
\tag{7}
\]
式 (1) 给 \(H(S_*)=1,\ H_q(S_*)=0\)。原背景在真正平接头有 \(w,w_r\to0\)，再由式 (3) 得 \(H\to1,\ H_q\to0\)。因此以
\[
s(q)=S_*+\int_{S_*}^qH(\xi)\,d\xi
\]
连接原 prefix 弧长，得到跨 common cut 且延至平接头的 C² 正向材料坐标；在接头后继续平面上的 \(r=c_f-(q-S_*-h)\)，仍保持上述二阶接合。

如果原位置图两侧在物理 \(s,u\) 下共享全部二阶迹，则
\[
X_q=H X_s,\quad X_{qq}=H^2X_{ss}+H_qX_s,\quad X_{qu}=HX_{su}
\tag{8}
\]
说明它们在共同 \(q,u\) 图下也共享全部二阶迹。反方向由 \(H>0\) 得到。式 (7) 必须真实计算，不能只将旧 \(X_{ss}\) 搬到新参数名下。

## 4. 原有限尾与平 collar 的实际位置

令原积分尾的 Fourier 扰动系数为 \(V(r)\)，真实角图为 \(u\)。在深有限端 \(r_i>c_f\)，原读取器保存的是同一系数曲线的
\[
V_i,\quad V'_i,\quad V''_i.
\]
令 \(\ell=r_i-c_f,\ z=(r-c_f)/\ell\)。原 collar 的定义是
\[
V(r)=A_3z^3+A_4z^4+A_5z^5,
\]
\[
A_3=10V_i-4\ell V'_i+\tfrac12\ell^2V''_i,\quad
A_4=-15V_i+7\ell V'_i-\ell^2V''_i,\quad
A_5=6V_i-3\ell V'_i+\tfrac12\ell^2V''_i.
\tag{9}
\]
式 (9) 在 \(r_i\) 接原有限尾，在 \(c_f\) 的 0/1/2 jets 全部为零。其完整角导数对同一有限 Fourier 系数求导，因此混合迹也同步成立；不需要对 \(X_{rr}\) 另作角插值。

写真实扰动为 \((V_{xy}(r,u),V_z(r,u))\)，并令
\[
D(r)=\int_r^c w(\rho)\,d\rho,\qquad
C=Z_{\rm prefix,mean}+V_{z,\rm mean}(c).
\]
与原反射方向一致的尾是
\[
X(r,u)=\bigl(r(\cos u,\sin u)+V_{xy}(r,u),\
C+D(r)-V_z(r,u)\bigr).
\tag{10}
\]
这给出
\[
X_{r,z}=-w-V_{z,r},\qquad X_{rr,z}=-w_r-V_{z,rr}.
\]
不得从数值 w 包多项式求导去冒充 \(w_r\)。common cut 的高度常数 \(C\) 与原 v2 高度规一致；在真正平接头，式 (9) 和原 \(w,w_r\to0\) 给出真实圆周平面二阶端迹。

## 5. 一个跨全部内部接口的 Cartesian 未知场

设 \(T=S_*+h\)，用 \(z=q/T\in[0,1]\) 上一套全局五次 B-spline 与既定完整角基定义 \(W\)。在 clamped knot 端只去掉最初与最后各三个径向基函数，便使
\[
W=W_q=W_{qq}=0
\]
在中央端和平接头严格成立。common cut、coast、各正负 K 段和旧 bridge 接口处不删除列，不另锁端迹。

因为 \(H>0\)，这些边界条件等价于 \(W=W_s=W_{ss}=0\)。在内部图中使用
\[
\partial_s=\frac1H\partial_q,\qquad
W_{ss}=\frac{W_{qq}}{H^2}-\frac{H_qW_q}{H^3}.
\tag{11}
\]
故若 \(B(z)\) 是保存的单位坐标基函数，则位置与真实物理导数的求值矩阵是
\[
B_0=B(z),\quad
B_1=\frac{B'(z)}{TH},\quad
B_2=\frac{B''(z)}{T^2H^2}-\frac{H_qB'(z)}{TH^3}.
\tag{12}
\]
完整修正后位置的六个 jets 仍由这一套 \(B_0,B_1,B_2\) 与同一角基导出。式 (12) 不能只在残差里使用，而在曲率观察器里漏掉第二项。

固定中央角图 \(u=u_0(\theta)\) 的导数记为 \(\rho_0\)，并令 \(b=f\rho_0\)（尾上 \(f=r\)）。完整相对 Gram 残差仍为
\[
\bigl(|X_s|^2-1,\ \sqrt2\,X_s\cdot X_\theta/b,\
|X_\theta|^2/b^2-1\bigr).
\]
其 J/JT 与流式模块相同，只需使用式 (12) 的真实径向矩阵，以及物理积分权 \(H\,dq\)。这里的 H1 矩阵仅作右预条件；没有把残差或零集改掉。

## 6. 已支付与未支付的接口

本文严格支付共同图的全区间非退化、真实 common-cut/平接头 C² 链式接合、原 g 的完整转换以及全局修正基的端迹性质。它使下一轮可把 r=.6 释放成内部变量。

尚未支付的是：按原 24 块源连续定义实际装入全部尾；背景逆像与积分的精度证书；新全域位置求解及独立细化；完整 Gram 残差趋零；精确解的全频存在机制；全域曲率、reach、held 和 README 的其余完成条件。本文不是这些缺项的替代证明。

本地环境失联后本文仅以文本保存；与本文接口对应的新全尾程序尚未实际运行。前一 recovered prefix 程序仍只到内部 common cut，其报告中的范围标志必须保持。
