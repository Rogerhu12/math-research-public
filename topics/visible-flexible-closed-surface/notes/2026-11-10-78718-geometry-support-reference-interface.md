# R93 的实际参考支撑接口：稳定入口、完整背景 jet 与暖态运输

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**范围。** R93 的同一物理度量、坐标运输和背景锚定公式已经证明。本文把它们接到实际 adaptive Frenet 的有限方程接口，并补出稳定入口求值的完整恒等式。最后一节是一次真实的有限浮点诊断，不能代替连续误差上界、BVP 联解或新的闭曲面。当前 M15/W22 生产源、物理参数、尾部边界与精度目标均未改变。

实际文件：

- `scripts/78718-geometry-support-reference-interface.py`：17247 B，SHA256 `646908b00183995289961475c74dc3dd146e851ee8ed841038074156f216485b`。
- `scripts/78718-geometry-support-reference-research.py`：10032 B，SHA256 `19b1b353fb37765c375222710443c1caddeafaebeaae3d269dd3c743edfb6c9c`。
- `notes/2026-11-10-78718-geometry-support-reference-interface-research.json`：7393 B，SHA256 `2b0f3b1f5cc13d8d741844d057a2b02cbab6c747b1024a5dc6c28217927c0461`。

它们使用已经保存的 UNSOLVED M15 warm，而不是一张未落盘的成功 inner。输入是 `2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz`，SHA256 `cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc`。参考系数与 R93 第6节相同，且实际再次读取的 literal core 系数逐值相同。参考的严格正性沿用 R93，不能把本次浮点显示值当作另一次严格证明。

## 1. 固定弧长位置差可以稳定地直接求出

令 $k_j=3j$，$c=c^*+d$，并记

$$
a_j^*=(1-k_j^2)c_j^*/k_j,\qquad a_j^d=(1-k_j^2)d_j/k_j.
$$

新的材料角入口是 $u=A_{c^*}(\psi)$。设实际支撑曲线在同一 u 对应的法向角为 $\phi=\psi+\delta$。它的精确定义为

$$
A_c(\psi+\delta)=A_{c^*}(\psi).
$$

消去共同的 $\psi$，用三角差公式得到等价的标量方程

$$
\begin{aligned}
f(\delta)={}&\delta
 +\sum_j2a_j^*\cos(k_j\psi+k_j\delta/2)\sin(k_j\delta/2)\\
&+\sum_j a_j^d\sin(k_j\psi+k_j\delta)=0.
\end{aligned}
\tag{1}
$$

其导数准确为

$$
f'(\delta)=1+\sum_j(1-k_j^2)c_j\cos(k_j\psi+k_j\delta)
=\rho_c(\psi+\delta)>0.
\tag{2}
$$

因此给定材料提升后根唯一。三重对称给 $A_c(m2\pi/3)=m2\pi/3$；把目标 u 所在的同一周期区间移去 $\psi$，就得到唯一根的括区间。实现用 (1) 的 Newton 步，若出界则取括区间中点；最多80步并实际检查残差，未收敛时明确抛出异常，不返回伪入口。给定正下界 $r$ 时，精确残差满足 $|\delta-\delta_{true}|\le |f(\delta)|/r$，由中值定理直接得到；本次显示的浮点残差本身没有区间误差包装。

这个方程在 $d=0$ 时准确有 $\delta=0$。它不通过把两个大小约1的材料角表达相减得到小残差。具体地，所有参考变化都保留为

$$
\sin(x+y)-\sin x=2\cos(x+y/2)\sin(y/2),
$$
$$
\cos(x+y)-\cos x=-2\sin(x+y/2)\sin(y/2).
\tag{3}
$$

对位置也使用同样方法。令 $h=h_c(\psi+\delta)$、$h'=h'_c(\psi+\delta)$，以及

$$
\begin{aligned}
\Delta h={}&\sum_jc_j^*[\cos(k_j\psi+k_j\delta)-\cos(k_j\psi)]
 +\sum_jd_j\cos(k_j\psi+k_j\delta),\\
\Delta h'={}&-\sum_jk_jc_j^*[\sin(k_j\psi+k_j\delta)-\sin(k_j\psi)]
 -\sum_jk_jd_j\sin(k_j\psi+k_j\delta).
\end{aligned}
$$

则有准确的复水平位置差

$$
\boxed{\;
\Gamma_c(A_{c^*}(\psi))-\gamma_{c^*}(\psi)
=e^{i\psi}\{\Delta h+i\Delta h'+(h+ih')(e^{i\delta}-1)\}.
\;}
\tag{4}
$$

证明只需展开右侧，得到
$e^{i(\psi+\delta)}(h+ih')-e^{i\psi}(h_{c^*}+ih'_{c^*})$。
实现进一步用

$$
e^{i\delta}-1=-2\sin^2(\delta/2)+i\sin\delta,
$$

