# R150 附录：完整射影确定因子的 381 次上界、170 次余因子与额外乘子

日期：2026-11-15 UTC。作者：Astra-ISP-789f / root、literature_audit。AI-assisted，GPT-6 Astra Pro。

状态：本篇连接已证明的原射影 Gauss 引理、完整仿射模 31 长度、完整自然无穷远模 31 长度及已经支付的特征零局部来源。没有运行新的大矩阵计算。结论为真正特征零完整确定因子的次数上界及一个额外参数乘子的存在；原 $h_0$ 本身的全局来源成员性、未知支撑的消除及固定 $31$ 分母均未因此成立。

## 1. 同一原矩阵的完整射影 gcd

沿用[原自然齐次化与 Gauss 引理](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)。原矩阵的转置记为
$$
\mathcal M(s)\in\mathbb Z[s]^{6188\times4367},
$$
保留原十七式的全部次数至多三乘子，以及全部次数一至五输出。其函数域秩为 $r=4354$。来源 $m^uN_i$、$m^u\Gamma_i$ 的行权分别为 $20+10|u|$、$25+10|u|$；输出 $m^v$ 的列权为 $10|v|$。按这些原权取
$$
\widetilde{\mathcal M}_{iv}(s,t)=t^{a_i-b_v}\mathcal M_{iv}(s/t).
$$
令 $\Delta_{\mathbb Q}(s,t)$ 为全部非零 $4354$ 阶齐次子式的 gcd，取 primitive 整数代表。不同子式的总次数可以不同，以下始终取全部子式的共同因子。

[完整仿射模 31 计算](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)及其[原特征回执](../notes/2026-11-14-r150-torsion-characteristic-receipt-789f.json)给出
$$
\Delta_{31,\mathrm{aff}}
=s^{66}(s-2)^{32}(s+6)^{12}(s-1)^7P_+^8P_-^8E_6^5Q^2,
\qquad \deg\Delta_{31,\mathrm{aff}}=315.
\tag{1.1}
$$
这里 $P_\pm$ 是 $F_\pm$ 的首一模 $31$ 约化，
$$
P_+=s^3+26s^2+25s+17,\qquad
P_-=s^3+27s^2+24s+24,
$$
$$
E_6=s^6+13s^5+18s^4+2s^3+15s+30,
\qquad \overline E_8=5(s-2)(s-1)E_6.
$$
$Q$ 是同篇给出的五个首一不可约因子的乘积，次数分别为 $2,6,7,16,29$，故 $\deg Q=60$。此处使用的是完整挠子模的特征多项式，不是其次数 $190$ 的最小多项式，也不是九目标的消去多项式。

[完整原自然无穷远计算](R150-appendix-full-original-infinity-mod31-length66-and-output-projection-gap28.md)独立给出完整模 $31$ 最大子式阶 $66$。因而同一原自然齐次化的整个模 $31$ gcd 为
$$
\Delta_{31}(s,t)\doteq
t^{66}\bigl(\Delta_{31,\mathrm{aff}}\bigr)^h(s,t),
\qquad \deg\Delta_{31}=66+315=381.
\tag{1.2}
$$
上标 $h$ 表示按实际单变量次数齐次化，$\doteq$ 表示相差非零域常数。在无穷远局部图 $(s,t)=(1,u)$ 中，齐次 gcd 的 $t$ 重数就是全部原最大子式的最小 $u$ 阶，也就是同一完整原矩阵的局部最大确定因子阶；自然权及参数没有另换。因此 (1.2) 使用的是完整矩阵的 $66$，不是所选方阵的 $243$。

原矩阵在模 $31$ 的泛秩仍为 $4354$。由 Gauss 引理，primitive 的 $\Delta_{\mathbb Q}$ 在整数多项式环中整除每个原最大子式；约化后它不是零多项式，并保持齐次总次数。因此
$$
\overline{\Delta_{\mathbb Q}}\mid\Delta_{31},
\qquad
\boxed{\deg\Delta_{\mathbb Q}\le381.}
\tag{1.3}
$$
这里不要求 $\Delta_{\mathbb Q}(s,1)$ 的最高次系数在 $31$ 处为单位。

