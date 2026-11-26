# 2026-11-26：R569 线性种子的数值实现与固定 g 尾接口

状态：实现已完成、仅静态解析与绑定核查；本笔记写入时尚无科学执行结果。证明是 [R569](../results/R569-fixed-oscillatory-tail-and-flat-infinitesimal-bending.md)，本次运行只将同一个固定种子的实际外端 jets 变成可用数据，不构造有限等距族。

## 1. 单 job 的确定输入

- 脚本：[r569_flat_seed_outer_jets_20261126.py](../scripts/r569_flat_seed_outer_jets_20261126.py)；
- 请求：[request-r569-flat-seed-20261126.json](../computations/request-r569-flat-seed-20261126.json)；
- workflow：仓库根 `.github/workflows/visible-r569-flat-seed-20261126.yml`；
- 复用已发布的 stdlib 入口 `run_inverse_rotational_metric_20261126.py`，先真正 pull 公、私有 main 并核 README/QUEUE，再清理凭据、在固定源提交执行科学子进程。

默认 $M=168$，129 个输出半径，DOP853 的 rtol/atol 为 $2\cdot10^{-11},2\cdot10^{-13}$，max step 为 $0.15$。同一 job 顺序计算：M 原容差、M 容差紧 8 倍、M+1 紧容差。三者 w、度量、数学种子和 $\alpha_{160}$ 归一完全相同。仅原始 stdout，无 artifact/release/git 或跨运行缓存写入。

本次规则输入来自 public $57a459871ee6abaa8050dea0ad90853da5fa7589$、private $f269d5ce0269dc4eb2580f48cfcb76932f868452$，README blob 与前次相同；执行时仍以入口实际 pull 后的检查为准。

## 2. 有限末端索引和 log 幅度

输入 M 准确表示
$$
\rho_{M+1}=0,\qquad y(\alpha_{M+1})=0.
$$
从 $\alpha_{M+1}$ 开始反向积分，而不是从 $\alpha_M$ 开始。采用平衡状态
$$
z_{\rm bal}=y_u/\varepsilon,\quad
y_u=\varepsilon z_{\rm bal},\quad
(z_{\rm bal})_u=-y-\big((\log p)_u+\varepsilon_u/\varepsilon\big)z_{\rm bal}.
$$
每个内部 cell 末端重新置 y=1，取得真实斜率比；最终统一以
$y(\alpha_{160})=1$ 为数学尺度。

之后向 $r=0.30$ 延伸。真实外端幅度可能超过双精度范围，故逐段保存对数幅度。展示时三份解使用**同一个**来自紧容差 M 解的外端 Cauchy 尺度，不分别归一来掩去幅度误差。输出保留这个共同尺度相对于 $y(\alpha_{160})=1$ 的 log。

## 3. 准确 DtN 截断界与数值传递误差分开

R569 给
$$
|\rho_{161}-\rho_{161}^{(M)}|
 \le\frac1{32}10^{-3(M-160)}.
$$
在第160个 cell，左端通量恒等式给
$$
z_{\rm bal}(\alpha_{160})
 =-\frac{D_{160,LL}+k_{160}\rho_{161}}
        {p(\alpha_{160})\varepsilon(\alpha_{160})}.
$$
由 R569 的
$k_{160}\le4C_\alpha e^{-11\sqrt\alpha/4}$、
$p(\alpha)\ge(C_\alpha/2)e^{-5\sqrt\alpha/4}$、
$\varepsilon(\alpha)\ge\alpha^{-3}$，得到
$$
\frac{k_{160}}{p(\alpha)\varepsilon(\alpha)}
 \le8\alpha^3e^{-3\sqrt\alpha/2},\qquad \alpha=\alpha_{160}.
$$
所以准确有限 DtN 输入的斜率截断误差至多
$$
8\alpha^3e^{-3\sqrt\alpha/2}\frac1{32}10^{-3(M-160)}.
$$

这两个界**不含数值 ODE 传递误差**。同 M 收紧容差、M/M+1 的外端和 C2 表差分别输出；它们是数值观察，不能代替区间 ODE 证书，也不能用准确 DtN 界掩盖浮点误差。

输出表只覆盖 $r(\alpha_{160})\le r\le0.30$。更内侧仍由 R569 的准确无限极限定义，没有把它替换成一个有限零圆领或带导数跳跃的 cutoff 曲面。

## 4. 单位切向表示中的直接入口

记 R569 向量场的径向分量
$$
a_V=w(4f-rf_r)/3.
$$
在圆尾 $T_0=(-\sin\theta,\cos\theta,0)$ 上，该场准确对应
$$
\delta u=\frac{3a_V}{2r}\sin2\theta,\qquad
\delta v=-\frac{2f}{r}\sin2\theta,\qquad
\delta a_{\rm radius}=0,\quad\delta z_{\rm mean}=0.
$$
因为
$\delta T=-(3a_V/(2r))\sin2\theta\,e_r-(2f/r)\sin2\theta\,e_z$，
而 $r\Pi_\theta\delta T=V$。脚本给这两个径向幅度及一、二阶 r 导数；若 $r=r_c+L-s$，一阶 s 导数取负、二阶同号。

局部固定 g 的真实非线性问题可写为
$$
X=r\Pi_\theta T+Z(r)e_z,\qquad |T|=1,\quad \overline T=0,
$$
$$
X_r\cdot T=0,\qquad |X_r|^2=1+w(r)^2.
$$
此时角度量 $G=r^2$ 已准确。以种子初始化
$u=qU\sin2\theta,\ v=qV\sin2\theta,\ Z=h$ 后，首阶误差为零，但二阶及以后仍须解上面的非线性方程；本输出没有宣称这些高阶方程已解。

## 5. 下一外端匹配条件

对一般旋转背景 $X=a(s)e_r+z(s)e_z$，二阶角模写为
$$
V=A(s)\cos2\theta\,e_r-\frac{A(s)}2\sin2\theta\,e_\theta
  +C(s)\cos2\theta\,e_z.
$$
直接线性化三项度量得
$$
aA'=-3a'A-4z'C,\qquad a'A'+z'C'=0.
$$
在选定的中段若 $z'>0$，这是普通二维一阶 ODE。开柱上 $a'=0,z'=1$，故 $C'=0,A'=-4C/a$；要接轴向恒定的椭圆核心变化，须实际求出
$$
C_{\rm core}=0.
$$
这是一个明确的标量 shooting 条件，可由中段径向 profile 参数调谐。达到它后 $A_{\rm core}\ne0$，否则 ODE 唯一性迫使整个种子为零。

固定 $q_{\rm ellipse}=0.18,\ r_{\rm offset}=0.2,\ R=0.38$，圆核从
$p=0.18$ 出发时，$p=0.18+\epsilon$ 的材料角一阶为
$$
u_c=\frac{3\epsilon}{4R}\sin2\theta+O(\epsilon^2),\qquad
a_0=R+\epsilon/2+O(\epsilon^2).
$$
其非径向分量要求 $A_{\rm core}=\epsilon/2,C_{\rm core}=0$；平均半径变化属于逆设计允许的旋转度量变化。不能直接把局部尾种子当成这个外端条件已经成立。当前硬约束 solver 的首轮身份不改；后续种子接入和 p-continuation 都必须另记实际输入。

