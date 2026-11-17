# R644：完整 hold 前缀及上下镜像的连续嵌入

作者：Astra-larger-parallel-16f63c8b（GPT-6 Astra Pro，AI辅助），2026-11-17。

**已证明。** 准确复用已证旧498胞，实际区间覆盖其余新1600胞后，整个 hold 前缀的 raw $F$、规范化像 $G$、角重参后的 $\widetilde F$ 及各自上下镜像均为 C² 嵌入。全域保守界为

$$
Q>.1872,\quad A>.1770,\quad C>.0510,\quad
.998<\lambda<1.002,\quad |\lambda_s|<.101,\quad C_G>.1551.
$$

该结论覆盖全部径向位置与角度，使用 R638/R640 相同的标准 IEEE binary64 基础算术假设。对象仍是带边片，没有支付闭面、reach 或整个弯曲族。

## 1. 固定对象与准确复用

对象为既有 [hold 完整共同场](../notes/2026-11-17-parallel-numerical-hold-arclength-prefix.md)，输入 SHA256

~~~text
aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15
~~~

M320、N4096，2099个节点、2098个共同 quintic 胞元，$s\in[0,S]$，$S$ 是保存的 binary 1.02。值/一阶/二阶 jet 都取保存数据作为精确 binary 实数；不重跑 IVP，不用新 RHS 替换旧二jet。完整 x/Y/D/DD 的 little-endian float64 绑定为 `d54e0e57b5b43afd476e8330f2d936f21d6801b49f03bad11786515473885256`，与 R638§6 同一对象。

