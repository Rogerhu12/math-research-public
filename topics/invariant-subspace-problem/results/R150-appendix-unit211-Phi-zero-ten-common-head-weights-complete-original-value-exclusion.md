# Phi=0 四头共同零的十权异常分支：完整原值排除

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完成结论

结果
[R150-appendix-unit211-Phi-zero-four-original-quadratic-heads-complete-ten-weight-locus.md](R150-appendix-unit211-Phi-zero-four-original-quadratic-heads-complete-ten-weight-locus.md)
准确分类了四个原二次头同时为零的权点：
$$
F_{10}(u)=0,\qquad Q=-a_9(u),
$$
共十个不同的 $(u,Q)$ 点。

**本次把这十个权点上的全部原值分支一并排除。** 不选择某个数值根，不遗漏任何十次域的复嵌入，也不倒置未付的线性行列式。

因此，在完整原 $\Phi=0$ 解集上，四个真实二次头没有共同零点。四个原头的非零开图形成完整覆盖，每个图中的原均值/N1 商仍至多由 $1,T,z$ 生成。这个结论不意味着第一个头全局为单位；第一个头为零的整条权曲线必须继续由其他头覆盖，不能把它缩成已经排除的十点。

## 2. 同一个真实十次常数域

令
$$
K=\mathbb Q[u]/(F_{10}),
$$
并使用上一结果明给的 $Q=-a_9(u)$。完整整数 $F_{10}$ 与有理 $a_9$ 直接从已保存精确 JSON 读入，文件 SHA256 固定为
0181016263cc74ceee904cc5d9c29baf77e5541f2a6535e1c34dfd89a83a619f。

在 K 中恢复
$$
\ell=1-\frac{2(u-1)(u-2)}Q,\qquad
m=u-\ell,\qquad
bc=\frac{\ell(2u-\ell Q)-u^2}{4(1-Q)}.
$$
所有原已付权单位都在此域中非零，每次使用的常数逆均有完整 QQ[u] xgcd 乘回。没有使用代数范数的未付逆。

仍保持同一点的
$$
z=Qt,\qquad f=-P_c/P_f.
$$
在 $K[\lambda,T,z]$ 中直接构造四条真实原二次式
$$
q_R=R_2/(2\rho),\quad q_W=W_4,\quad
q_O=O_8/\rho,\quad q_N=N_1^*.
$$
原紧凑恒等式的规范不变；特别 N1 与未偏振的 $N(V)$ 没有混同。

## 3. 秩二头给出同两条线性方程

源对四式在 $(T^2,Tz,z^2)$ 上的完整 K 矩阵作精确消元。实际秩恰为 2，主元列是 $T^2,Tz$。完整四行变换矩阵乘回原头；再用同一个行变换作用于整个四条原多项式，逐项核回所有系数。

两个零二次头的原组合给出同两条仿射线性方程
$$
a_T(\lambda)T+a_z(\lambda)z+a_0(\lambda)=0,
$$
$$
b_T(\lambda)T+b_z(\lambda)z+b_0(\lambda)=0.
$$
其中 $a_T,a_z,b_T,b_z$ 关于 $\lambda$ 至多一次，$a_0,b_0$ 至多二次。令
$$
\Delta=a_Tb_z-a_zb_T,\quad
N_T=a_zb_0-b_za_0,\quad
N_z=b_Ta_0-a_Tb_0.
$$
实际次数为
$$
\deg_\lambda\Delta=2,\qquad
\deg_\lambda N_T=\deg_\lambda N_z=3.
$$
两个完整 Cramer 身份
$$
a_TN_T+a_zN_z=-\Delta a_0,\qquad
b_TN_T+b_zN_z=-\Delta b_0
$$
均已精确乘回。

### 行列式零的整个分支

任何 $\Delta=0$ 的原解必有 $N_T=N_z=0$，这是线性相容性的必要条件，不要求预先假定任一单个系数非零。

源在 $K[\lambda]$ 中计算
$$
\gcd(\Delta,N_T,N_z).
$$
完整 Bézout 与除法均乘回。仅剥除原已付 $\lambda$ 单位后，余 gcd 为非零常数。因此整个 $\Delta=0$ 原分支已排除。这里没有把未付的 $\Delta$ 当作一般单位后跳过其零支。

### 行列式非零的整个分支

在其余原解上，可以合法使用
$$
T=N_T/\Delta,\qquad z=N_z/\Delta.
$$
源将同一有理对代回全部四个原二次式，并按各式的真实总次数乘以 $\Delta^2$。同时也代回原矩条件 $F_6$ 和原 $N(V)$ 条件，按真实总次数乘以 $\Delta^6$。得到同一个 $\lambda$ 上的必要多项式：

