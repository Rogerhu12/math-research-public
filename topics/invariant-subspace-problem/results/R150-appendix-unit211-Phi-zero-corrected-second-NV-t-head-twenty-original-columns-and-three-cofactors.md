# R150：正确 Phi 第二 NV 头的完整四元二十列与原 lambda 五、六、六次式

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**已完成的结果。** 在完整 NV 的第二 t 头
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0
$$
上，两个真正原首一二次构成自由四元环境。五条剩余原条件及其四个基倍数，已实际返回完整 $4\times20$ 同点关系列。三个事前固定四阶 cofactor 全部回到七个原分子，给出实际 lambda 次数 $5,6,6$ 的必要多项式。

三个标量都非零，但没有返回旧单位；其 lambda 头没有支付。本条不排除整个第二头，不宣布 Phi 为空，不改变已有公共权曲线或原点数界。完整 NS/PS、个别 N/P 及所有未付头零纤维继续保留。第一 NV 头的三标量 gcd 仍按原记录冻结。

## 1. 唯一实际执行与可读来源

唯一首次运行 [46170068898](https://github.com/Rogerhu12/math-research-public/actions/runs/46170068898)，job 141056253058，已经亲读全部十条内层数学记录。其实际结束值为：

| 项目 | 实际值 |
|---|---|
| 内层源 exit | 0 |
| driver 时间 | 4.379637370999994 秒 |
| 最后数学时间 | 4.300939481 秒 |
| 最大子进程 RSS | 54564 KiB |
| stdout | 39500 B |
| stdout SHA256 | d4d494a097d81b1f7cd7b446e8c45c1572a34d68689575682ab34636fbff10a1 |
| 源提交 | 7655c08e832cc748f1fa63c4487b3f8b2a07f5c5 |
| 真 pull 后提交 | 5e6fabfb5dfb5820b92bb0104d9cad43ff6e09d2 |
| pull/rules 时间 | 2026-11-28T17:22:02.282919+00:00 |

两份 README 均实际读取且未变。逐行去掉 Actions 时间戳后，十条源记录按原换行重构的 39500 B 与 driver SHA 完全一致；没有只依据外层工作流绿色判断数学成功。

可读来源为
[唯一完整源码](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-t-head-original-four-generator-columns-8542.py)、
[预定输入](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-t-head-original-four-generator-columns-8542-input.md) 和
[实际小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-t-head-original-four-generator-columns-8542-execution.json)。

源码 blob 为 d20becf217080f2f22bbe5b696822d3cddca9ec4，完整 SHA256 为
c7141ce12424d916ee415c0ac0121ea938ff206d20b5a8c12193bb3a1cdcdaa1。
本次零依赖，唯一预算 120 秒、1 GiB，外层 135 秒。没有泛域 gcd、因式、数值素数、点选择或重派。

## 2. 原范围和两个首一来源

设
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
M=\ell(2u-\ell Q)-u^2=4bc\delta,\quad
T_0=2u-\ell Q-2u^2,\quad J=2u(1-u)+\ell Q,
$$
$$
P_{02}=2s\ell Q,\quad K_w=Q+4s,\quad M_n=QM.
$$
仍在当前正确 Phi、distinct singleton、物理 $D_{\rm phys}\ne0$ 原图；所有实际分母只在旧纯权单位
$$
U=Q\delta sK_wLM_n
\tag{1}
$$
中。没有新 m、u、$2\ell-1$、$2u-3$、t、sigma、D 或 lambda 头的逆。

在整个 $B_2=0$ 上，令
$$
a=\lambda-\tfrac32,\qquad T=\ell a-m\sigma.
$$
由[正确全 t 模型](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)恢复
$$
E=\frac{P_{02}(T+\ell)}{T_0},\quad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},
$$
$$
V=f+bct-E,\quad A_1=2E,\quad W_1=T_0/2+2uf,\quad
w=\lambda-1-T.
\tag{2}
$$
原双点乘法一直是 $(vv')_1=v_0v'_1+v_1v'_0$。完整 Gram 的三个均值、N1 极化及完整 $N_4$ 都从同一点 (2) 生成；源实际返回 $E_0,N_0,P_1$ 的恢复身份，没有借用撤回的 wrong-Rbar 链。

物理向量的两个 singleton 值为
$$
h=\lambda-\tfrac12-\rho\sigma,\qquad
k=\lambda-\tfrac12+\rho\sigma,\qquad \rho^2=\delta.
$$
令
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
E_2=b(h-1)^2+c(k-1)^2-A_\lambda,\quad
E_3=b(h-1)^3+c(k-1)^3-B_\lambda.
$$
实际返回
$$
q_\sigma=\frac{E_2}{\ell\delta}
=\sigma^2-\frac{2ma}{\ell\delta}\sigma
-\frac{A_\lambda-\ell a^2}{\ell\delta}.
\tag{3}
$$
这是原第二矩的首一二次，所有复根、重根和幂零都保留。

另一方面，[全权首一 t 二次](R150-appendix-unit211-Phi-zero-corrected-whole-monic-t-quadratic-exact-ten-columns-and-four-generator-NV-head.md)给
$$
q_t=\gamma_R\mathcal R+\gamma_OE_{Bo},\qquad [t^2]q_t=1,
$$
$$
\gamma_R=-\frac{B_q}{\ell bcsQ},\quad
\gamma_O=-\frac{8\delta}{\ell},
$$
$$
B_q=Q^2+(2u^2-3)Q+2s(2u-1)(u-2).
\tag{4}
$$
这里 $\mathcal R$ 是正确的原均值差，完整原身份
$$
2\mathcal R+E_1-bE_B-cE_C=0
$$
和两个 t 二次头的 Bézout1 均在本次真实坐标中返回。$\gamma_O$ 本身是旧单位。

按 (3) 对 (4) 首一除 sigma，得到
$$
q_t=\widetilde q_t+w_sq_\sigma.
\tag{5}
$$
$\widetilde q_t$ 对 t 首一二次，其系数对 sigma 至多一次。因此
$$
\mathcal B=
\bigl(\mathcal A[\lambda,\sigma]/(q_\sigma)\bigr)[t]/(\widetilde q_t)
\tag{6}
$$
是 $\mathcal A[\lambda]$ 上真正自由四元代数，以
$$
e=(1,\sigma,t,\sigma t)
\tag{7}
$$
为基。自由性来自两次首一除法，只属于 (6)；没有假设最终原条件商自由。

## 3. 七原式的精确二十列呈示

本次原子理想是
$$
J_7=(E_2,\mathcal R,E_{Be},E_{Bo},N_1,E_3,NV),
\tag{8}
$$
其中 $NV=N_4(1,w,h,k)$ 为完整原值，$N_1$ 为完整原双点极化。源直接返回 $[t]NV=0$，但没有施加物理 $t=0$。

在 (6) 中，只需五条 seed
$$
\mathcal R,\ E_{Be},\ N_1,\ E_3,\ NV .
\tag{9}
$$
因为 (3) 消去 E2，(4) 和 $\gamma_O$ 的单位性消去原 EBo。对 (9) 中每条 F，依次乘 (7) 的四个基元，先首一除 t，再首一除 sigma。对每一个实际列，源完整返回
$$
m_0F=r+Q_t\widetilde q_t+Q_sq_\sigma
$$
以及回到原式的普通多项式身份
$$
\boxed{
m_0F=r+
\frac{Q_s-Q_tw_s}{\ell\delta}E_2
+Q_t\gamma_R\mathcal R+Q_t\gamma_OE_{Bo}.
}
\tag{10}
$$
最后 r 的四坐标也逐项重构。

五个 seed 的四列全部成功，合计二十个普通来源、八十个坐标。按 seed-major 次序，列号为：

| seed | 四列号 | 四列各自的 lambda 坐标次数 |
|---|---:|---|
| $\mathcal R$ | 0–3 | (2,1,1,0)，(3,2,2,1)，(3,2,2,1)，(4,3,3,2) |
| $E_{Be}$ | 4–7 | (2,1,1,0)，(3,2,2,1)，(3,2,2,1)，(4,3,3,2) |
| $N_1$ | 8–11 | (2,1,1,0)，(3,2,2,1)，(3,2,2,1)，(4,3,3,2) |
| $E_3$ | 12–15 | (3,2,−1,−1)，(4,3,−1,−1)，(−1,−1,3,2)，(−1,−1,4,3) |
| 完整 $NV$ | 16–19 | (3,2,−1,−1)，(4,3,−1,−1)，(−1,−1,3,2)，(−1,−1,4,3) |

负一次表示零坐标，不表示 Laurent 极点。E3/NV 的分块来自它们在该原头上完整不含 t；t 仍由 (6) 保留。

这二十列的 cokernel 精确呈示 (8) 在 (6) 中的原商。理由是 (7) 是一个真实结合代数的基，任何 seed 的理想由它的四个基倍数生成。没有把一个裸四坐标矩阵当成无关系的代数，也没有仅凭某个数值秩得出该呈示。

## 4. 三个固定 cofactor 与七原分子完整返回

事前固定的列组为
$$
(0,1,4,8),\quad (0,1,4,12),\quad (0,1,4,16).
\tag{11}
$$
对每组 B，源取完整列 $\omega=\operatorname{adj}(B)e_0$，其中每个分量为删首行的三阶 cofactor。实际四坐标返回
$$
B\omega=F e_0,\qquad F=\det B.
\tag{12}
$$
三组共十二个坐标全部通过，没有倒任何行列式或 lambda 首项。

再把 (10) 的全部原来源代入，得到
$$
F=\sum_{i=0}^6\Omega_iF_i,
\tag{13}
$$
其中 $F_i$ 为 (8) 的七原式。将 $F_i=N_i/d_i$ 转成七个原分子后，只按以下顺序处理：

1. 合并七个实际原乘子，并完整返回 (13)。
2. 清除它们及 F 的实际分母，普通多项式乘回。
3. 只同时约掉全部七个原乘子的共同多项式因子，再完整乘回。
4. 只移除 (1) 的旧单位支持；七个最终乘子再次返回同一个原标量。

第一、第二组的共同乘子因子实际总次数二、双次数 $(2,1)$，五项；第三组共同因子是常数一。这里没有凭标量自身的内容约原方程。所有原共同因子零面和矩阵主元零面都通过最终普通身份保留。

最终得三个非零原必要多项式
$$
C_N(u,Q,\lambda),\quad C_H(u,Q,\lambda),\quad C_V(u,Q,\lambda)
\in J_7\cap\mathcal A[\lambda].
\tag{14}
$$

| 标量及固定列组 | $\deg_u$ | $\deg_Q$ | $\deg_\lambda$ | 总次数 | 项数 |
|---|---:|---:|---:|---:|---:|
| $C_N$，(0,1,4,8) | 33 | 18 | 5 | 40 | 2298 |
| $C_H$，(0,1,4,12) | 30 | 16 | 6 | 36 | 2109 |
| $C_V$，(0,1,4,16) | 33 | 18 | 6 | 39 | 2605 |

三个实际 profile SHA256 依次为：

- CN：00ec850d85a28217080f50ce6b57b6901930929beffec4f1464dfb9813dfe15e。
- CH：273c1dca874c425bb126ec83ff62f238047dc1027dab6fae5967031081f6bcec。
- CV：bde71005f5967415ced9c34067679ae11c8bf082568cd687df7568609d570d27。

这些对象由固定源、(11) 的实际列及完整七源处理唯一给定；没有保存系数载荷。

给基权 $(0,1,1,2)$，两种首一除法保持总几何次数。三组列的几何次数分别为 $(2,3,2,2)$、$(2,3,2,3)$、$(2,3,2,3)$，减去基权和四，得到 lambda 上界 $5,6,6$。本次实际次数达到这些上界；这并不支付各个头在所有权点非零。

## 5. 实际 lambda 头与未付零纤维

三条原式的实际 lambda 头为：

| 头 | $\deg_u$ | $\deg_Q$ | 总次数 | 项数 |
|---|---:|---:|---:|---:|
| $[\lambda^5]C_N$ | 32 | 18 | 35 | 353 |
| $[\lambda^6]C_H$ | 29 | 16 | 30 | 298 |
| $[\lambda^6]C_V$ | 32 | 18 | 33 | 368 |

其 SHA256 分别为
0b2d51fc455e5837223c7a96a2f22e41406705ba3fe2cc8f8b442644b93f3d3c、
7033f974ff2ea690d0f5f410e1f9eb8feeb172010875602062462bca1f470973、
bb3817331543a5e973309461b83173a684e5e5914a2cbc14eba77b09e754d88a。

本次没有对它们因式分解、互素性或单位理想作结论。所有三个头共同为零的完整权纤维保留；不将 (14) 称为全权首一 lambda 式。

完整统计为：15163 次精确乘回除法、8 条两个首一来源身份、41 次首一除法返回、20 条原列来源、80 个列坐标、12 个固定 cofactor 坐标、15 次七原式完整返回，以及 21 个最终乘子分母支付返回。

## 6. 结论边界

本次成功的是同一原 sigma、同一原 t 的完整四元呈示与三个固定原必要多项式。最终没有返回旧单位，也没有执行三标量 gcd；因此整个第二 NV 头仍开。

(8) 只是完整物理条件的必要子理想。原 NS/PS、个别 N/P、其它同 sigma 条件与所有物理开图继续保留。本文没有把三条独立必要多项式的共同零集当作物理充分模型，也没有把 (6) 的自由性移到最终商。

后续真正新输入可加入尚未用到的完整原值，或研究新的同点关系；本次二十列、三个 cofactor 和七源返回已完成，不作为新的 gcd 或改序目标重跑。第一头三标量泛域 gcd 与 Q 主分量资源边界继续保持冻结。