## 2. 除去全部已付公共因子后的准确余项

[原低投影双线性确定因子定理](R150-appendix-original-low-projection-double-linear-divisor-and-E8-local-target-membership.md)第 8 节给出
$$
K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,
\qquad \deg K_{158}=158.
\tag{2.1}
$$
这是原全部特征零最大子式的公共因子；二点的十二阶来自真实投影长度十二，并不要求二点的原 $h_0$ 目标已解决。另由[十七条真实五阶左延拓](R150-appendix-infinity-seventeen-fifth-left-jets-order53-and-cost8638.md)，原完整最大子式的无穷远阶至少为 $53$。

故存在 primitive 整数齐次多项式 $R_h$，相差符号无关，使
$$
\Delta_{\mathbb Q}(s,t)
=t^{53}K_{158}^h(s,t)R_h(s,t),
\qquad
\boxed{\deg R_h\le381-53-158=170.}
\tag{2.2}
$$
Gauss 引理在这里同样保证整数余因子：$t^{53}K_{158}^h$ 是 primitive，且已在 $\mathbb Q[s,t]$ 中整除 $\Delta_{\mathbb Q}$。

对 (2.2) 模 $31$，再使用 (1.1) 和 $\overline E_8$ 的真实分解，得到
$$
\boxed{
\overline R_h\mid
t^{13}(s-2t)^{16}(s-t)^3
(P_+^h)^2(P_-^h)^2E_6^h(Q^h)^2.
}
\tag{2.3}
$$
右边的总次数准确为
$$
13+16+3+12+6+120=170.
$$
式 (2.3) 是约化余因子的完整可能范围，并未把这些有限域因子命名为新的特征零异常点。

令
$$
\Delta_{\mathrm{aff}}(s)=\Delta_{\mathbb Q}(s,1),
\qquad
R(s)=R_h(s,1)=\Delta_{\mathrm{aff}}(s)/K_{158}(s).
$$
任一公共仿射因子的实际齐次化整除每个自然齐次最大子式；反过来，除去 $t$ 因子的齐次公共因子去齐次后仍是公共仿射因子。因此 $\Delta_{\mathrm{aff}}$ 确为同一完整仿射 gcd，而非只知它的一个下因子。

由于真实特征零无穷远阶至少为 $53$，
$$
\boxed{\deg\Delta_{\mathrm{aff}}\le328,\qquad \deg R\le170.}
\tag{2.4}
$$
这没有把原模 $31$ 仿射次数 $315$ 当成特征零仿射上界。比如 primitive 因子 $1-31s$ 的仿射约化是常数，而其齐次式 $t-31s$ 的约化是 $t$；这种未知有限根在约化时逃到无穷远的可能性已经保留在 (2.3) 的 $t^{13}$ 中。

## 3. 一个至多 170 次额外乘子的完整来源结论

记原固定来源模为
$$
L=\operatorname{im}A\subset\mathbb Q[s]^{4367},
$$
其中 $A=\mathcal M^T$，仍只使用原十七式的次数至多三乘子。原九目标是
$$
t_j=\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10,
$$
且
$$
h_0=s^3(s-2)F_+^2F_-^2E_8,\qquad \deg h_0=24.
$$
[原泛型像回接](R150-appendix-original-generic-image-bridge-exact-cubic-zero-cost-and-thirteen-free-heads.md)已证明全部 $t_j$ 属于 $L\otimes\mathbb Q(s)$。于是它们在 $\operatorname{coker}A$ 中都是扭类。

下面证明由 (2.2) 定义的同一个 $R$ 满足
$$
\boxed{0\ne R,\quad R\,h_0\,t_j\in L\quad(2\le j\le10),\qquad
       \deg(Rh_0)\le194.}
\tag{3.1}
$$

