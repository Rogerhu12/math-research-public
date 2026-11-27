# R150：原 Q=1−u 首项边界上整个 singleton 均值 y=1 支排除

**状态：已证明。** 在原 unit 2+1+1 非零孤立均值图中，共同规范 p+q=2 后，原均值坐标 X=x+yr、Y=x−yr 不可能同时满足 Q=1−u 和 y=1。本结论不要求原两线行列式 Delta 非零，也不假设 W=0。一般 Q=1−u 边界仍开放；普通 Hilbert ISP 未完成。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。日期：2026-11-27（台北）。

## 1. 同一原 Gram 与坐标

沿用已登记的原 U-value atlas、加权矩坐标和原 P1 双系数零排除。这里的 y 是 **singleton 均值 X、Y 的奇部系数**，不是 U 值 h−1 或 k−1。

原 Frobenius 代数为
$$
\mathcal A=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,\qquad
\tau(v)=a v_0+v_1+bv_B+cv_C,\quad a=1-b-c.
$$
其乘法为
$$
(v_0,v_1,v_B,v_C)(z_0,z_1,z_B,z_C)
=(v_0z_0,v_0z_1+v_1z_0,v_Bz_B,v_Cz_C).
$$
令
$$
p=1+r,\quad q=1-r,\quad r^2=1-Q,\qquad
\ell=b+c,\quad u=bp+cq.
$$
完整二次代数中
$$
b=\frac\ell2+\frac{u-\ell}{2(1-Q)}r,\qquad c=\bar b.
$$
本文只在 Q=1−u 上工作，故 r²=u，并保留整个二次代数、同一个 r 的配对。原已付条件给
$$
u(u-1)bcP_{02}\ne0,\qquad P_{02}=2P_0.
$$
特别
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
M=\ell V_2-u^2=4bcu\ne0.
$$
u−1 的原整支排除沿用
R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-isolated-mean-unit-base-complete-exclusion.md；
本文没有重新规范原 U_0。

以 X=x+yr、Y=x−yr 表示同一原 d=D_K1 的两个 singleton 均值。原 E0、N0、P1 给
$$
f=\frac{ux+(u-\ell Q)y-T_0/2}{2u},
$$
$$
\lambda=\frac{V_2x+(2u-uQ-\ell Q)y-uT_0-(V_2+2u^2)f+bcQt}{P_{02}},
$$
$$
T=\frac{gT_0-P_f f-\Phi bcQt}{QP_{02}}-\ell,
$$
其中
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q,
$$
$$
P_f=T_0(J-Q),\qquad g=\lambda P_{02}-(1-u)T_0.
$$
以上只除以原 u、Q、P02，不除 Phi 或 Delta。

从这些量重建同一原 Gram：
$$
r_G=X-a p-c t,\quad s_G=Y-a q-bt,\quad
A_1=2f-2bX-2cY+2bct,
$$
$$
K=\begin{pmatrix}
0&0&p&q\\
0&A_1&r_G&s_G\\
p&r_G&0&t\\
q&s_G&t&0
\end{pmatrix}.
$$
令 k_j 为其行，D_Kv=(tau(k_jv))_j，d=D_K1。后面所有式子都来自此 K；不把另一个嵌入的范数条件代替原同点式。

## 2. 使用的原行及完整加权迹

定义
$$
P_2(v)=\tau((v-\tau(v)1)^3),
$$
$$
N_4(v)=2\tau(dv^2)-2f\tau(v^2)-4\tau(v)\tau(dv)
       +4f\tau(v)^2+\tau(vD_Kv).
$$
原均值行为
$$
E_j=e_j-2(D_Kd)_j-2(d^2)_j+4fd_j,
$$
其中 e1=2tau(k0k1)，其余 ej=tau(kj²)。写 EB=EBe+EBo r。令
$$
P_j=3\tau((k_0-\tau(k_0)1)^2(k_1-\tau(k_1)1)),
$$
$$
N_H=N_4(k_0+k_1)-N_4(k_0)-N_4(k_1)-\frac{4\lambda}{3}P_j.
$$
原双点值给 NH=0。重建逐项核验
$$
\tau(d)=2f,\quad E_0=0,\quad
P_2(k_0)=P_{02},\quad N_4(k_0)=2\lambda P_{02},\quad
P_j=3(\lambda-1-T)P_{02}.
$$

