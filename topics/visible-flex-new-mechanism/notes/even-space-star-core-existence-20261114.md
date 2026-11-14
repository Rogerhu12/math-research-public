# 偶高度星形投影的零 framing 准确平核：小宽存在与接口

日期：2026-11-14。本文给出一个正面的局部输入：保持当前强 \(C_3\) 星形平面投影，两个偶高度模式已经足以取得嵌入、全圈非零空间曲率的中央曲线；其 rectifying 核在某个正宽度上准确等距、嵌入且 framing 为零。这里的宽度、曲率、reach 和最终幅度没有取得宏观定量门，完整封口仍未构造。

## 1. 固定投影与准确坏系数集合

令
\[
r=1+a\cos3\phi+b\cos6\phi>0,\qquad
\gamma_{xy}=r(\cos\phi,\sin\phi),\quad
p=|\gamma'_{xy}|>0.
\]
本文的两组 \((a,b)\) 均为已有公开有理参数；平面投影是 Jordan 径向图。记
\[
A=x'y''-y'x''=r^2+2(r')^2-r r''.
\]
\(A\) 是非零实解析三角多项式，故在紧圆周上只有有限个零点。对任意高度 \(z\)，空间曲率为零当且仅当
\[
A=0,\qquad {\cal L}[z]:=p z''-p'z'=0.
\tag{1}
\]
这是前一篇 framing 审计的二分量公式，或直接展开 \(\gamma'\times\gamma''\) 得到；\(p>0\) 排除了速度退化。

考虑
\[
z(\phi)=\varepsilon\{H_1\cos3\phi+H_2\cos6\phi\},\qquad\varepsilon>0.
\tag{2}
\]
在 \(A=0\) 的任一角点，两个线性系数
\[
{\cal L}[\cos3\phi]=-9p\cos\chi+3p'\sin\chi,
\]
\[
{\cal L}[\cos6\phi]=-36p\cos2\chi+6p'\sin2\chi,\qquad\chi=3\phi,
\]
不可能同时为零。证明：若 \(\sin\chi=0\)，第一项已非零；否则第一项为零给
\(p'/(3p)=\cot\chi\)，第二项为零再给
\(2\cos2\chi=\cot\chi\sin2\chi=2\cos^2\chi\)，迫
\(\sin\chi=0\)，矛盾。

所以每个平面 inflection 只排除 \((H_1,H_2)\) 平面中的一条真直线。有限条直线不覆盖平面；其补集开且稠密，并含有有理参数。选取其中任一点，则对任意固定 \(\varepsilon>0\)，(1) 在全圈都不同时成立，因而
\[
\boxed{\kappa(\phi)>0\quad\hbox{全圈成立}.}
\tag{3}
\]
中央曲线继续嵌入，因为水平投影从未改变。

若需要无需先逐个定位 inflection 的具体解析选择：对有理 \(a,b\)，这些 inflection 的 \(\cos\chi,\sin\chi\) 及两线性系数都是实代数数；两个系数不同时为零。因此可取 \(H_1=1,H_2=\pi\)，利用 \(\pi\) 的超越性保证任何坏直线均不包含该参数。这个选择只用于精确存在，不主张它有良好的曲率或高度比例。实际 Actions 设计可选更有利的有理系数。

## 2. 准确 rectifying annulus 及某个正宽嵌入

以中央曲线弧长 \(\ell\) 定义 Frenet \(T,N,B\)、曲率 \(\kappa\)、挠率 \(\tau\)，记
\[
q=\tau/\kappa,\qquad a_0=\operatorname{Length}(\gamma)/(2\pi).
\]
R9 的原始参数表达为
\[
G(s,\ell)=\gamma(\ell)+s(B+qT).
\]
取材料角
\[
a_0\theta=\ell+s q(\ell).
\tag{4}
\]
因为 (3) 和解析周期性，\(q_\ell\) 全圈有界。对充分小正 \(w\)，
\[
J=1+s q_\ell>0\quad (|s|\le w),
\]
故 (4) 给准确周期材料坐标。该曲面满足
\[
X_s=B,\qquad X_\theta=a_0T,\qquad
g=ds^2+a_0^2d\theta^2,
\tag{5}
\]
以及完整位置二 jet
\[
X_{ss}=\frac{\tau^2}{\kappa J}N,\qquad
X_{s\theta}=-\frac{a_0\tau}{J}N,\qquad
X_{\theta\theta}=\frac{a_0^2\kappa}{J}N.
\tag{6}
\]

此外，某个足够窄的 ribbon 确实嵌入：在中央 \(s=0\)，两个参数导数 \(B\) 和切向独立；紧嵌入中央曲线有有限个局部坐标邻域，在这些邻域中逆映射估计可统一取正宽。相互不相邻的中央弧段有正距离，缩小宽度又使其扰动继续分离。两类约束取最小值，得到一个正的嵌入宽度。此论证没有给出 \(w=0.02\) 或任何固定 reach/D 的保证。

因此 (2)–(6) 给真正的准确小宽核心，而不是仅有形式 Taylor jet。令 \(\varepsilon\to0\) 时，最小空间曲率和可用宽度可能退化；不能据小高度存在推断宏观几何优良。

## 3. 零 framing 与剩余的逐侧镜面对称

高度取偶函数后，blackboard 法架中 \(B\) 的两个分量
\[
\left(\frac{p z''-p'z'}{|\gamma'\times\gamma''|},
-\frac{|\gamma'|A}{p|\gamma'\times\gamma''|}\right)
\]
都为 \(\phi\) 的偶函数。因此每个 \(C_3\) 周期回走同一路，winding 严格为零；前一奇高度类的非零 linking 障碍已经解除。

设 \(S=\operatorname{diag}(1,-1,1)\)。有
\[
\gamma(-\phi)=S\gamma(\phi),\quad
T(-\phi)=-ST(\phi),\quad B(-\phi)=SB(\phi).
\]
曲率为偶，挠率及 \(q\) 为奇；弧长从对称点起也为奇。由 (4) 可得
\[
\boxed{X(s,-\theta)=S X(s,\theta).}
\tag{7}
\]
这个反射保留每个 \(s\) 侧；它不交换正负两侧。因此两边 connector 仍须分别求解，不过每侧可用 \(x,z\) 的 cos 模和 \(y\) 的 sin 模保持这一准确反射，减少自由变量。

## 4. 对称点挠率为零仍不足以给全宽曲率门

在 \(\phi=0,\pi/3\)，有
\(r'=r'''=z'=z'''=0\)。记
\[
R=r''-r,\quad U=r''''-6r''+r,\quad Z=z'',\quad V=z'''' .
\]
逐项叉积给
\[
\kappa=\frac{\sqrt{R^2+Z^2}}{r^2},\qquad \tau=0,
\]
但
\[
\boxed{
q_\ell=\frac{ZU-RV}{(R^2+Z^2)^{3/2}}
}
\tag{8}
\]
一般非零。因此该角点的全宽最坏主曲率仍是
\[
\frac{\kappa}{1-w|q_\ell|}
\]
（须先证明分母为正），不能由 \(\tau=0\) 直接宣布局部预算通过。离对称点还须全角计算 \(\kappa+\tau^2/\kappa\) 和 \(J\)。

## 5. 双侧连接与统一相位的条件性组装逻辑

若未来分别得到正、负两侧准确 connector，使其在中央开核心与 (5)–(6) 全二 jet 匹配，并共同形成
\[
g=ds^2+a(s)^2d\theta^2
\]
的完整嵌入环带，其两个端部又是绕同一固定轴的开放平圆领，则不需要原来的 proper 半转对称。

在整条环带使用同一个角平移，并定义
\[
F_\alpha(s,\theta)=R_z(\alpha)X(s,\theta-\alpha).
\]
角独立度量保证它准确等距。在同轴圆领及对应圆盘上，
\[
R_z(\alpha)(\rho\cos(\theta-\alpha),\rho\sin(\theta-\alpha),h_\pm)
=(\rho\cos\theta,\rho\sin\theta,h_\pm),
\]
所以两圆盘可逐材料点固定。中央准确核心自动保障正负两侧在中间相容；两条独立 connector 则必须各自支付终端全二 jet、全局嵌入、尺寸及 reach 条件。

这说明丢失交换两侧的半转捷径不会在形式组装层面破坏统一相位构造，但没有替代实际 connector 的存在证明。完整闭面的固定握持尺寸、幅度与 reach 仍属待解条件。

## 6. 后续计算身份

偶高度几何与旧奇高度几何不同，周长 \(a_0\) 也会变化；旧 sin 核的曲率、\(J\)、高度证书不能直接转用。新设计输出应精确保留选中 binary64 参数的有理身份，冻结后再由独立验证器逐 cell 认证。所有研究规模的优化和连续区间计算继续在本公开仓库 Actions 完成。