使 (4) 中每一项都随差值变小。特别在同一 binary 系数向量 $c=c^*$ 时，程序里的 $d,\delta,\Delta h,\Delta h'$ 和整个位置差都准确为零；没有对 O(1) 位置相减留下投影尾。此处的准确零是有限入口表示的代数事实，不是整个曲面的等距结论。

## 2. 入口 Jacobian 与当前物理参数化兼容

R91 已证明固定 u 的参数导数

$$
\partial_{c_j}\Gamma_c(u)
=\cos(k_j\phi)e_r(\phi)
-\frac{\sin(k_j\phi)}{k_j}e_\theta(\phi).
\tag{5}
$$

参考 $c^*$、新背景和材料图在一次求解中全固定。因此从 (4) 求导不产生额外的参考导数，直接使用 (5) 即可。当前物理入口参数仍是

$$
c_1=q_{seed}e^{p_0},\qquad c_j=p_{j-1}\,scale_{j-1}\quad(j\ge2),
$$

未知状态的 gauge q 仍为原来的固定值。故有限初始列是

$$
J_{p_0}=\frac{c_1}{q}P_M(\partial_{c_1}\Gamma_c),\qquad
J_{p_{j-1}}=\frac{scale_{j-1}}qP_M(\partial_{c_j}\Gamma_c).
\tag{6}
$$

这与原来的参数归一化、真实支撑幅度未知量及 bc Jacobian 接口一致。参考点 $c=c^*$ 时 $\phi=\psi$；(5) 只含对应圆柱 R 列和 T 列，系数分别为1与 $-1/k_j$，所以有限空间严格重现线性项。R91/R93 的二阶余项仍是这里截断误差的来源。

精确角一、二阶导数用于入口诊断时应写成

$$
F_\psi=\rho_*e_\theta(\phi),\qquad
F_{\psi\psi}
=-\frac{\rho_*^2}{\rho_c(\phi)}e_r(\phi)
 +\rho_*'e_\theta(\phi),
\tag{7}
$$

因为 $\phi_\psi=\rho_*/\rho_c(\phi)$。不能把新的材料 $\psi$ 直接当成实际支撑曲线的法向角，除非 $c=c^*$。

## 3. 实际内部接口保留全部所需 jet

`ReferenceGeometry` 使用当前原 scalar spline 乘原三四分之一处起始的 quintic cutoff 作 $\chi$。锚定幅度取

$$
\eta=1-10(s/L)^3+15(s/L)^4-6(s/L)^5.
$$

准确的背景与材料图就是 R93(2)、(18)：

$$
\Theta=\psi+\chi P_*,\quad
B=a[(1-\eta)e^{i\Theta}+\eta\gamma_*].
$$

实现返回 `pos,p1,p2,s1,s2,sp,spp`，分别是 $B,B_\psi,B_{\psi\psi},B_s,B_{ss},B_{s\psi},B_{s\psi\psi}$。它还提供 $\Theta_s,\Theta_{ss},\rho,\rho_\psi,\rho_s$ 及

$$
v=\Theta_s/\rho,\quad
v_s=(\Theta_{ss}\rho-\Theta_s\rho_s)/\rho^2,\quad
v_\psi=(\rho_s\rho-\Theta_s\rho_\psi)/\rho^2.
$$

所以现有 `Flow.frame`、`adapt_fun`、`adapt_fun_jac` 和 `velocity_s` 的表达不需要删项或改物理系数。它们得到的仍是

$$
W=V_{normal}+vF_\psi,\qquad
Y_s=q^{-1}P_M(W-B_s).
\tag{8}
$$

固定参考下对状态扰动的微分仍是原 `frame_jvp` 加 $v\,\delta F_\psi$。显式径向求导仍是

$$
W_s=(V_{normal})_s+v_sF_\psi+vF_{s\psi};
$$

而 $(V_{normal})_s$ 中使用的新 `sp/spp` 已包括背景锚定的全部乘积项。这也解释了为什么只换 `pos` 或只换入口是不够的。所有公式只要求径向 C²，额外角导数来自有限 Fourier；没有把总体正则性门提高到 C³。

新模块只修改显式传入的一个新对象及其将来创建的 flow。它不全局 patch 现有类，不触碰正在运行的生产进程。`geo['e']` 仍保留原 scalar fade 的诊断值，但它**不再定义**新的多谐波材料图；运输必须使用完整 `theta`，不能沿用旧单正弦逆图。

## 4. 暖态运输必须连同背景及竖直均值一起处理

`transport_state_jets(oldflow,old_pp,newflow,s,N)` 实现 R93(8)–(13)。旧状态以圆柱分量存储，函数先加入旧已知背景并求出 Cartesian 位置与两 jet，再解

$$
\Theta_o(s,\Phi(s,\psi))=\Theta_*(s,\psi),
$$

使用完整链式法则运输。之后才减去新背景并投影：

$$
q_*Y_*^{(j)}=P_M\partial_s^j[\widehat X-B_*],\qquad j=0,1,2.
\tag{9}
$$