令 A=2lambda²−2lambda+1、B=4lambda³−6lambda²+3lambda−1。原三矩及 w=lambda−1−T 给
$$
bh^2+ck^2=\ell+2T+A,\qquad bh^3+ck^3=\ell+3T+3A+B.
$$
因此以下两式是**同一原最高/第二梯度值的必要线性组合**：
$$
N_S=bN_4(k_B)+cN_4(k_C)-2\lambda P_{02}(\ell+2T+A)=0,
$$
$$
P_S=bP_2(k_B)+cP_2(k_C)-P_{02}(\ell+3T+3A+B)=0.
$$
它们没有删除原值条件，也没有被声称充分恢复全部 U 值。

设 nu=(u−ell Q)/u。两条 singleton 均值的可逆原组合为
$$
R_t=\frac{u}{2bc}\left(EBo+\frac{\nu}{u}EBe\right),\qquad
R_y=-EBe+\frac\ell2R_t.
$$
这里 1−Q=u，故每个除数均已付，Rt=Ry=0 与 EB=EC=0 等价。原恒等式还给
$$
[t]E_1=4bc(x-u-1).
$$
令
$$
H=(2u-1)\ell+u.
$$
直接在 y=1 返回原 Gram 得到关键因式：
$$
R_y\big|_{y=1}
=-\frac{(u-1)H}{M}\{\ell(u+1-x)-u\}. \tag{1}
$$

## 3. H 非零支：原 69 次完整覆盖

在 H≠0 上，(1) 强迫 ell≠0 并给
$$
x=u+1-u/\ell.
$$
此时 E1 的 t 系数为 −4bcu/ell，故原 E1 唯一恢复 t。准确式为
$$
t=\frac{
\ell^4(u-1)^2+4\ell^3u(u-1)
+4\ell^2u^2(u^2-u+2)-4\ell u^3(u+2)+4u^4
}{2\ell u^2 M}. \tag{2}
$$
不要求 (2) 分子非零。将同一个 x、y、t 代回 Rt、NH、NS、PS，然后令 h=ell/u。这里只逆已付 ell、u、M。

以下给出有限算术的完整可重建定义。把每个原有理式约成最简分子/分母，作 ell=hu；从分子中逐次准确除去与
$$
h,\ u,\ u-1,\ M,\ P_{02},\ H
$$
的 gcd，除到互素为止。记四个所得多项式为 R,N,S,P；选择任一非零有理内容归一不影响下述根覆盖。每次移除都只是原已付单位。其次数及项数为：

| 原行 | (deg_h,deg_u) | 项数 |
|---|---:|---:|
| R（Rt） | (8,4) | 27 |
| N（NH） | (10,5) | 50 |
| S（NS） | (14,9) | 129 |
| P（PS） | (16,10) | 155 |

使用完整原 u 次数 4、5 的 Sylvester 结式
$$
C(h)=\operatorname{Res}_u(R,N)
$$
准确为 69 次。完整 QQ 因式分解及乘回给
$$
C\doteq h^{22}(h-2)^{12}(2h-1)^4
(h^2-2h+2)^8(h+1)C_{14}(h), \tag{3}
$$
C14 是单首项 14 次因子。式 (3) 也唯一地定义 C14；不需要选择它的复根或数值近似。全 C 的已执行输入归一 SHA256 为
64ad01d50a2fe5e8352b4b630feb33579b40549133d8d8d46281a1201be6a938。