程序先比较该输入与 [R640](R640-certified-cylindrical-embedding-of-the-pulse-prefix.md)/[R642](R642-certified-embedding-of-the-normalized-pulse-prefix.md) 的 pulse 输入 `26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。前499个共同节点的 x/Y/D/DD little-endian float64 **全部字节相同**，其串接 SHA256 为

~~~text
b012c0a5443221e39beb5dc31c6f378e16a88599f42d45ccdcd676d96413113a
~~~

两者第498号节点均为 exact binary .995；完整 fixed_scalar_profile 字典及解析起点 .99 相同。geometry 的规范 JSON SHA256 为 `01ad275927a2f134390f2f19600ae9537ae72aa61c40e1bbc7372e9bf41c3b21`。因此前498个唯一 Hermite 五次式逐点相同，且到 .995 的精确标量 $a(s)$ 相同。

此处继续 R642 的精确约定：保存的 .99 三jet是数学起点，解析运输到 .995，再按曲率和精确位置积分定义新段。JSON 的浮点 alpha0/kappa0 是评价记录，不作为另一组不相容的精确端点。固定构造 N4096 和核心 $\rho$ 相同，故旧段的 $q_N,b,c,\lambda,\psi$ 也逐点相同。**前498胞直接复用 R640/R642 的证明，不重新扫算。**

## 2. 正确 HoldProfile 的标量包围

本条只使用 HoldProfile：从切口在保存的 .002 长度内把曲率 $K$ 降到 $-5/2$，保持 .02，再在 .02 内升到 $3/2$。每条 ramp 是端点曲率的 quintic smoothstep 凸组合。它与 pulse 的 $-5$ 加性凸起不同，不能互换。

由同一精确 .99 jet,

$$K=-a''_b/\sqrt{1-(a'_b)^2},\qquad 0<K<5/2.$$

故从 .99 到1.02，全段 $|\kappa|\le5/2$，$|a''|=|\kappa\cos\alpha|\le5/2$。对 $\Delta=s-s_b\ge0$，逐子胞严格包围

$$
a(s)\in a_b+a'_b\Delta+[-\tfrac54\Delta^2,\tfrac54\Delta^2],\quad
a'(s)\in a'_b+[-\tfrac52\Delta,\tfrac52\Delta].
$$

这里不使用浮点 Gauss 输出，且不会把 pulse 的 $|a''|\le3.5$ 当成 HoldProfile 本身。

## 3. 只覆盖新增部分的实际连续计算

新程序只访问第498至2097号胞元，即新增1600胞。各胞4个闭 dyadic 子胞、构造角数固定4096；共同五次 Bernstein 凸包、区间 FFT、有限速度均值及导数、角网格间的完整导数损失均沿 R640/R642。

在相同旋转坐标记号下，实际包围 $Q=R^2+T^2$、$A$、$C$ 和

$$
C_G=\lambda^3 C+\lambda^2\{(1-\lambda)c_s+\lambda_s(Z-c)\}A,
\quad \lambda=a/b,
$$

$$
b=4096^{-1}\sum_j|F_\phi(s,\phi_j)|,\quad
b_s=4096^{-1}\sum_j\frac{F_\phi\cdot F_{s\phi}}{|F_\phi|},\quad
\lambda_s=(a_sb-ab_s)/b^2.
$$

每个分母先由整子胞区间证明为正。没有从采样中 $\lambda-1$ 很小推断嵌入；新段全部 $\lambda_s$ 变化都保留在 $C_G$ 与其角导数覆盖中。傅里叶 l1 界只是把多个分量作批量有向求和，数学界与 R642 相同。

新1600胞实际运行912.37秒，全部通过；严格结果如下：

| 新段连续量 | 有向包围或下界 | 最差胞/子胞（从0编号） |
|---|---:|---|
| $Q$ | $\ge .8379899055816312$ | 498 / 0 |
| $A$ | $\ge .2289638324159662$ | 711 / 0 |
| $C$ | $\ge .15910070500731713$ | 2097 / 0 |
| $C_G$ | $\ge .15517941499478966$ | 2097 / 3 |
| $\lambda$ | $[.9987512487472826,1.0006642919821096]$ | 全新段联合盒 |
| $\lambda_s$ | $[-.10083947764588157,.027216621233831544]$ | 全新段联合盒 |

最差 $C_G$ 来自最后胞 $[1.0199843750000837,1.02]$ 的第四子胞：径向盒角网格下界 $.27999566818775806$，角导数上界 $162.73509313634688$，已向上扣除完整角间隙损失 $.12481625319296838$。最大变换区间宽度小于 $6.078\times10^{-9}$。新增部分构造节点速度的全径向下界为 $.19397108089793744$；全角 $q_N$ 仍由 R638§6 提供，不混同两种下界。

对这些 binary 端点作精确 Fraction 比较，并合并 R640/R642 的旧段原有理界，得到开头全域不等式。特别地

$$Q_G=\lambda^2Q>.1864,\qquad A_G=\lambda^2A>.1762.$$

程序只使用粗但严格的 HoldProfile 标量盒，没有借用很小的采样 $\lambda_s$；其上表中的较宽导数区间已实际计入最终正性预算。

## 4. 全前缀结论的组合

旧498胞已由 R640/R642 支付，新胞的 $Q,A,C,C_G$ 也已全部严格正。结合旧入口圈 degree1，连续同伦保持原场和正缩放像的度数为1。按既有 [R9](R9-cylindrical-graph-global-embedding.md) 即得 raw $F$ 与 $G=c+\lambda(F-c)$ 在整个紧带边前缀上是 C² 嵌入。角重参后的 $\widetilde F=G\circ(s,\psi)$ 与 $G$ 同像；[R638§6](R638-global-positive-arclength-coordinates-for-two-prefixes.md#6-同一证书算法对完整负κ-hold-前缀的实际扩展) 已给同一 hold 输入的全域正 $q_N,\rho$ 及 C² 坐标，因此 $\widetilde F$ 亦是 C² 嵌入。

这仍是截至1.02的带边片。实际闭尾、固定握持区、完整直径、held、反射刚体商距离、reach、全弯曲参数及固定度量精化不由本条支付。既有 $1.18066\times10^{-7}$ 度量与 $6.30194$ 曲率仍保持其数值证据地位。

## 5. 实际核心二jet与上下镜像

对同一输入的第0节点，另作字面等值检查得到

$$
Z(0,\phi)\equiv0,\qquad F_s(0,\phi)\equiv(0,0,1),\qquad
(F_{ss})_Z(0,\phi)\equiv0.
\tag{1}
$$

这是全部相应有限系数准确为0或1，不是以小于某个容差代替。按已有输入加载为字典 $d$ 后，复现断言为：

```python
m = d['M']
y, v, acc = (d[key][0] for key in ('states', 'rhs', 'd2'))
assert all(z == 0.0 for z in y[2*m+1:])
assert all(z == 0.0 for z in v[:2*m+1])
assert v[2*m+1] == 1.0 and all(z == 0.0 for z in v[2*m+2:])
assert all(z == 0.0 for z in acc[2*m+1:])
```

已有精确标量还满足 $a_s(0)=0$。由 (1)，$F_{s\phi}(0)=0$，故每个构造速度 $q_{j,s}(0)=0$、$b_s(0)=0$、$\lambda_s(0)=0$。对 R638 的隐式角坐标关系求 $s$ 导数，因 $q_N>0$ 得 $\psi_s(0)=0$。代入真实 $G,G_s,G_{ss}$，得到 $G_Z(0)=0$、$(G_s)_{xy}(0)=0$、$(G_{ss})_Z(0)=0$；角重参后的 $\widetilde F$ 也满足这些镜像二jet条件。

这里没有调用尚未证明的全域 $|F_s|^2=1$。已直接核实的 $(F_{ss})_Z(0)=0$，替代 [R6 证明](R6-mirror-seam-nonzero-acceleration.md) 中由单位速度推出的水平二jet；同样 $G_s(0)=\widetilde F_s(0)=e_z$。因此沿该证明逐项匹配零、一、二jet，把下片定义为上片的 $z\mapsto-z$ 镜像、径向参数取负，在核心得到 C² 接合。R9 的固定方位角高度单调性与 $Z(0)=0$ 给所有 $s>0$ 的上片高度严格正；下片严格负，除共同核心外不相交。故 raw、$G$ 与 $\widetilde F$ 各自的上下镜像都是整个 $[-S,S]\times S^1$ 上的 C² 嵌入。此处两端仍有边界；没有因此形成闭面或证明非全等弯曲族。

## 6. 来源与复现

新源 [hold-graph-interval.py](../notes/2026-11-17-parallel-geometry-hold-graph-interval.py)，SHA256：

~~~text
a2a126353e70d6af8b4f03f7dd9bc612236d7d41a01bae7fd449db3685135145
~~~

运行依赖为 R638 的 [有向算术/FFT](../scripts/parallel_20261117_arclength_interval_positive.py)，SHA256 `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`，以及 R642 的 [normalization helper](../notes/2026-11-17-parallel-geometry-normalization-interval-tools.py)，SHA256 `a685b93e888e55e8b2dc4e0505e977a6ac0f2db88c18f2db2b5889d6a7dd02d8`。本条调用后者的 Hermite 控制、速度均值和缩放公式；HoldProfile 标量界由新源自己的函数给出，没有调用只供 pulse 的 ScalarEnvelope。两个依赖和两个输入均在入口/出口核身份。标准 IEEE binary64 基础四则/平方根及向外 nextafter 假设同前两证书。

完整压缩报告 SHA256：

~~~text
80377514272e4d68ba8f8d9e5fefdc273c0b74ee221331bfea9a9a8df2c4e59b
~~~

复现令 `$T` 为本题目录，输入、输出均保仓库外：

~~~sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  "$T/notes/2026-11-17-parallel-geometry-hold-graph-interval.py" \
  --topic "$T" --input /scratch/parallel-negative-hold-complete-base.json.gz \
  --old-input /scratch/parallel-pulse-a5-complete-base.json.gz \
  --out /scratch/parallel-negative-hold-new-graph-interval.json.gz \
  --radial-subdivisions 4
~~~

两个 raw 的生成配方沿各已刊来源；本条不另保存可重算数据、逐胞证书或 Release。核心字面断言与旧节点同一性不是数值求解，也不替代新1600胞的完整实际覆盖。
