# R150 附录：Phi 原 N1 斜率补图的精确六行两列呈示及三个完整原八次标量

日期：2026-11-28（Asia/Taipei）。  
范围：当前一般 unit211 的 $\Phi=0,D\ne0$ 原图；整第一二次头已付。  
状态：本次唯一实际运行完整返回；整个新斜率零权面、所有未付标量内容和首项零面仍保留。

## 1. 定理与本次实际数据

沿当前原权环，三个完整原均值记为 $q_R,q_W,q_O$，第四式记为完整原 $q_N=N_1$。前三式的真实二次头 $H$ 已由[整 H1 排除](R150-appendix-unit211-Phi-zero-whole-H1-complete-original-exclusion.md) 支付。其规则给出第四式的准确线性余式
$$
n=p_0(\lambda)+p_1(\lambda)T+p_2(\lambda)z,
\qquad
\deg_\lambda(p_0,p_1,p_2)\le(2,1,1).
\tag{1.1}
$$
写
$$
p_1=a\lambda+b,\qquad p_2=c\lambda+d,\qquad
\Delta_N=ad-bc=ap_2-cp_1.
\tag{1.2}
$$
$a,b,c,d$ 只含权参数。

实际 $\Delta_N$ 的约分后分子双次数为 $(31,16)$，总次数 33；只剥已经支付的 $\ell,M$ 权因子后，整剩余权支持 $C_\Delta$ 为
$$
\deg_{u,Q}C_\Delta=(25,13),\qquad
\deg_{\rm tot}C_\Delta=27,
$$
共 231 项，profile SHA256 为

`bd95b5a6a4379af906872b84a75dc97539695c7e1615916dc3523ab6a5d5b41b`。

没有声称这个多项式不可约，也没有关闭其整零集。

在明确的 $\Delta_N\ne0$ 补图，原四式理想
$$
I_4=(q_R,q_W,q_O,q_N)
$$
的商有下面的完整表示：

1. 一个真实首一二次式
   $$
   P=\mathcal Z^2-\beta_1(\lambda)\mathcal Z-\beta_0(\lambda),
   \qquad
   \deg_\lambda\beta_0\le3,\quad\deg_\lambda\beta_1\le2;
   $$
2. 三条 $\mathcal Z$ 线性余式 $r_R,r_W,r_O$；
3. 作为权环加物理 $\lambda$ 上的模，全部关系精确由
   $$
   r_R,\ \mathcal Zr_R,\ r_W,\ \mathcal Zr_W,\ r_O,\ \mathcal Zr_O
   $$
   六行两列给出。

这是真正的理想与模的双向表示，不是仅在解点上的必要行集合。仅首一二次环境被称为自由秩二；原商不假定自由。

此外，本次从每个完整原均值余行及其真实 $\mathcal Z$ 子行返回了三个新的原标量
$$
P_R(\lambda),\quad P_W(\lambda),\quad P_O(\lambda)\in I_4.
\tag{1.3}
$$
它们都对 $\lambda$ 恰为八次，完整多项式信息如下。

| 原来源 | 双权次数 | $\lambda$ 次数 | 总次数 | 项数 |
|---|---:|---:|---:|---:|
| $r_R,\mathcal Zr_R$ | $(118,62)$ | 8 | 126 | 39468 |
| $r_W,\mathcal Zr_W$ | $(117,61)$ | 8 | 125 | 38120 |
| $r_O,\mathcal Zr_O$ | $(120,63)$ | 8 | 130 | 40947 |

所有未付权内容和 $\lambda$ 首项都仍在这些完整多项式中。这里没有把任何一个八次首项宣为单位，没有借其形式次数宣称整个原图有限或为空。

## 2. 原四式与斜率坐标的完整同构

