# R132：真实不变矩形与明确的 [-.05,.05] 精确嵌入环带

2026-11-13，visible-exact-astra-ac0d。

**结论：已证明并实际执行。** R125 的同一原腰分支、同一原始目标
\(g_0=E(r)dr^2+a(r)^2d\theta^2\)，对完整
\[
\delta=-\frac{7789843107295549}{4611686018427387904}+\eta,
\qquad |\eta|\le10^{-9},
\]
均有真正的 \(C^2\) 精确等距嵌入
\[
[-1/20,1/20]\times S^1\longrightarrow\mathbb R^3.
\tag{132.1}
\]
这将已认证的原腰环带径向宽度扩大十倍。证明只消费完整真实目标系数
和精确初始腰数据，不以有限候选的误差屏障通过为前提。

不同辅助 \(\delta\) 仍可对应不同目标；本篇没有构造同一个公共度量的
闭曲面 flex，也没有完成正帽、无限平尾或最终 reach。此前完整 `.05`
候选的 \(C^0\) 管失败记录仍成立，不被本篇改写成通过。

## 1. 同一个真实方程和初始符号

沿用 [R126](R126-exact-Codazzi-reconstruction-and-continuation.md)
及 [R131](R131-linear-degenerate-weighted-gradient-and-C0-continuation.md)
的准确符号与方向：
\[
\begin{aligned}
D_p p&=-\beta q(1+p^2)+\kappa(p-q)=f(p,q),&
D_p&=\partial_r-\gamma q\partial_\theta,\\
D_q q&=-\beta p(1+q^2)-\kappa(p-q)=g(p,q),&
D_q&=\partial_r-\gamma p\partial_\theta,
\end{aligned}
\tag{132.2}
\]
\[
k=\sqrt{-K},\quad\gamma=\sqrt E/a,\quad
\beta=a'/a,\quad\kappa=K'/(4K).
\]
目标 \(E\) 一直是原始候选 \(|F_r|^2\) 的完整角平均，不从新的解重算。

真实腰上 \(B_0=0\)，
\[
C_0=-\frac{1+\sum_j4j b_j(0)\cos4j\theta}{a(0)}<0,
\qquad p_0=k_0/C_0<0<q_0=-k_0/C_0.
\tag{132.3}
\]
R131 从完整初始 primitive 和准确有限相位独立认证的全角/全参数界给
\[
\min(-p_0,q_0)>0.121806458549795,
\qquad \max(-p_0,q_0)<2.669121967092210.
\tag{132.4}
\]
本篇对储存的有向端点再取准确有理屏障
\[
m_0=\frac{609}{5000}=0.1218,
\qquad M_0=\frac{67}{25}=2.68,
\qquad M_*=3.
\tag{132.5}
\]
真实下边界初余量大于 \(6.458549795\times10^{-6}\)，上边界初余量
大于 \(0.01087803290\)。这里保留完整 mean，未指定另一条 Cauchy 腰。

## 2. 准确移动不变矩形

对实数 \(x\)，记 \(x_-:=\max(0,-x)\)。在有限严格负曲率区间上，
设连续分片仿射函数 \(m,M\) 满足
\[
0<m\le m_0<M_0\le M<M_*.
\tag{132.6}
\]
在每个闭盒上，给真实系数的全区间上界，记
\[
\begin{aligned}
F_+&=|\beta|_{\rm up}M_*(1+M_*^2)+2|\kappa|_{\rm up}M_*,\\
F_-&=(\beta_-)_{\rm up}M_*(1+m_0^2)
              +(\kappa_-)_{\rm up}(m_0+M_*).
\end{aligned}
\tag{132.7}
\]
若该盒内部严格满足
\[
M'>F_+,\qquad -m'>F_-,
\tag{132.8}
\]
则沿实际特征的不变矩形为
\[
\boxed{\qquad -M(r)<p(r,\theta)<-m(r),\qquad
                      m(r)<q(r,\theta)<M(r).\qquad}
\tag{132.9}
\]

