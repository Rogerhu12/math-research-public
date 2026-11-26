# R150 附录：单位 2+1+1 的相反基点配对与零总单点权支路为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 在同一原单位 $2+1+1$ 与孤立零点分支中，本条排除 $p=1,q=-1,b+c=0$ 的整个纤维。Frobenius 单点权要求 $bc\ne0$，所以本纤维自动有 $u=b-c\ne0$。其他总单点权没有由本条单独排除。

## 1. 保留同一原方程

完全沿用[半总单点权专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-half-total-weight-exclusion.md)第一节的原长度五除子 $2A+B+C+Z$、原六维非退化配对、活跃单位代数和全部值、一阶 jet。这里
$$
a=1,\quad b=u/2,\quad c=-u/2,\quad u\ne0,
\qquad K_B=\begin{pmatrix}
0&0&1&-1\\0&A_1&r&s\\1&r&0&t\\-1&s&t&0
\end{pmatrix}.
$$
仍以原 Frobenius 乘法定义 $D_K,d,f,E,P,N$，并写 $P_0,P_1,P_B,P_C$、$N_0,N_1,N_B,N_C$ 为原值和一阶 jet。

令原零点配对列为 $U$，$m=\tau(U)$。完整临界性要求原孤立零点的 mean 与最高式
$$
\tau(U^2)=2m^2,\qquad P(U)=0.
$$
因此专条已证明的无除法必要条件在本条仍然是
$$
S=\overline P-2\overline N=0,\qquad
c_0=3P_0N_1-2N_0P_1=0,                                      \tag{1.1}
$$
其中 $\overline P=P_0+P_1+(u/2)P_B-(u/2)P_C$，$\overline N$ 同理。这些是同一原最高式、第二梯度和零点 mean 的必要条件；下文只用它们作排除，不主张其充分性。

## 2. 全部 mean 的必要参数图与第一个分母

设 $x=d_B,y=d_C$，定义
$$
X=(x+y)/2,\quad v=x-y-1,\quad T=uX,\quad w=ut,\quad e=u^2\ne0.
$$
原 $E_0=0$ 精确等价于 $f=(X+u)/2$，由此恢复原参数：
$$
r=X+\frac{v-1}{2}+\frac{ut}{2},\quad
s=X+\frac{1-v}{2}-\frac{ut}{2},\quad
A_1=X-uv-\frac{u^2t}{2}.                                      \tag{2.1}
$$
定义
$$
B=v^2+vw-w+1,\qquad D=v-w+1.
$$
原两个单点 mean 的可逆组合为
$$
u^2(E_B+E_C)=-eB,\qquad u(E_B-E_C)=-2D(T-e)-w^2.                \tag{2.2}
$$
所以 $B=0$。先处理 $D=0$：这时 $w=v+1$，因而 $B=2v^2$，迫 $v=0,w=1$；但 (2.2) 第二式此时为 $-1$。故
$$
D\ne0,\qquad T=e-\frac{w^2}{2D}.                              \tag{2.3}
$$
没有丢弃 $D$ 的任何零纤维。

把 (2.3) 代回原 $u^2E_1$、$S/u$ 和 $c_0$，分别得到有理式 $M_0,S_0,C_0$。这些表达式的分母只含非零有理常数、$e,D$。记 $\operatorname{num}$ 为先约去公因子后的分子。由原式精确取余得到
$$
\operatorname{num}(M_0)\bmod B=-w^2(eH-w^2),
\qquad H=5vw-2v+w^2-5w+4.                                    \tag{2.4}
$$

## 3. $w=0$ 与 $H=0$ 纤维均已支付

若 $w=0$，则 $B=v^2+1=0$，而同一原 $S_0$ 的分子取余后是
$$
\left.(\operatorname{num}(S_0)\bmod B)\right|_{w=0}
 =8e(v-1).
$$
由 $e\ne0$ 和 $S=0$ 得 $v=1$，与 $v^2+1=0$ 矛盾。因此 $w\ne0$。

现在原 $E_1=0$ 与 (2.4) 给 $eH=w^2$。若 $H=0$，又迫 $w=0$，已排除。故
$$
H\ne0,\qquad e=\frac{w^2}{H}.                                \tag{3.1}
$$
下文仅使用已付的 $u,e,D,w,H$ 为除数，所有这些量都非零。

## 4. 两个原相容式的精确结式只留下已矛盾纤维

将 (3.1) 代入原 $S_0,C_0$，约去分子分母公因子后取分子，再对 $B$ 关于 $v$ 取余，分别记为 $R_S,R_C$。它们来自原方程，故每个真正原解都满足 $B=R_S=R_C=0$。精确余式为
$$
\begin{aligned}
R_S=-4\big(&4vw^4-15vw^2+12vw-2v\\
          &-4w^4+9w^3-3w^2-4w+2\big),
\end{aligned}                                                   \tag{4.1}
$$
$$
\begin{aligned}
R_C=3w^4\big(&65vw^5+188vw^4-356vw^3-108vw^2+332vw-112v\\
             &+w^6-67w^5-106w^4+668w^3-820w^2+380w-56\big).
\end{aligned}                                                   \tag{4.2}
$$
特征零有理数域上的两个完整结式为
$$
\operatorname{Res}_v(B,R_S)
 =-64(w-1)^4(w^4+4w^3-12w^2+8w-2),                             \tag{4.3}
$$
$$
\operatorname{Res}_v(B,R_C)=-288w^8(w-1)^4Q_8(w),               \tag{4.4}
$$
其中
$$
Q_8=2w^8+14w^7-78w^6-503w^5+402w^4+2112w^3-3750w^2+2282w-490.
$$
两者次数为 $8,20$，精确首一最大公因子为 $(w-1)^4$。于是任何原解都必须 $w=1$。这一步使用的是有限共同根的必要条件；不从结式反向断言存在解，首项系数下降造成的额外根也都保留在这一个最终纤维内。

在 $w=1$ 时，原 $B=v(v+1)$，原已付分母 $D=v\ne0$；而 (4.1) 精确成为 $R_S=4v$，不可能为零。因此最后纤维也被排除，原 $q=-1,b+c=0$ 全支为空。

## 5. 可复算身份与结论范围

配套[自含 QQ 源](../notes/2026-11-26-unit211-opposite-zero-total-weight-347c.py)从原 Frobenius 乘法和原 Gram 重建全部 $E,P,N$ 与 jets，验证 (2.2)–(2.4)、全部分母零纤维、(4.3)、(4.4)、精确 gcd 和最后的 $R_S=4v$ 身份。运行只使用 Python 3.12.14 与 SymPy 1.14.0，无需 FLINT；不保存计算数组。

实际执行命令为 `python 2026-11-26-unit211-opposite-zero-total-weight-347c.py`，exit 0，程序计时 0.883975 秒，峰值 RSS 50152 KiB。源码 SHA256 为 `6981238d8926e9053f54de013f96b09e44d8fe527ae5e98be9b755f48e1571de`。小执行记录由主交接统一登记。

本条在同一原代数参数范围直接排除必要方程，无须替换物理配对、放松 jet 或假定某个原范数非零。它包含该模型允许的无穷远支撑，不据此宣称剩余相反配对权、一般非零基点 mean 或整个 ISP 已解决。
