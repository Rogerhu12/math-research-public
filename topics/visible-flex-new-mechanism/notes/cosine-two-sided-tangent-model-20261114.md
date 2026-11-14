# 偶高度核心的双侧单位切向连接模型与负 K 径向种子

日期：2026-11-14。本文是可直接实现的有限维模型推导，不是 connector 存在证明，也不是当前已被曲率必要界排除的 cosine 候选的复用理由。先取得可用的冻结零 framing 核心，才应在公开 Actions 求解以下边值问题。完整闭面、reach、幅度仍待证明。

## 1. 两个真实端口必须独立使用

固定一个通过独立连续认证的准确核心 \(X(s,\theta)\)，\(|s|\le w\)。两侧各取向外坐标 \(t\ge0\)，令 \(\sigma=+1\) 或 \(-1\)，入口位于 \(s=\sigma w\)。真实入口数据为
\[
X_0^\sigma=X(\sigma w,\theta),\quad
X_t^\sigma=\sigma X_s(\sigma w,\theta),\quad
X_{tt}^\sigma=X_{ss}(\sigma w,\theta),
\]
\[
X_{t\theta}^\sigma=\sigma X_{s\theta}(\sigma w,\theta),\qquad
X_{\theta\theta}^\sigma=X_{\theta\theta}(\sigma w,\theta).
\tag{1}
\]
不能把同一正侧数据原样复制到负侧；偶高度只保留每侧的镜面，不交换两侧。

两个连接器共享同一个准确 \(a_0=\operatorname{Length}(\gamma)/(2\pi)\)，入口的径向度量 jet 是
\[
a(0)=a_0,\qquad a_t(0)=a_{tt}(0)=0.
\]
每侧末端使用同轴平圆领
\[
X_{\rm end}=(r_c\cos\theta,r_c\sin\theta,h_\sigma),\quad
X_t=-e_r,\quad X_{tt}=0,\quad
a=r_c,\ a_t=-1,\ a_{tt}=0.
\tag{2}
\]
高度 \(h_+\) 与 \(h_-\) 独立，不从旧半转构造推定相反。

## 2. 三个角闭合条件可以严格自动满足

用两个实函数 \(u(t,\theta),v(t,\theta)\) 表示角单位切向：
\[
\boxed{
T(u,v)=\frac{(-\sin(\theta+u),\ \cos(\theta+u),\ v)}
                   {\sqrt{1+v^2}} .
}
\tag{3}
\]
这里 \(v\) 是竖直/水平切向的斜率，不是纬度角，因此无需用硬夹紧避免 \(\cos v=0\)。这个表示限定水平角切向非零；核心和圆领满足该条件，但它不是所有可能 connector 的完备参数化。

要求 \(u,v\) 都是周期 \(2\pi/3\) 的奇函数，例如由准确入口函数和有限个 \(\sin(3j\theta)\) 自由模组成。则
\[
T_{xy}(\theta+2\pi/3)=R_{2\pi/3}T_{xy}(\theta),\qquad
T_z(-\theta)=-T_z(\theta).
\]
所以三项闭合条件严格成立：
\[
\boxed{\int_0^{2\pi}T\,d\theta=0.}
\tag{4}
\]
这不是把一个非闭向量场的数值平均任意扣掉。水平积分由 \(C_3\) 旋转的 \(1+\zeta+\zeta^2=0\) 消去，竖直积分由奇性消去。

令 \(\Pi\) 是周期零均值原函数算子，并取
\[
\boxed{
X(t,\theta)=z_c(t)e_z+a(t)\Pi T(t,\theta).
}
\tag{5}
\]
那么 \(X_\theta=aT\)，因此 \(G=a^2\) 准确成立。只剩两个度量方程
\[
|X_t|^2=1,\qquad X_t\cdot T=0.
\tag{6}
\]
保留 \(z_c(t)\) 的真实自由度；不能把每层位置重新置中来隐藏位移。

(3)–(5) 自动具有每侧
\(X(t,-\theta)=\operatorname{diag}(1,-1,1)X(t,\theta)\)。
因此 \(E\) 为角偶函数、\(F\) 为角奇函数；\(\langle F\rangle=0\) 自动成立。数值角网格宜取 6 的倍数，使离散闭合同样与这些对称性相容。连续模型仍由积分定义，FFT 只是数值求值方式，非线性切向的混叠、谱尾和原函数误差须按 R28 单独控制。

## 3. 核心的材料中心其实是准确二次式

记中心弧长 \(\ell\)、\(P=2\pi a_0\)、\(q=\tau/\kappa\)。准确核心为
\[
X=\gamma+s(B+qT),\qquad
d\theta=\frac{1+s q_\ell}{a_0}\,d\ell .
\]
所以材料平均 \(C(s)=\langle X(s,\theta)\rangle_\theta\) 满足
\[
C(0)=\frac1P\int\gamma\,d\ell,\qquad
C'(0)=\frac1P\int B\,d\ell,
\]
\[
\boxed{
C''(s)=\frac1P\int\frac{\tau^2}{\kappa}N\,d\ell,
}
\tag{7}
\]
右侧与 \(s\) 无关。最后一式也直接由
\(X_{ss}=\tau^2N/(\kappa J)\) 与材料测度中的 \(J\) 抵消得到。故 \(C(s)\) 严格为二次多项式，而不只是二阶近似。\(C_3\) 使它的水平分量为零。

