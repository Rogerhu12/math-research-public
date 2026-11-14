# R141：正仿射字符下完整加速度层的协变与新 J 的必要符号门

日期：2026-11-14。**已证明。** 本稿只作纸面推导，并读取 R136 已发表导出的十个真权负二记录的状态键；没有重新评价原式、编译响应或扫描剩余九个非成员目标。

依据 [R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R127](R127-positive-affine-character-of-the-fourth-cost-cone.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R134](R134-acceleration-layer-from-complete-local-v4.md)、[R136](R136-acceleration-coefficient-beyond-response-and-G-orbit.md)、[R137](R137-real-fast-pulse-positivity-and-acceleration-PSD.md) 与 [R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md)。

本稿给出一个准确的路线区分：R136 的 J 已在真实 span 商中独立；对可能剩余的正性障碍，它必须满足下面的 PSD 条件，但目前没有被迫为零。因此不能据此宣布 J 可取任意正负成本。

## 1. 泛函与真实仿射作用

记 $U=\mathcal U_4,R=\mathcal R_8$。令 λ 是一个满足

$$
\lambda(R)=0,\qquad
\lambda\circ\mathsf P_{H,d}=H^\sigma\lambda
\quad(H>0,\ d\in\mathbb R)
\tag{1}
$$

的实泛函，其中 $\sigma\in\mathbb Z$。本节到第 5 节的协变只需 (1)；若再假设 λ 为真实成本闭锥的非负泛函，R137 的 PSD 门才适用。

R127 保证：若闭成本锥为真子锥，至少存在一个非零正泛函具有 (1)。它不保证该字符的权恰为 −2，也不声称其他一般正泛函都已经是字符。

完整真实路径变换为

$$
S=(h,k,\omega)\longmapsto
S_{H,d}=(Hh,k,(\omega+d)/H).
\tag{2}
$$

时间参数 s 不变；故

$$
(u,w,a,b)\longmapsto(Hu,w,Ha,b).
\tag{3}
$$

真实 $\omega_s=k_s/(2h)$、frame、空间相似变换、profile 与右锚输运都按 R89 保留。它不是仅代换某个局部系数多项式。

任取 λ 到 R130 有限局部环境 E 的线性延拓，记

$$
I(P)=\int_P\lambda(L)\,ds,\qquad L=L_0+L_2+L_4.
$$

对 M=0 的完整同 germ、frame I 路径，R109 给 $I(P)=\lambda(V_P)$；第三算子可非零，因为 R105 以真倒行把其 V 纳入 U。

## 2. 仿射局部积分的差只能是八矩端点项

固定 H,d，定义真实局部积分差

$$
J_{H,d}(P)=I(P_{H,d})-H^\sigma I(P).
\tag{4}
$$

它对拼接准确相加、对固定环境旋转不变、对同 k 真倒行保持同号。后两点来自完整局部式的几何导数权 0、2、4，不能用累计 V 的倒行代替。

若 P 为同 germ、frame I、M=0，则 $P_{H,d}$ 也满足这些条件，R89 和 (1) 给

$$
J_{H,d}(P)
=\lambda(\mathsf P_{H,d}V_P)-H^\sigma\lambda(V_P)=0.
\tag{5}
$$

R130 §§4–6 的端点纤维论证可原样用于这个局部积分差；为避免把它误当点态协变，简述其完整作用：

1. 对同 scalar germ、相同末 frame A 和矩阵 M 的两条路径，用同一真实目标 $A^{-1},-M$ 补偿。由 (5) 及可加性，它们的 J 值相同。
2. 所以 J 下降为 $SO(3)\times E_8$ 上的连续加法同态；R70 的局部平滑截面给连续性。SO(3) 的紧性使其到实数的连续同态为零，只剩矩阵线性函数。
3. 任一开 scalar 路径 P 与其真倒行组合，frame 是 $ADA^TD$，通常不是 I。由于上一步已允许全部 frame，且局部 J 倒行同号、矩阵也是同号，仍得到开路径的矩阵公式。
4. 真实 M=0 开端口桥比较不同 germ，证明同一个乘子适用于所有起止 germ。

因此存在依赖 H,d 和延拓的固定

$$
\beta_{H,d}\in E_8^*
$$

使所有真实开平端路径满足

$$
\boxed{J_{H,d}(P)=\beta_{H,d}(M(P)).}
\tag{6}
$$

这一步没有假定原局部势的基点已仿射协变，也没有删除端口常势。所有这些差已经被完整端点论证吸收到 (6)。

## 3. 最高导数层的准确积分协变

把任意固定 P 的时间缩放为 δ 倍。由 R112，(6) 的两边分别是

