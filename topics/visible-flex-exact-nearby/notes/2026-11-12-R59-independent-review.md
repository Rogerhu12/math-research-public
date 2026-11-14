# R59 恢复版的独立代数、区间和两单元审查

执行器丢失后，已原样重建旧验证器（SHA256 `6eec35d4153c3c7cfaff4fc8c1be8e465022152b466f89d4061775804d1c9d75`），
再逐式对照新的可恢复实现。此次实际审查源码
`scripts/fourfold_phase_modulus_characteristic_strip.py` SHA256：

`62c925991a373a2af66c4dc3fcf7667646675b850ec23c8ac6e2b852aad3ec7d`。

所审 R59 证明正文版本 SHA256：

`bb18e17fbbd1b5aa0ffb43d3305cf3143b461f03b4a4be0bf3c5ce196be08740`。

**结论：准确代数、复水平范数、连续边界门、模下界及商的两阶
上界成立；新源码的0与587两单元已实际重放通过。** 本审查只独立
重放两个单元，不将其扩张成完整592单元的数值证书。

## 1. 独立代数

在复正交移动标架 $(U,V,e_z)$ 中取

$$
T=(c,0,s),\quad X=(h,v,z),\quad
T_\theta=(-su,Pc,cu),\quad T_r=(-sq,pc,cq),\quad c^2+s^2=1.
$$

直接展开得到

$$
(T\times X)\cdot T_\theta=uv-Pc(cz-sh),\qquad
(T\times X)\cdot T_r=qv-pc(cz-sh),
$$

$$
(T\times X)\cdot(T\times X)=(cz-sh)^2+v^2.
$$

故 $n=-a^2D$、$m=-a^2M$ 与 $G=a^2(Q^2+v^2)$ 的符号正确。
这里 $h=X\cdot U$ 是 frame 分量，与支持函数 $F\cdot\nu$ 不同。
点积、叉积是双线性解析运算；不把 $G$ 换成非解析的 Hermitian 平方。

独立从 $X_\theta=a'T+aT_r$ 得

$$
h_\theta=a'c-aqs+Pv,\quad v_\theta=apc-Ph,
\quad z_\theta=a's+aqc.
$$

配合 $c_\theta=-su$、$s_\theta=cu$ 重新求导。$D_\theta$ 中
$PcuR-uPh=uPsQ$ 给出第二个 $-Pu sQ$；$M_\theta$ 中使用
$h=cR-sQ$ 给出同一 $B=Pq-up$。再次求导得到正文两阶式，未漏掉
$u_\theta,p_\theta,q_\theta$ 或 $a'$ 抵消项。

独立脚本 `fourfold_phase_frame_algebra_check.py`（SHA256
`a97ff3ccdea1104bb8cdaaa6a510f2abd9795feebcb1854066f9f7583e2de15c`）
恢复后已再次执行：11个恒等式的差模 $c^2+s^2-1$ 的多项式余式
全部准确为0，包括 $n,m,G,Q',R',D',D'',M',M'',G',G''$。

## 2. 复旋转与连续角域

对 $\phi=x+iy$，$\|U\|_2^2=\cosh(2y)\le e^{2|y|}$，$V$ 同理。
这是通常复 Euclidean 范数，因此足够控制双线性点积的模。水平
$X$ 先沿竖线积分得到 $H+\sigma H_1$，再与 $U,V$ 点乘时再付
$e^{I_\phi}$。代码中的两个 frame 因子有不同来源，基础角的虚部
也已计入 $I_\phi$。

由 $\sin\gamma=\gamma\int_0^1\cos(t\gamma)dt$，有
$|s|\le\Gamma e^{I_\gamma}$。若 $c_-=1-\Gamma^2/2>0$，
则 $\operatorname{Re}\cos\gamma\ge c_-$，不只是模下界。
独立求导 $z_{\theta\theta}=a'uc+a(q_\theta c-qu s)$；实轴的一阶
竖直 Taylor 项纯虚，所以代码的 $z_-=Z_--\sigma^2Z_2/2$ 是
合法的实部下界。