于是两侧 \(z_c(0),z_c'(0),z_c''(0)\) 可从同一组准确中央积分及 \(s=\pm w\) 取得，按照 (1) 翻转一次导数。以后改变求积密度是在评估同一个积分定义，不是在重新设计每层中心。

## 4. 全二 jet 硬拼接不能省略的导数

入口单位切向 \(T=X_\theta/a_0\) 对应 (3) 中
\[
u_{\rm core}=\phi-\theta-\arctan(r'/r),\qquad
v_{\rm core}=z'/\sqrt{r^2+(r')^2},
\tag{8}
\]
其中 \(\phi=\phi(s,\theta)\) 是准确材料反解。按每个对称扇区连续展开 \(\phi-\theta\)，两函数均为所需的奇 \(C_3\) 函数。

若通过 (5) 对**位置**作完整 \(C^2\) 硬拼接，还必须匹配 \(T_{tt}\)，因为
\[
X_{tt}=z_c''e_z+a''\Pi T+2a'\Pi T_t+a\Pi T_{tt}.
\tag{9}
\]
已有核心模块只返回位置全二 jet，不能据此宣称 \(T_{tt}\) 已实现。它满足
\(T_{ss}=a_0^{-1}\partial_\theta X_{ss}\)，涉及核心三阶位置信息。

具体可直接从隐式反解继续求导。令 \(V=|\gamma_\phi|\)，
\[
A_\phi=V+s q_\phi,\qquad
\phi_s=-\frac q{A_\phi},
\]
\[
\boxed{
\phi_{ss}=
-\frac{2q_\phi\phi_s+(V_\phi+s q_{\phi\phi})\phi_s^2}{A_\phi}.
}
\tag{10}
\]
这里 \(q_{\phi\phi}\) 需要曲线第五阶 jet；有限 cos 模型能够准确提供它，但必须新增并独立检查实现，不能把目前 0–4 阶模块直接当作已具备该接口。