在 $s=0,-6,F_+,F_-,E_8$ 的各不可约局部环，已经分别支付原 $h_0t_j$ 的局部来源：零点三阶、负六点不需因子、两个三次因子各二阶，以及 E8 一阶。准确来源见上述零点回接稿、[负六完整局部证明](R150-appendix-minus-six-local-smith-length12-and-original-nine-target-membership.md)、[两三次数域证明](R150-appendix-both-cubic-fields-low-smith33-and-original-nine-target-local-membership.md)及第 2 节的 E8 定理。再乘 $R$ 不改变这些已成立的成员关系。

在 $s=2$，令 $W=(I^2)_{\le5}$ 为原共动正常理想平方的真实输出子模。全部九目标在 $W$ 中。由[原完整投影差长精确序列](R150-appendix-original-local-projection-length-gap-and-two-point-length-bound30.md)，
$$
\ell\bigl(W/(L\cap W)\bigr)=\delta_{A,2}-\delta_{P,2}
=\delta_{A,2}-12.
$$
另一方面，(2.1) 在二点的准确次数为十二，故
$$
v_{s-2}(R)=\delta_{A,2}-12.
$$
长度为 $\ell$ 的有限 DVR 模被参数的 $\ell$ 次幂消去。因此 $R$ 本身已经在二点局部消去整个 $W/(L\cap W)$，从而 (3.1) 的九个二点局部关系成立。这里没有假定 $h_0$ 在二点的一次因子已经足够。

最后，在其余任一不可约有限因子 $f$ 处，$K_{158}$ 为单位，所以
$$
v_f(R)=v_f(\Delta_{\mathrm{aff}})=\delta_{A,f}.
$$
该完整局部最大子式阶是整个局部扭子模的长度，至少为其最大 Smith 指数。故 $R$ 消去每个泛型像目标的局部扭类。

于是 $Rh_0t_j$ 在 $\mathbb Q[s]$ 的每个非零素理想处都属于原来源模。它又在函数域中属于原像，故其商类是一个在所有有限局部化均为零的扭元素。由 PID 上有限生成模的局部判准，该商类为零，证明 (3.1)。

## 4. 结论的范围与证据

$R$ 是明确由真正完整特征零 gcd 定义的余因子，但本篇没有计算其系数或证明它为常数。式 (3.1) 支付一个次数至多 $170$ 的额外参数乘子存在；它不支付原候选 $h_0$ 自身的全局成员性，也不提供参数来源系数次数的新数值、固定 $31$ 分母或指定最大子式的首项单位。

本篇只读取并连接已有证据，没有重复原模块正常形或任何大消元：

- 仿射完整特征回执为 completed、field31、torsionDimension315、characteristic.degree315；源码 SHA256 为 8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2，原实际计算 0.366523649 秒。
- 自然无穷远完整原计算 run43731615668、步骤 full-infinity-original-dual27-v2-through21，十四个正方向全部完成，总长66。原小回执 SHA256 为 540fd2d44e7d49f9d4284d8966e9994397320f145e353c1560c7807f76caf9b4。
- 特征零下界来自原真实第五 left-jet 计算 run43702348535、步骤 infinity-fifth-joint-high-low-left-envelope、execution470a799c88b44f67cb1f8504f619fd4949a37137：十个恒等方向加七条五阶延拓覆盖原6188来源，累积连接秩上界4,4,5,8,10，故最大/次大公共阶至少53/47。原实际15.752552958秒，raw14709B/SHA256381d159232a410c5a68a891b93dea6afe0b45e3f7a8ac7966b5470001d0b6970；并未把受限第五包络秩当作完整连接下界。
- 因此同时保真 $53\le\delta_{\mathrm{full},\mathbb Q}\le66$、$47\le\delta_{4353,\mathbb Q}\le55$ 及最大指数至多 $66-47=19$；真原输出投影长二给 $55\le\delta(A_{I,\mathbb Q})\le68$。这些收紧纠正近期摘要沿用43/39的遗漏，不改变旧真实证明，也没有把有限域单个指数搬到有理数域。