$$
\delta J_0(P)+\delta^{-1}J_2(P)+\delta^{-3}J_4(P)
$$

和

$$
\beta_{H,d}(\delta M_0(P)+\delta^{-1}M_2(P)).
$$

它们对每个 δ>0 相等，所以最高系数严格为零：

$$
\boxed{
\int_P
\bigl[
\lambda(L_4(S_{H,d};Hu,w,Ha,b,\ldots))
-H^\sigma\lambda(L_4(S;u,w,a,b,\ldots))
\bigr]\,ds=0.
}
\tag{7}
$$

(7) 对所有真实开平端 P 成立。这里是恒等式，不用负时长，也没有把完整 M 或 frame 假设为缩放不变。

## 4. 正规化后 A/H 的逐状态协变

R129 的边界势在两个常值 germs 上分别为零。将其正规式代入 (7)，仍有一个对所有开平端路径积分为零的同类正规式。

这种零积分首先迫加速度二次的三个状态系数为零：在任意状态 $S_0$ 用 $(h,k)=(h_0,k_0)+\varepsilon(\alpha,\beta)f$，除以 $\varepsilon^2$，任意方向给二次型恒零。随后这三个系数在整个状态域已恒零，非共线正负微幅脉冲除以 $\varepsilon^3$ 迫两个 H 系数恒零。最后可用共线脉冲的四次首项处理速度四次式。这里用的是零积分唯一性，不需将非负积分误读为各项独立非负。

记 $A_{ij}^\lambda=\lambda(\bar A_{ij})$、$H_i^\lambda=\lambda(H_i)$，得到

$$
\boxed{
H^2A_{hh}^\lambda(S_{H,d})=H^\sigma A_{hh}^\lambda(S),\quad
H A_{hk}^\lambda(S_{H,d})=H^\sigma A_{hk}^\lambda(S),\quad
A_{kk}^\lambda(S_{H,d})=H^\sigma A_{kk}^\lambda(S).
}
\tag{8}
$$

面积乘子准确为

$$
\boxed{
H^2H_1^\lambda(S_{H,d})=H^\sigma H_1^\lambda(S),\qquad
H H_2^\lambda(S_{H,d})=H^\sigma H_2^\lambda(S).
}
\tag{9}
$$

(9) 的两个 H 次数来自 $(H_1Hu+H_2w)\,H(ub-wa)$；不能给两者同一个次数。

取 H=1，d 任意，所有五个 λ 系数均独立于 ω。再从 $(1,k,0)$ 取 H=h、d=hω 到达任意 $(h,k,\omega)$，得到

$$
\boxed{
A_{hh}^\lambda=h^{\sigma-2}a(k),\quad
A_{hk}^\lambda=h^{\sigma-1}b(k),\quad
A_{kk}^\lambda=h^\sigma c(k),
}
\tag{10}
$$

$$
\boxed{
H_1^\lambda=h^{\sigma-2}p(k),\qquad
H_2^\lambda=h^{\sigma-1}q(k).
}
\tag{11}
$$

这些是完整真实 profile 泛函后的协变结论。没有假定未取 λ 的局部势逐点严格按同一规则变换。

## 5. R136 已发表十个真权负二系数的准确支撑

只消费 R136 的已发导出

~~~text
notes/actions-43654534244-1-acceleration_layer_mixed/
acceleration-layer-mixed-original-expressions.json.gz
~~~

其压缩 318634 B，SHA256 b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e；原始 1909429 B，SHA256 7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38。这里读取的是已有 selected_weight_records/family_records 元数据，不作任何新原式运算。

按原 candidate id 0 到 9 将十个真权 −2 两模式原算子记为 $J_0,\ldots,J_9$。其中 $J_0=J$ 正是 R136 已分离的新方向。实际原记录给出完整支撑：

| id | 族 | 状态单项 |
|---:|---|---|
| 0 | $\bar A_{hh}$ | $h^{-4}$ |
| 1 | $\bar A_{hh}$ | $h^{-4}k^2$ |
| 2 | $\bar A_{hh}$ | $h^{-3}k\omega$ |
| 3 | $\bar A_{hh}$ | $h^{-2}\omega^2$ |
| 4 | $\bar A_{hk}$ | $h^{-3}k$ |
| 5 | $\bar A_{hk}$ | $h^{-2}\omega$ |
| 6 | $\bar A_{kk}$ | $h^{-2}$ |
| 7 | $H_1$ | $h^{-4}k$ |
| 8 | $H_1$ | $h^{-3}\omega$ |
| 9 | $H_2$ | $h^{-3}$ |