| 原来源 | $\lambda$ 次数 |
|---|---:|
| $q_R$ | 6 |
| $q_W$ | 6 |
| $q_O$ | 6 |
| 原 N1 | 6 |
| 原 $F_6$ | 18 |
| 原 $N(V)$ | 19 |

这里没有为了得到低次式而改变来源或另选 $T,z$。源逐项检查与同一 $\Delta$ 及原 $\lambda$ 单位的 gcd；本次实际没有剥掉任何额外因子。

## 4. 一个真实 60 维乘法矩阵排除开图

取六次原 $q_R$ 的清分母余式，记为 $P_R(\lambda)\in K[\lambda]$。它的首项在 K 中非零，源通过 QQ xgcd 完整支付其逆，并将它规范为真正首一的 $\widehat P_R$。

考虑
$$
A=K[\lambda]/(\widehat P_R).
$$
它在 QQ 上的真实维数为 $10\cdot6=60$，使用基
$$
u^i\lambda^j,\qquad 0\le i<10,\quad0\le j<6.
$$
所有规范系数及首项的 QQ 逆在素数 $1009$ 处整。故对这一个固定 QQ 代数中原理想行的模运算，是完整 QQ 乘法和首一除法的真实约化。

源构造了其余五条原多项式的全部 $u^i\lambda^j$ 倍数，共 300 行。实际模秩为 60。更具体地，选中的 60 行全部来自同一个原 $q_W$ 清分母余式 $P_W$ 的倍数
$$
u^i\lambda^j P_W.
$$
因此选中方阵就是 $P_W$ 在这个真实 60 维代数中的完整乘法矩阵。源求出其模逆，并对全部方阵乘积验证等于单位阵。

这使相应固定 QQ 方阵的行列式在 $1009$ 处为单位，特别在 QQ 中非零。故 $P_W$ 在 A 中可逆，即
$$
1\in(P_R,P_W)\subset K[\lambda].
$$
两个同源原六次式没有共同复根，整个 $\Delta\ne0$ 分支被排除。

这一步不依赖把模饱和空性直接提升到 QQ，也不假设模 $F_{10}$ 不可约。完整 60 维矩阵覆盖十次常数域的全部复嵌入。所选原两式已经足够；另行完成的 $F_6$ 与 $N(V)$ 余式不构成新的审核门。个别 NB/PB 不必再加入这个已经排空的分支。

结合上一节的 $\Delta=0$ 完整排除，整个十权原值分支关闭。

## 5. 实际执行及小回执

源：
[2026-11-27-unit211-Phi-zero-ten-weight-same-linear-full-original-values-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-ten-weight-same-linear-full-original-values-input-8542.py)。

- 源 blob：0eeafb8c93e8da7e687a6ed38116362ef6102ab3。
- SHA256：883c60019e692aa3fbfdf19d9ed9ab8ff1b4f214ff6cdc298a70b253bd8e1964。
- 实际 run/job：46035126777 / 140628490310。
- source commit：50145fc4b1ddc6a7976c701ffd8a33ae7b09e508。
- 内层：0.694719790 秒 / 41660 KiB / exit 0。
- stdout：221084 字节，SHA256 bd17a912d0bf7baa3e566cfba9495de68227e7af85cb21d21422154cb7a32359。
- 实际执行前 pull 到 13b0bbd9f7020f05807d23ad1f4c012e7fe1f85b，两份 README blob 无变化。

数学返回在 0.629 秒前完成。检查包括 42 次常数 QQ 逆乘回、36 次 $K[\lambda]$ 除法乘回、14 次 Bézout 乘回、两个完整 Cramer 系数身份、35 次模首一除法以及一个完整 60 阶方阵逆乘积。

选定方阵 SHA256：
fe0b423291f4f2d9e2324c764283ac0eb2a8c8b53f12a6fb1d8b9a2631bca49b。

其完整模逆 SHA256：
54a87dce33e51a3db05d7213f8f147988a20f6037c3530f582969a9b7e1a92b0。

390803 字节的大系数载荷已在原运行中压缩、解压并完整重建验证，SHA256 为
93b68a215bc897bc92dc3e9ae2e6a86a1248da3a8ff561579691555472d04f3b。
本稿小回执只保留该载荷的哈希与字节数，不重复存储 208836 字符的压缩正文。完整可再生源和唯一 2975 字节常数权输入均已固定。

普通不变子空间问题尚未因此完成；后续继续四个真实头开图的完整原值条件。