另一个**完整原**结式
$$
S_N(h)=\operatorname{Res}_u(R,S)
$$
准确为 102 次，在 QQ[h] 中 gcd(C14,SN)=1。所附自含源由扩展 Euclid 构造 a、b 并乘回
$$
aC_{14}+bS_N=1.
$$
因此整个 C14 纤维排除。没有借模多变量单位来判 QQ 空集，也没有除任何 u 首项。

## 4. H 非零支的全部小因子返回

h=0 已由 ell,u 非零排除。对其余三个有理 h 和整个二次代数
$$
K=\mathbb Q[h]/(h^2-2h+2)
$$
返回 R,N,S,P 的**同一 u**。全部 K 系数逆均由 QQ 多项式扩展 Euclid 得到并乘回；K[u] 中每次多项式除法和扩展组合也乘回。结果是：

| 完整 h 纤维 | 四原行在 K[u] 的单首项共同 gcd | 支付 |
|---|---|---|
| h=−1 | u−1 | 原 u−1 |
| h=1/2 | (u−1)² | 原 u−1，全重数 |
| h=2 | (u−1/4)² | 原 M=u²(4u−1) |
| h²−2h+2=0 | u² | 原 u，全重数 |

这张表同时保留二次因子的两个嵌入，没有把四原行分别在不同根上实现。至此 (3) 的所有因子已回原物理条件排除。

## 5. H=0 支与先行支付 x=u+1

现在 H=0。u≠0 强迫 2u−1≠0，且
$$
\ell=-\frac{u}{2u-1},\quad
M=-\frac{u^3(4u-1)}{(2u-1)^2},\quad
P_{02}=\frac{u(4u-1)(u-1)^2}{2u-1}. \tag{4}
$$
所以 4u−1 也由原 M 非零支付。

在 x=u+1、y=1 上，准确原式为
$$
E_1=-\frac{(u-1)(4u-1)(3u-1)}{2(2u-1)^2}. \tag{5}
$$
由 (4)—(5) 必有 u=1/3、ell=1、x=4/3。这个点仍保留全部 t。直接原返回为
$$
R_t=t(t-4),\qquad
N_H=-\frac{t^2}{9}+\frac t9+\frac{20}{27}.
$$
t=0 和 t=4 分别使 NH 为 20/27、−16/27，均非零。故整个 x=u+1 支已经排除，后面使用 E1 唯一解 t 的分母 x−u−1 是合法的。

## 6. H=0 的原 18 次覆盖与 41 次返回

在余下 x−u−1≠0 上，将 (4)、y=1 代回原 E1，取
$$
t=-[t^0]E_1/[t^1]E_1.
$$
其分母来自原 u、u−1、2u−1、M、P02 以及刚支付的 x−u−1。把这个**同一 t** 返回 Rt、NH、NS、PS，按这些单位准确剥除分子公共因子，得到 R0,N0,S0,P0。这里的 N0 是本节所得多项式名，不是原基点第二梯度。

| 原返回 | (deg_u,deg_x) | 项数 |
|---|---:|---:|
| R0 | (5,4) | 20 |
| N0 | (5,4) | 19 |
| S0 | (12,6) | 70 |
| P0 | (14,6) | 83 |

完整原 x 次数 4、4 给
$$
C_0(u)=\operatorname{Res}_x(R_0,N_0)
\doteq
u^6(2u-1)(4u-1)^2(3u-1)^5
(8u^2-4u+1)(32u^2-16u+1). \tag{6}
$$
这是完整 18 次 QQ 覆盖，原输入归一 SHA256 为
50ff81e5590319df7a7bcb97bd3bf2b329f39a6b15cb8bad9a7eaf82ffc3e360。

完整原加权 N 返回
$$
S_0^{\rm ret}(u)=\operatorname{Res}_x(R_0,S_0)
$$
为 41 次。准确 QQ 扩展 Euclid 的共同 gcd 为
$$
\gcd(C_0,S_0^{\rm ret})
=\operatorname{monic}\{u^6(2u-1)(3u-1)^5\}. \tag{7}
$$
所以 (4) 及原 u 非零支付后，仅余 u=1/3。全部 x 首项退化仍包括在完整 Sylvester 式内。