因为新圆柱基仅依赖 $\psi$，$P_M$ 与固定 $\psi$ 的 s 导数交换，故这三个投影准确对应新暖态的值、一阶和二阶 jet。该陈述是投影算子的关系；有限重投影一般会改变曲线，不能把它称为原实际像的准确运输。

还有一个实际容易遗漏的量：原状态没有记录整体竖直均值 $H(s)$。设 $\widehat X$ 是旧背景加旧非均值状态在新角图的运输，定义

$$
m_j(s)=\langle\partial_s^j\widehat X_z(s,\psi)\rangle_\psi,
\qquad j=0,1,2.
$$

新完整平均高度必须是

$$
H_*=H+m_0,\qquad H_*'=H'+m_1,\qquad H_*''=H''+m_2.
\tag{10}
$$

这是直接对角均值求导的结果。重新材料参数化通常不保持“对辅助角平均”；虽然这些常数被非均值 state 的投影杀掉，它们不能从完整 XYZ 运输中删除。函数因此返回 `mean_shift_jets` 并明确标记仍省略原 $H,H',H''$。它不凭空构造原均值积分，也不把返回的非均值 jet 当作完整闭面。

在 cut，两角图及全部两 jet 均为恒等，背景及两 jet 相同，因此 (9) 只剩同一有限 Fourier 向量的重现，(10) 的理论均值增量为零。真实尾 DN 的材料 Fourier 定义因此不变。若以后要把此接口用于生产，checkpoint 必须记录固定 `reference_coefficients` 与背景种类，restart 和导出器必须调用这些 jet；目前旧的只认识 round background 的源加载器与 exporter 不能自动解释它。现有生产没有选择这一接口。

## 5. 真实小诊断及其限制

命令为

```sh
python topics/visible-flexible-closed-surface/scripts/78718-geometry-support-reference-research.py \
  --checkpoint topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --linear-port topics/visible-flexible-closed-surface/notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json \
  --source-root topics/visible-flexible-closed-surface/repro/source-root \
  --out topics/visible-flexible-closed-surface/notes/2026-11-10-78718-geometry-support-reference-interface-research.json
```

实际 `fbd8c0/session24951` 启动，`e313ba` 自然 exit0，约1.024秒；0 BVP、0 DN、0径向积分。没有保存新的候选曲线。

1. 同一 c* 的新入口扰动状态逐值为0，位置与一阶入口差逐值为0。解析上它的相对 G 准确为0；N2048 浮点计算的 G Fourier-l1 为 $5.85062\cdot10^{-15}$。原未锚定回调同样诊断约 $1.30246\cdot10^{-9}$。这不是用采样给连续上界，连续零来自参考入口的公式。
2. 在 cut，`theta,rho,rhop,v,vs,vp,pos,p1,p2,s1,s2,sp,spp` 与原 flow 的实际数组最大差均为0。
3. 在5个内部点，沿实际有限状态方向，以 $10^{-25}$ 复步比较原有限 Jacobian 与新 RHS，relative L2 差为 $9.50308\cdot10^{-16}$。径向曲线值路径的中心差分对 `velocity_s` 的 relative L2 差为 $1.49143\cdot10^{-10}$，步长 $2\cdot10^{-6}$；后者是有限差分诊断，不是严格导数误差界。
4. 11个径向点、每点2048角的材料逆图残差至多约 $1.78\cdot10^{-15}$。新投影暖态相对未投影运输的 Cartesian 位置、一阶、二阶最大差约为 $8.64\cdot10^{-11}$、$9.73\cdot10^{-10}$、$2.13\cdot10^{-9}$。这诚实记录了重投影引入的表示变化。
5. 同11点平均高度运输的 $m_0,m_1,m_2$ 最大绝对值约 $5.70\cdot10^{-8}$、$2.70\cdot10^{-7}$、$8.24\cdot10^{-6}$。它们并非可忽略的“恒为0”项；不是全径向上界。
6. 运输的原 UNSOLVED global-Z warm 与新投影暖态的 G Fourier-l1 峰分别约 $1.15397904\cdot10^{-6}$、$1.15397958\cdot10^{-6}$。因此这次表示工具并未解决已经定位的 global-Z 暖态缺陷，仍须真实 BVP。

最后，用纯诊断方向 $d_1=10^{-4}$、$d_{15}=10^{-6}$、其余0，取缩放 $1,1/2,1/4,1/8,1/16$，实际锚定入口的有限 FFT-l1 依次约

$$
1.83017\cdot10^{-7},\quad4.55524\cdot10^{-8},\quad
1.13627\cdot10^{-8},\quad2.83749\cdot10^{-9},\quad7.08977\cdot10^{-10}.
$$

这与 R91/R93 已证明的二阶余项一致；这些参数只用于局部公式检查，没有用来优化当前主计算，也不是五张新的联解。可选接口已能在真实有限方程里使用，当前剩余工作仍是所选同一物理 g 的真实联解及其全域几何指标。
