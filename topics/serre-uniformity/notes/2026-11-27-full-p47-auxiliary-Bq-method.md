# 原 full47 辅助条件 (B) 的精确计算请求

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

**状态：root 与 global_route 已全文逐行纸审方法及代码；本请求尚未执行，不预设两个素数的输出。**

本次只计算原 $X=X_{\rm ns}^+(47)$、$J=\operatorname{Jac}(X)$ 在
$q=283,4513$ 的新输入
$$
(B)_q:\qquad q\nmid\#J(\mathbf F_q).
$$
不重算 R1080 的 $L'$、R1081 的角 Gram 或 $H_t$ 整分解，
也不重跑 R1074/R1086 的同点筛选。

## 1. 原 Jacobian 与完整有理输入

R1067 已证明原 $X$ 在所有 $q\ne47$ 有好约化。R1080 使用的
Chen–de Smit–Edixhoven 同源是定义于 $\mathbf Q$ 的原同源
$$
J\sim_{\mathbf Q}J_0^+(47^2)^{\rm new}.
$$
它给良素数处相同的 Frobenius 特征多项式和有限域点数；
不要求这个同源的次数与 $q$ 互素。
证明可在一个辅助素数 $\ell\ne q$ 的有理 Tate 模上读取：
同源给 $G_{\mathbf Q}$-表示同构，良约化比较给相同 Frobenius 作用。

消费者重建与 R1080 一致的精确有理 modular-symbol 输入
$$
\operatorname{ModularSymbols}(2209,2,\mathrm{sign}=1;\mathbf Q).
$$
先核 ambient/cuspidal/new 维数为 $189,165,157$。
这里 star sign $+1$ 只取每个特征形式的一份，**不是 Fricke 正号**。
在全部 new Hecke 因子上逐个计算真实 $W_{2209}$ 矩阵，
检查它是 $+I$ 或 $-I$，总负号维数为84。
完整正号因子必须恰为维数 $16,24,33$，总和73。
任何缺失因子、不同维数或非标量 Fricke 行都使请求失败。

这一步只重建本次新算子所需的相同精确空间；
不调用旧导数、区间包围、旧整生成元或旧有限点集消费者。

## 2. 两个新 Hecke 算子与群阶判据

对每个 $q\in\{283,4513\}$，在上述三个完整正号因子上计算
实际 $T_q$ 的矩阵，并令
$$
P_{q,i}(X)=\det(X-T_q\mid V_i),\qquad
P_q(X)=\prod_iP_{q,i}(X).
$$
在 $\mathbf Q[X]$ 计算特征多项式后，程序精确转换到
$\mathbf Z[X]$；这一步要求所有分母均为1，不作舍入。
逐个检查多项式首一、degree分别为16、24、33，
乘积首一且degree73。

对一个标准化特征形式及其系数嵌入 $\sigma$，
Eichler–Shimura 关系给良素数 $q$ 的二维 Frobenius 多项式
$$
T^2-\sigma(a_q)T+q.
$$
在 $T=1$ 评价，并对全部73个嵌入相乘，严格得到
$$
\#J(\mathbf F_q)=\prod_iP_{q,i}(q+1)=P_q(q+1).
$$
这里 $P_q$ 是73次的 **Hecke** 特征多项式，
不是146次的 Frobenius 特征多项式；两者通过上述完整乘积关联。
因此
$$
\boxed{\quad
\#J(\mathbf F_q)\equiv P_q(1)\pmod q.
\quad}
$$
程序同时以完整多项式及三个因子的整数值计算 $P_q(q+1)$，
核两者相等、为正，并逐因子与整体核模 $q$ 的
$P_q(q+1)=P_q(1)$。

输出为每因子与整体的精确余数、degree、整数特征多项式 SHA-256，
以及完整整数群阶和其 SHA-256。
没有浮点近似、随机抽样、部分嵌入或只算一个简单因子。

## 3. 真与假的两种合法结果，以及超时范围

若整体余数非零，本次付清相应 $(B)_q$。
若整体余数为零，程序仍正常完成并准确记录
$q\mid\#J(\mathbf F_q)$，即这个辅助素数不满足 $(B)$；
它不是程序错误，也不能把这个结果改写成尚未判断。

每完成一个因子就向 Actions log 输出一条回执，
每完成一个素数的全部三个因子就输出完整认证。
若后一个素数超时，前一个已完成的完整认证继续有效；
未完成素数不凭其部分因子推断条件成立。
异常最终回执保留已完成的因子、完整素数和未完成列表。
外层硬超时前已经写出的日志同样保留；
若硬停止没有最终回执，只按真实已完成条目叙述。

本结果不付 Mordell–Weil 饱和指数、局部对数或高度首项，
不付 R1074 八个原 CM 盘内的唯一性。
两个素数的输出必须在真实执行后分别消费。

## 4. 固定执行、来源与存储

- 只允许本公开仓库 GitHub Actions 执行。
- 新独立脚本：
  [full_p47_auxiliary_Bq_certificate.py](../scripts/full_p47_auxiliary_Bq_certificate.py)。
- 新请求：
  [full-p47-auxiliary-Bq-request.json](full-p47-auxiliary-Bq-request.json)。
- 官方 SageMath 10.6 amd64 image：
  `sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879`。
- 数学预算600秒，预留30秒；consumer在570秒抛出带部分回执的超时。
  外层600秒 TERM、再30秒 KILL；容器拉取不计数学预算。
- 全局 `proof.all(True)`，精确 `new.decomposition()`；
  不向 Sage 10.6 的 QQ kernel 接口传不支持的 `proof` 关键字。
- 只读 checkout；从实际 `.git/HEAD` 及 loose/packed ref 读取提交，
  与 `GITHUB_SHA` 比较，容器不依赖 git 可执行文件。
- 预检请求 SHA、两 README、脚本、方法和原 R1080 来源 SHA。
- 不上传 artifact/Release，不向仓库写可重算矩阵、多项式数组或原始输出。
  后续登记只保存真实 run/job/source、结论和摘要哈希。

## 5. 已消费来源

- [R1080：原完整层47 Jacobian 的无条件秩与准确空间](../results/R1080-certified-full-level47-Jacobian-rank.md)，
  §§1、3：原 Chen 同源、全部 new Fricke 正号因子及真实维数。
- [R1067：原 cuspidal 标签仅在 p 支撑](../results/R1067-original-cuspidal-labels-supported-only-at-p.md)，
  原所有良素数整模型；本次只消费原 $q\ne47$ 好约化。
- B. de Smit, B. Edixhoven, *Sur un résultat d'Imin Chen*,
  Math. Res. Lett. **7** (2000), 147–153，Theorems 1–2；
  [作者全文](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。
- 精确软件接口沿用已成功公开执行的 R1081 同版本、同容器骨架；
  本次唯一新增数学算子是完整 $T_{283}$ 与 $T_{4513}$。