**四边核验。** 首次可能退出之前，\(|p|,|q|<M_*\)，所以
\(|f|,|g|\le F_+\)。在 \(p=-M\) 上，
\(D_p(p+M)=f+M'>0\)；在 \(q=M\) 上，
\(D_q(q-M)=g-M'<0\)。这控制两条外边。

在 \(p=-m\)、\(m\le q\le M\) 上，准确有
\[
f=-\beta q(1+m^2)-\kappa(m+q)
\le\beta_-M_*(1+m_0^2)+\kappa_-(m_0+M_*)\le F_-.
\]
因此 \(D_p(p+m)=f+m'<0\)。在 \(q=m\) 上写 \(x=-p\)，则
\[
g=\beta x(1+m^2)+\kappa(x+m)\ge-F_-,
\]
故 \(D_q(q-m)=g-m'>0\)。这控制两条内边。初始严格余量与四边的
严格导数方向排除首次退出。证明只用源项的真实符号，不把不同特征的
角路径相互混用。

在有限 scalar germs 的接点，\(p,q,m,M\) 连续；真实 \(\kappa\) 可用
有界的一侧值。逐片使用同一积分屏障，论证仍成立。

## 3. 不依赖候选误差的真实继续存在

由 (132.9)，实际 \(d=p-q\) 满足
\[
|p-q|\ge2m>0,\qquad\max(|p|,|q|)\le M.
\tag{132.10}
\]
R131 的准确加权角梯度
\(U=(p-q)p_\theta,V=(p-q)q_\theta\) 满足线性输运，因此
\[
\max(\|U(r)\|_\infty,\|V(r)\|_\infty)
\le W_0\exp\int_0^r\big[|\beta|(2+4M^2)+4|\kappa|\big]dt.
\tag{132.11}
\]
初始 \(W_0<221.387250615\) 是 R131 从真实
\(-2k_0^2 C_{0,\theta}/C_0^3\) 取得的全角上界。
结合 (132.10)，实际一阶角导数在有限验证区间上统一有限。
R131 §4 的特征接续及高阶角导数归纳随即排除有限最大存在端点。
这证明原 R125 分支延拓，而不只是已经存在的解满足估计。

反变换
\[
C=\frac{2k}{p-q},\qquad B=k\frac{p+q}{p-q},\qquad A=Cpq
\tag{132.12}
\]
保持非退化；\(a,E,k\) 的正下界也逐盒验证。R126 的完整周期框架重建
给同一材料角上的单值 \(C^2\) 浸入及准确度量。没有从有限 Fourier
投影推断无限 PDE，也没有遗漏闭角 monodromy 条件。

## 4. 同一真实分支的定量嵌入

令 \(x=-p>0,y=q>0\)。从 (132.12) 准确得到
\[
A=\frac{2kxy}{x+y}\le kM,
\quad |B|=k\frac{|x-y|}{x+y}\le k,
\quad |C|=\frac{2k}{x+y}\le\frac{k}{m}.
\tag{132.13}
\]
对 R126 的真实正交框架 \(X,Y,n=Y\times X\)，
\[
F_r=\sqrt E X,\quad F_\theta=aY,\quad
X_r=\sqrt E A n,\quad Y_r=\sqrt E Bn,\quad
n_r=-\sqrt E(AX+BY).
\tag{132.14}
\]
所以四个完整积分类界是
\[
\begin{aligned}
\Delta_F&=\int\sqrt E,&
\Delta_X&=\int\sqrt E kM,\\
\Delta_Y&=\int\sqrt E k,&
\Delta_n&=\int\sqrt E k\sqrt{M^2+1}.
\end{aligned}
\tag{132.15}
\]
它们作用于实际解，不是候选 frame 的浮点差。

[R123](R123-separated-correction-budgets-and-normal-Hessian.md) 和
[R128](R128-quantitative-embedding-of-the-exact-waist-annulus.md) 已对同一
初始腰给 \(F_{0,h}\cdot n_{0,h}>1/2\)、\(|F_{0,h}|<13/10\)，
且初始水平曲线绕数为1。初始 \(Y\) 是水平单位切向，\(X\) 是竖直单位向量。
保单位长度的框架恒等式给
\[
\begin{aligned}
|F_h|&>1/2-\Delta_F, & |F_h|&<13/10+\Delta_F,\\
\det_h(F_h,Y_h)&>1/2-\Delta_F-(13/10)\Delta_Y,\\
F_h\cdot n_h&>1/2-\Delta_F-(13/10)\Delta_n.
\end{aligned}
\tag{132.16}
\]
令 \(\varphi=\arg F_h\)、\(z=F_z\)。只要这些分子为正，
\[
\varphi_\theta=
\frac{a\det_h(F_h,Y_h)}{|F_h|^2}>0,
\qquad
z_r\varphi_\theta-z_\theta\varphi_r
=\frac{\sqrt E a F_h\cdot n_h}{|F_h|^2}>0.
\tag{132.17}
\]
水平位置的同伦不穿过原点，所以每个固定 \(r\) 的角映射仍具有度1，
进而是圆周微分同胚。在固定真实方位角 \(\varphi\) 下，第二个正分子
说明 \(z\) 随 \(r\) 严格增加。因此两点像相同必有同一 \(r,\theta\)，
得到整个正环带的全局单射。

原腰的准确偶反射给负半环带：水平位置不变、竖直位置反号。
两侧二阶迹按 R125 匹配，(132.17) 的方向一致。固定 \(\varphi\) 的
高度在整个 \([-1/20,1/20]\) 上严格递增，故两半之间也不会自交。
紧致材料环带上的单射浸入是嵌入，证明 (132.1)。

## 5. 原生有向执行与全部数值门

完整目标系数来自已经保存的150闭盒报告
`2026-11-13-Codazzi-joint-Taylor-r005-compact-native.json.gz`；
这里文件名 `r005` 表示 `.05`。consumer 只读该报告的真实目标系数和
实际 scalar germ 域，**不读候选、D1、rho0 或任何残差屏障**。
原始目标 provider 的 primitive 节点、全尾及 wholeη 费用均保留。

逐盒长度为 \(h\)，起始边界为 \(M_l,m_l\)。Arb 以256-bit算术取
\[
\begin{aligned}
M_r&=\operatorname{up}\big[M_l+hF_+(1+2^{-40})+2^{-180}\big],\\
m_r&=\operatorname{down}\big[m_l-hF_-(1+2^{-40})-2^{-180}\big].
\end{aligned}
\tag{132.18}
\]
再独立验证
\(M_r-M_l-hF_+>0\)、\(m_l-m_r-hF_->0\)。实际屏障是端点间的仿射
函数，故这两项正余量准确推出 (132.8)。每盒还核 \(M_r<3,m_r>0\)。
径向端点和 germ 从属关系使用准确有理数；全150盒连续覆盖 \([0,1/20]\)。

| 实际全区间量 | 安全有向结果 |
|---|---:|
| \(\int|\beta|\) | \(<0.001355286429\) |
| \(\int|\kappa|\) | \(<0.026159805617\) |
| \(\int\beta_-\) | \(<4.963372\times10^{-11}\) |
| \(\int\kappa_-\) | \(<0.016666099592\) |
| 实际 \(\max(|p|,|q|)\) | \(<2.877618\) |
| 实际 \(\min(-p,q)\) | \(>0.06977177014\) |
| 实际全域 gap | \(>0.13954354029\) |
| 真 \(k\) 下界 | \(>0.91245260089\) |
| 末加权梯度 \(W\) | \(<257.271163\) |
| 实际一阶角导数 | \(<1843.662284\) |
| \(\Delta_F\) | \(<0.055567417\) |
| \(\Delta_X,\Delta_Y,\Delta_n\) | \(<0.143643986,\ 0.051661239,\ 0.152654439\) |
| 水平半径下界 | \(>0.4444325839\) |
| 实际 \(\varphi_\theta\) | \(>0.2194231922\) |
| 实际柱坐标 Jacobian | \(>0.1586075083\) |
| 实际主曲率绝对值 | \(<14.000161\) |

最小外边界微分余量大于 \(3.75021\times10^{-29}\)，最小内边界微分
余量大于 \(6.52530\times10^{-55}\)；它们虽小但由实际有向算术严格为正。
曲率最后一项只是 Gershgorin 的安全上界，不据此授全闭面 reach。

输入/source/对象/参数盒和传递依赖 SHA 都由 consumer 核对；原始初值
provider 与 R131 的真实数据单独绑定。两个独立推导已核四边方向及
全部 frame/柱坐标符号。

## 6. 固定文件、复现及继续范围

| 文件 | SHA-256 |
|---|---|
| `scripts/fourfold_codazzi_invariant_rectangle.py` | `41a61d59294e87ee43eeda7b1881c9c079c0a3083d334aae80060cd61d226213` |
| `notes/2026-11-13-R132-invariant-rectangle-r05-native.json.gz` | `b7ca04a090ac4a2ac3daae39c3649cde2b21694a1f482f1cebdd757da46b6f6f` |
| 完整150盒目标报告 | `d69d826e957f4a3532fdd5e892d916080de8ae325dfb89d78a7ca0b84a82162a` |
| R131 独立真实腰数据报告 | `be7f67eec3fd07a4057b7db351484d2c8360c93b3461f5b39fcebb6fff790f2e` |

从 topic 目录复现：
```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_invariant_rectangle.py \
  --out /tmp/R132-invariant-rectangle-r05-native.json.gz
```
已存在的 native 报告不会覆写。输出同时保留完整150行、全部边界余量、
真导数界、几何门及 `closed_surface_complete=false`。

接下来仍须真正处理更远负区、\(K=0\) 接合、正帽、regular 平尾、全 mean
及闭合位置/框架。更紧的候选误差可以用于改进几何费用，但不再是本篇
环带存在与嵌入的必要条件。所有最终非全等/固定H/可见幅度/reach 条件
仍须在同一个闭合精确族上另行完成。