记 $v=(1,T,z)^t$，$w=(T^2,Tz,z^2)^t$，令前三原二次式的低次部分为 $L v$，则
$$
(q_R,q_W,q_O)^t=Hw+Lv,\qquad
\mathcal R=-H^{-1}L.
$$
于是准确原规则是
$$
w=\mathcal Rv+H^{-1}(q_R,q_W,q_O)^t.
\tag{2.1}
$$
若第四原式的二次头是 $h_N$，其低次行是 $\ell_N$，则
$$
q_N=(\ell_N+h_N\mathcal R)v
   +h_NH^{-1}(q_R,q_W,q_O)^t
 =n+h_NH^{-1}(q_R,q_W,q_O)^t.
\tag{2.2}
$$
因此
$$
I_4=(n,q_R,q_W,q_O).
\tag{2.3}
$$

在 $\Delta_N\ne0$ 上，作同一可逆仿射变化
$$
\mathcal Z=aT+cz,\qquad \nu=p_0+p_1T+p_2z.
$$
其完整逆变换为
$$
T=\frac{p_2\mathcal Z-c\nu+cp_0}{\Delta_N},\qquad
z=\frac{-p_1\mathcal Z+a\nu-ap_0}{\Delta_N}.
\tag{2.4}
$$
源码逐系数返回 $aT+cz=\mathcal Z$ 和 $\nu=p_0+p_1T+p_2z$；没有倒置 $\lambda$。

由 (2.3)，消去 $\nu$ 后，原四式商严格同构于三个真正代入式
$$
\widetilde q_i(\lambda,\mathcal Z)
=q_i\!\left(\lambda,
\frac{p_2\mathcal Z+cp_0}{\Delta_N},
\frac{-p_1\mathcal Z-ap_0}{\Delta_N}\right),\qquad i=R,W,O
$$
的商。源码还完整返回
$$
\widetilde q_N=h_NH^{-1}
   (\widetilde q_R,\widetilde q_W,\widetilde q_O)^t
$$
的全部三个 $\mathcal Z$ 系数，所以没有丢掉原第四式或其头零纤维。

## 3. 首一平方、三个线性余式与完整六行

用 (2.1) 降低
$$
\mathcal Z^2=a^2T^2+2acTz+c^2z^2.
$$
记
$$
r=(a^2,2ac,c^2)\mathcal R,\qquad
\sigma=(a^2,2ac,c^2)H^{-1}.
$$
在 $\nu=0$ 处，$rv$ 唯一写成 $\beta_0+\beta_1\mathcal Z$。故
$$
P=\mathcal Z^2-\beta_1\mathcal Z-\beta_0
 =\sum_{i=R,W,O}\sigma_i\widetilde q_i.
\tag{3.1}
$$
这三个完整系数已在本次实际计算中逐一返回。实际 $\beta_0,\beta_1$ 的 $\lambda$ 次数分别为 3、2；它们的分母只有旧权单位和本节明确的 $\Delta_N$ 补图单位。

若
$$
\widetilde q_i=q_{i,0}+q_{i,1}\mathcal Z+q_{i,2}\mathcal Z^2,
$$
置
$$
r_i=(q_{i,0}+q_{i,2}\beta_0,\ 
      q_{i,1}+q_{i,2}\beta_1).
$$
则所有九个系数的反向恒等式
$$
\widetilde q_i=r_i(1,\mathcal Z)^t+q_{i,2}P
\tag{3.2}
$$
也已返回。(3.1)–(3.2) 给出理想等式
$$
(\widetilde q_R,\widetilde q_W,\widetilde q_O)
=(P,r_R(1,\mathcal Z)^t,r_W(1,\mathcal Z)^t,r_O(1,\mathcal Z)^t).
\tag{3.3}
$$

设 $A$ 为当前原权环再倒置 $\Delta_N$，$R=A[\lambda]$。明确的环境
$$
B=R[\mathcal Z]/(P)
$$
自由秩二。其乘法为
$$
(r_0,r_1)\mathcal Z=(r_1\beta_0,\ r_0+r_1\beta_1).
\tag{3.4}
$$
任意多项式乘子在 $B$ 中都化为一次，故由三个 $r_i$ 生成的 $B$ 理想，作为 $R$ 模恰由 $r_i,\mathcal Zr_i$ 生成。源码实际返回每行第二次乘法
$$
\mathcal Z^2r_i=\beta_1\mathcal Zr_i+\beta_0r_i
$$
的全部六个系数。因此六行已经对整个 $\mathcal Z$ 乘法封闭，无需添加未经证明的自由三维交换条件。