## 7. 最后 u=1/3 的原有理返回

此时 ell=1、Q=2/3、y=1，但 x、t 暂不改动。直接从同一个 Gram 得
$$
f=x/2-1/3,\quad
\lambda=1/2+3x/4+3t/8,\quad
T=-1/2-3x/4+9t/8,\quad w=3x/2-3t/4,
$$
$$
E_1=-\frac13(x-4/3)(t+6x-4),\qquad
R_t=t(t-2x-4/3). \tag{8}
$$
x=4/3 已由第 5 节排除。因此 t=4−6x，且
$$
R_t=\frac{16}{3}(3x-2)(3x-1).
$$
两个剩余原点如下：

- x=1/3、t=2：lambda=3/2，Pj=4/9，原双线性 Nv=20/27，所以
  $$N_H=20/27-(4(3/2)/3)(4/9)=-4/27\ne0.$$
- x=2/3、t=0：lambda=1、T=−1、f=0、P02=−4/27。原两 singleton 最高值加权和为 4/27，原目标为 −4/27，所以
  $$P_S=8/27\ne0.$$

这些最后返回可直接以 r²=1/3、b=1/2−r、c=1/2+r 计算；不是从结式的抽象根作推断。两点另已在纯 V8 的 BigInt 有理函数/Frobenius 运算中实际返回上述准确常数。H=0 支也排空，结合第 3—4 节即证整个 Q=1−u、y=1 原支为空。

## 8. 源、已执行范围及环境中断记录

自含可重建源：[2026-11-27-unit211-Q1minusU-y1-original-return-8542.py](../notes/2026-11-27-unit211-Q1minusU-y1-original-return-8542.py)。
SHA-256：31a297c6aa002c4ab84c2bdfd907fb5606ac7c0309d1364cbe324890fe162131。该整合源尚未端到端执行，准确依据见下列原子成功与纸面返回。

源重建同一原 Gram，验证 E0/N0/P1、(1)、(2)、全部 69/102 与 18/41 结果式及小整商代数返回，并检查最后原点。它不依赖任何 scratch JSON 或外部数值数据。所有输出只应保存小执行回执与 SHA，不保存大证书。

操作状态须准确区分：

1. 一般原均值源 generic_LS_original_X_quadrics_cubics_8542.py 已实际执行，SHA256 3d0679e3bd29f703b465b5655d0b2040eb613c2cb3d3402b2c03ec2145633d9a，源内约 0.104 秒、exit 0。
2. H≠0 的 69 次完整覆盖源 generic_LS_uplusQminus1_y1_ratio_cover_8542.py 已实际执行，SHA256 a8936aefdff75318ec79505745ea69134d2e2b5679a404f5305fe006842da47a，源内约 0.177 秒、exit 0。随后 102 次原 QQ 返回及四个小域 gcd 已实际完成；完整算式及这些返回在本稿自含源中重新明确给出。
3. H=0 的 18/41 次覆盖源 generic_LS_uplusQminus1_y1_Hzero_cover_8542.py 已实际执行，SHA256 7ca887e358b15d9125e59cde9d7d535e5175f84ef816f9fde20e88a43146a3fe，源内约 0.169 秒、exit 0。
4. 其后终端标为 unavailable；最后计划的本地 u=1/3 gcd 调用未执行，本稿不把它记作成功。第 7 节用完整纸面原返回完成，并在独立于失效终端的纯 V8 小有理运算中准确得到 −4/27 与 8/27。
5. 现附的**整合自含源本身尚未端到端执行**；这是环境中断后的重建文件，不伪称原成功脚本的同一 SHA。上述已经完成的原子 QQ 计算与纸面最后纤维是本证明依据，不把额外整合运行设成数学登记门槛。

本结论只支付 Q=1−u 边界上的 y−1；后续可在余支合法用 Ry 对 t 的系数 u(y−1)，仍须保全部原 mean/N/P、U 矩、LS、同一复嵌入与原物理非零条件。