边界 $\operatorname{Re}P$ 的 cosh **双端区间**与带符号 beta 系数
相乘；代码没有仅使用 cosh 上端后错乘负系数。4096节点覆盖的是
物理角四分之一周期，最大最近节点距离为 $\pi/(4\cdot4096)$。
`P1` 恰是所需 $\sum(4k)^2|b_k|\cosh(4k\sigma)$ Lipschitz 界。
节点间误差已扣除，周期圆柱上的调和最小值原理再覆盖 strip 内部。
相位为准确有限三角多项式，此步骤不另欠 Fourier 截断尾。

## 3. 模门与舍入实现

全部正因子成立时，

$$
|Q|\ge|c||z|-|s||h|\ge c_-z_--S_0V_0,
$$

$$
|D|\ge|P||c||Q|-|u||v|\ge P_-c_-Q_--\bar uV_0.
$$

代码把 $Q_-$ 明确命名为模下界；没有冒称 $\operatorname{Re}Q>0$。
新实现将 $a_->0$ 放入局部 `positive` 条件，避免平方下界只依赖
外部前提。$|n|\ge a_-^2D_-$ 与原二阶实部法给出的合法模下界
可取较大者；新模门通过不意味着 $\operatorname{Re}n<0$。

全部上界由 `product`/`total` 逐次向上舍入；正乘积下界与差用
`Box` 下端。新实现的 `product` 包裹及 `Box` reciprocal 比旧版
可能多少量向外余量，故不要求报告字节相同。逐项核对 `m2`、
`g2` 与

$$
|(F/n)''|\le F_2/d+2F_1n_1/d^2+F_0n_2/d^2+2F_0n_1^2/d^3
$$

一致；wave factor 之后仍需乘实际 $\sqrt{-K_0}$ 和时间缩放。

新入口明确要求同源、同方向的完整R57实证书和其 proved 标志，
重新检查闭单元覆盖。resume 比较源/依赖/输入/参数与要求索引，
并要求已存行是索引的准确前缀。probe 即使所有选中单元通过，
`complete_radial_coverage` 与 `proved_uniform_denominator_nonzero`
仍为 false；完整592单元才可设置整域证明标志。

## 4. 恢复后的实际两单元重放

输入原点/方向 SHA 分别为
`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`、
`8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。
实证书 SHA 为
`b52537b755e7b5475dc945a5781c0d57a93e71ccdf39ec90891c236fcae2438a`。
物理角宽准确取 $1/64$。

| 量 | cell 0 | cell 587 |
|---|---:|---:|
| 径向闭区间 | $[0,.00045259580718443065]$ | $[.23837921545746676,.23881882318620012]$ |
| $\operatorname{Re}P$ 下界 | $.22152907924310533$ | $.5361061856994205$ |
| $|Q|$ 下界 | $1.1085866153592732$ | $1.132000069783157$ |
| $|n|$ 下界 | $.2804975468745544$ | $.5493744316826016$ |
| 旧实部法的 $\operatorname{Re}n$ 上界 | $+2.705278485255633$ | $+.31558397645501485$ |
| $|G_{\theta\theta}|$ 上界 | $2.2131338324839263$ | $238.77674501443005$ |

端点按准确 binary64 数解释。两单元均依赖新的模门，旧实部门在
此宽度不能给负值。关键模下界与丢失前重放一致；新报告按新源码
与字段重新生成，不复制旧数据。

新完整两单元报告 `notes/2026-11-12-R59-independent-two-cell-review.json`
SHA256：

`e19e0c77545be2b1b663be2684b25d996291d794f41c08b4522d59f3bcd69cd4`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_frame_algebra_check.py

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_modulus_characteristic_strip.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --direction topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --real-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_parameter_N_interval.json \
  --width .015625 --indices 0,587 \
  --out /tmp/visible-R59-independent-two-cell-review.json
```

本审查只独立重跑两个单元。场的复角定义域仍不等于实际返回域；
R60 的连续残差、二阶流管、两腿包含、初值覆盖与 Wiener 条件
仍须支付，更未因此完成精确等距闭曲面。