## 4. 三个原八次标量的准确来源

对任一 $r_i$ 和其真实子行 $\mathcal Zr_i$，先仅乘 $A$ 中的权单位清分母，得到两条多项式行 $A_i,B_i$。取实际两个乘子
$$
\omega_i=((B_i)_1,-(A_i)_1).
$$
只在这两个乘子内部整除其共同因子 $g_i$，令 $\eta_i=\omega_i/g_i$。随后完整返回
$$
\eta_{i,0}A_i+\eta_{i,1}B_i=(S_i,0).
\tag{4.1}
$$
该恒等式在 $g_i=0$ 也成立，因为整除后的是新的真实多项式乘子；没有除去原方程或从单个标量的内容中漏掉零面。

三次实际 $g_i$ profile 相同，双权次数 $(7,5)$，32 项。每次 (4.1) 的两个列积和
$$
g_iS_i=\det(A_i,B_i)
$$
都实际乘回。最后只除当前权单位及明确的斜率补图单位，得到 (1.3)。各标量的准确 profile SHA256 为：

- $P_R$：`02eaddb578414cd0ee0662851845c9abde008e018f56c39ffaf87a2646b467d4`；
- $P_W$：`3b1caecf5be355d52489a66f4c807806a2323aabfe473dda6c03f3ee56fd46d0`；
- $P_O$：`4ffb147b10042103d4ac4836511e1962e4ea90a0e6aa7216fbbc3224456af85b`。

这些完整原标量可以作为后续同点输入。这里只记录源定义、次数与 SHA，不保存其可重算系数，也不增加任何完整再生审计门。

## 5. 当前可直接使用的纤维推论

若同时处在原 $P_6$ 真首项 $H_{19,11}\ne0$ 和本节 $\Delta_N\ne0$ 补图，已有完整必要式给首一 $\lambda^6$，本节给首一 $\mathcal Z^2$。故当前 $(\lambda,T,z)$ 必要环境由
$$
\lambda^j,\ \lambda^j\mathcal Z,\qquad 0\le j<6
$$
十二个元素生成；每个固定权点的长度和不同点数至多 12。

这个推论仅对上述两个明确补图的交成立。$C_\Delta=0$ 整曲线没有关闭，八次标量的首项亦未支付。个别完整原值式尚可继续加入；本定理没有把 $I_4$ 称为全部原问题的充分条件。

## 6. 实际执行身份

源码：
[2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py](../notes/2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py)。

源 blob `e7973898af760437428eea7ccc9aa8552b9b2db5`，12550 字节，SHA256

`c4af169436165777186a811ccbea1b242b64e0bd84ac14bde43289254c4a2332`。

唯一实际运行：

- run `46089342243`，job `140806329232`；
- 源提交 `86cf860e85d7aa440e67ec1c616ae856c947a99c`；
- 2026-11-28 00:42:51.817902 UTC 真 pull 后提交相同，根与课题 README 均无变；
- 97.787519007 秒，峰值 330620 KiB，内层退出码 0；
- stdout 8809 字节，SHA256 `5f387e990ab9012b2af3ae768268a66511830eee995d3517275030bdf8f145ad`。

完整四式二生成元呈示在 3.942 秒已返回，六行封闭在 13.084 秒已返回；三个新八次目标分别在 40.157、67.395、97.707 秒返回。没有把外层 workflow 的绿色代替这些实际原系数回执。

小回执：
[2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542-execution.json](../notes/2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542-execution.json)。

本次只读取旧 D cofactor 之前的 7097 字节必要规则定义。没有重放旧 P6/P9、弱 Popov、Gaussian、旧范数或完整 Gram 门。所有未付范围保持开放。