设 \(H(\phi)=\phi-\arctan(r'/r)\)、\(b(\phi)=z'/\sqrt{r^2+(r')^2}\)，则
\[
u_s=H'\phi_s,\quad u_{ss}=H''\phi_s^2+H'\phi_{ss},
\]
\[
v_s=b'\phi_s,\quad v_{ss}=b''\phi_s^2+b'\phi_{ss}.
\tag{11}
\]
例如 \(H'=A_{xy}/p^2\)，其中
\(A_{xy}=r^2+2(r')^2-r r''\)、\(p^2=r^2+(r')^2\)。
所有表达式都有准确的周期和奇偶身份。

一个直接有限模型可用左端 quintic Hermite 基线精确保留
\(u_0,u_1,u_2\) 和 \(v_0,v_1,v_2\)，右端三 jet 取零，再加
\[
t_*^3(1-t_*)^3
\sum_{i=0}^{K-1}\sum_{j=1}^M
c_{ij}P_i(2t_*-1)\sin(3j\theta),\qquad t_*=t/L.
\tag{12}
\]
每条入口函数保留其完整准确角依赖；自由修正才用有限模。不能把强核心先投到 \(m=12\) 后把投影误差叫作 BVP 残差。两侧使用独立自由系数。

## 5. 为什么新径向模型必须容许负 K

每个向外半带的度量曲率为
\[
K=-a_{tt}/a.
\]
从准确平核 \(a_t=0\) 到向内平圆领 \(a_t=-1\)，其总高斯曲率固定为
\[
\int_{\rm half}K\,dA
=-2\pi[a_t]_{\rm start}^{\rm end}=2\pi.
\tag{13}
\]
但总曲率为正不允许把整个半带强制成 \(K\ge0\)。

若两侧都 \(a_{tt}\le0\)，并以平圆盘（或处处非负高斯曲率的旋转帽）封口，全闭面将有 \(K\ge0\) 且总曲率 \(4\pi\)。Pakzad 的原始论文 [Corollary 2, p.4](https://arxiv.org/pdf/2206.09224) 给出所需正则性范围的完整嵌入凸性结论；本模型的闭 \(C^2\) 嵌入和预定 \(C^2\) 度量满足其 \(C^{1,\alpha}\)、\(\alpha>2/3\) 假设。紧性排除无界情形。

闭凸曲面的全局刚性适用于这里，包括平区；Ghomi–Spruck 原文的 [Appendix A 末段, p.9](https://ghomi.math.gatech.edu/Papers/rigidity.pdf) 明确说明 Pogorelov 的无正则限制版本。这里没有误用该文要求 \(C^{2,1}\) 的局部新定理。

于是每个内在角平移都唯一延拓为环境刚体运动。这个连续紧 \(S^1\) 群固定一个空间点，经共轭成为轴旋转群；固定径向坐标的轨道必须为平面圆。强 \(C_3\) 星形中央曲线不可能是这样的圆。因此在这一全局角独立度量/圆帽模型中，至少一处真正的负 \(K\) 区必不可少。

这只排除全 \(K\ge0\) 的模型限制，不说明增加负 \(K\) 就能解出 connector。

## 6. 一个明确正半径、带定量负 K 的径向种子

用 \(d(t)=-a_t(t)\)。令 \(S_5(x)=10x^3-15x^4+6x^5\)，选择
\[
0<\nu<\mu\le1,\quad \lambda_1,\lambda_2,\lambda_3>0,\quad
\lambda_1+\lambda_2+\lambda_3=1.
\]
在三段长度 \(L\lambda_i\) 内，令 \(d\) 分别由 \(S_5\) 光滑过渡
\[
0\longrightarrow\mu,\qquad
\mu\longrightarrow\nu,\qquad
\nu\longrightarrow1.
\tag{14}
\]
置
\[
\bar d=\tfrac12\{\lambda_1\mu+
\lambda_2(\mu+\nu)+\lambda_3(\nu+1)\},\quad
L=(a_0-r_c)/\bar d,
\]
\[
a(t)=a_0-\int_0^t d(u)\,du.
\tag{15}
\]
则 \(r_c\le a\le a_0\)，两端的 \(a,a_t,a_{tt}\) 正好满足 (1)–(2)，并可分别接开放常半径核心度量和开放线性平领度量。中段 \(d\) 严格下降，所以 \(a_{tt}>0\)、\(K<0\)，且准确负曲率总量为
\[
\boxed{\int_{\rm middle}K\,dA=-2\pi(\mu-\nu).}
\tag{16}
\]

一个明确初始选择为
\[
\mu=19/20,\quad\nu=13/20,\quad
(\lambda_1,\lambda_2,\lambda_3)=(1/4,7/20,2/5).
\]
此时 \(\bar d=583/800\)、\(L=800(a_0-r_c)/583\)，负曲率总量为
\(-3\pi/5\)。这些数只是内在度量种子，不是已嵌入的参考曲面尺寸证书。

由于 \(\max S_5'=15/8\)，中段有准确上界
\[
|K|\le\frac{15(\mu-\nu)}{8L\lambda_2 r_c}.
\tag{17}
\]
它可先剔除与曲率预算明显不相容的过窄负 \(K\) 带；满足 (17) 的预算仍不等于全部主曲率通过。

后续自由径向修正可在每个分段内部取支持，并使其二 jet 在分段边界消失。这样保留端点导数差，(16) 继续固定一个非零负曲率总量，避免优化器把整个模型退回已排除的全非负曲率类。改变 \(a\) 是设计；得到候选后必须冻结准确径向函数再加密。

## 7. 求解前的真实位置与长度筛

对于选定的 \(L,r_c\)，每个材料点至少需要满足弦长界
\[
|X_0^\sigma(\theta)-(r_c\cos\theta,r_c\sin\theta,h_\sigma)|\le L.
\tag{18}
\]
设其水平距离为 \(d_{xy}(\theta)\)。若某点 \(d_{xy}>L\)，立即不可能；否则尾高度必须落在所有区间的交集：
\[
h_\sigma\in\bigcap_\theta
\left[z_0^\sigma(\theta)-\sqrt{L^2-d_{xy}^2},
      z_0^\sigma(\theta)+\sqrt{L^2-d_{xy}^2}\right].
\tag{19}
\]
该交集还须与实际全曲面高度包络相交。它只用准确端口位置，不从圆对称参考面的高度推断真实非圆连接器。

此外必须先满足 [R25](../results/R25-cosine-core-outward-port-budget.md) 的外尖转向门。尾圆盘的握持半径也须按完整直径预算选择；例如固定握持圆盘半径 \(r_H\) 需要 \(2r_H\ge0.2D\)，并给圆领拼接留出实际开放余量。所有这类筛通过仍只是必要条件或设计预算。

## 8. 与正交 frame 版本的关系

已证明的 [R28](../results/R28-orthonormal-frame-reconstruction-and-metric-bound.md) 给出三变量正交 frame 的积分性方程及连续残差到最大度量误差的界。本文不另写第二个 frame solver。(3)–(4)、真实双侧端口、(7)、负 \(K\) 种子和 (18)–(19) 可直接供该版本使用。

若最终仍用 (5) 重建位置，§4 的 \(T_{tt}\) 需求必须真实支付。也可从 \(X_t=V\) 沿径向积分来固定 \(E=1\) 和入口二 jet，但那会把圆领位置相容转成另一组径向积分边界条件；不能把两种表示各自的优点同时宣称已自动满足。