每个所列状态单项的完整系数本身只有真权 −2；这些十项没有未列出的其他 profile 权或 log 项。因此

$$
\Pi_{-2}\bar A_{hh}
=h^{-4}(J_0+k^2J_1)+h^{-3}k\omega J_2+h^{-2}\omega^2J_3,
$$

$$
\Pi_{-2}\bar A_{hk}=h^{-3}kJ_4+h^{-2}\omega J_5,\qquad
\Pi_{-2}\bar A_{kk}=h^{-2}J_6,
$$

$$
\Pi_{-2}H_1=h^{-4}kJ_7+h^{-3}\omega J_8,\qquad
\Pi_{-2}H_2=h^{-3}J_9.
\tag{12}
$$

这些是原生产者已经保存的系数展开，不声称 $J_1,\ldots,J_9$ 互相独立。R136 的原式非成员只支付了 $J_0$。

## 6. 权负二正字符的四个准确零条件与 PSD 锥

现在限定 $\sigma=-2$，并假设 λ 是正泛函。由 (1)，它杀掉其他真权。由第 4 节的 ω 不变性及 (12)，准确得到

$$
\boxed{\lambda(J_2)=\lambda(J_3)=\lambda(J_5)=\lambda(J_8)=0.}
\tag{13}
$$

置

$$
a_0=\lambda(J_0),\quad a_2=\lambda(J_1),\quad
b_1=\lambda(J_4),\quad c_0=\lambda(J_6),\quad
p_1=\lambda(J_7),\quad q_0=\lambda(J_9).
$$

则

$$
A^\lambda(S)=
\begin{pmatrix}h^{-2}&0\\0&h^{-1}\end{pmatrix}
\begin{pmatrix}
a_0+a_2k^2&b_1k/2\\
b_1k/2&c_0
\end{pmatrix}
\begin{pmatrix}h^{-2}&0\\0&h^{-1}\end{pmatrix}.
\tag{14}
$$

R137 的逐状态 PSD 条件对所有 $k\in\mathbb R$ 成立，当且仅当

$$
\boxed{
a_0\ge0,\qquad a_2\ge0,\qquad c_0\ge0,\qquad
4a_2c_0-b_1^2\ge0.
}
\tag{15}
$$

证明：对角非负给前三个条件；行列式除去 h 的正幂后为

$$
a_0c_0+(a_2c_0-b_1^2/4)k^2,
$$

对所有 k 非负恰给最后一项。反向同样直接成立。

特别，

$$
\boxed{\lambda(J)=a_0\ge0.}
\tag{16}
$$

这并没有迫 $a_0=0$，也不证明存在满足所有完整正性条件的 λ。R136 的非零模 p 证书不含实数符号，不能把它拿来验证或违反 (16)。

面积乘子为

$$
H_1^\lambda=h^{-4}p_1k,\qquad H_2^\lambda=h^{-3}q_0.
\tag{17}
$$

若 $a_0=c_0=0$，PSD 先迫 $b_1=0$；在 k=0 处整个矩阵为零，所以 R137 给

$$
q_0=0.
\tag{18}
$$

若再有 $a_2=0$，则矩阵在所有状态恒零，R137 进一步给

$$
p_1=q_0=0.
\tag{19}
$$

没有从仅秩一退化或仅 $a_0=0$ 就擅自消掉 (17) 的全部面积项。

## 7. 本门能与不能说明什么

R136 否定了 $U=R+\operatorname{span}\operatorname{Orb}(G)$。本稿将新方向 J 接到真实正性问题：若余下障碍中有一个权 −2 的正仿射字符，它的十个已发加速度系数评价必须落在 (13)、(15)、(18)–(19) 所述约束中。

这些门只使用已经完成的真实协变、真实端口补偿和完整原记录。没有为其余九个算子重新运行成员扫描，没有把 scalar 状态表的形式系数直接视作有符号实际控制。

仍须检验是否存在同一个 λ 同时：

- 杀 R 及整个 G 轨道并满足 $N^*\lambda=0$；
- 满足这里及其他真权的相应协变/PSD 条件；
- 满足 R140 的同一八矩乘子对全部水平路径的完整 action 不等式。

这里没有证明一个这样的非零 λ 存在，也没有排除所有权的 λ。若未来能排除全部非零正字符，R127 才允许推出闭锥等于 U；即使如此，闭锥与实际半群、完整 ruling 和有限等距族仍需分别支付。

当前最准确的判断是：J 是已证独立的真实成本 span 方向，其在权 −2 正字符上的值只能非负；现有证据不允许将它当作已经可双向支付的新控制。
