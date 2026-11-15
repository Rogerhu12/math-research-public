# R150：同选自然 $u$ 第一连接的原整数小入口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15。

状态：本版源码已冻结，未在本地执行或声称完成新数学。首版在实际 run 43679903558 / execution source 44d727dae5beba12177887d624da7cb1ddd8dbbf 的输入阶段因 NumPy 不存在退出，数学仅 0.091968757 秒，未到第一计算阶段、没有新连接结论。本版只移除该依赖并保持根线程已付的线程数一；已有 primitive 历史字节可复用，其余旧绑定下没有完成数学缓存。由既有 Actions 临时会话按下列真实输入运行。默认数学共享上限 $30$ 秒、地址空间 $512$ MiB，无 native 编译；建议外层上限 $65$ 秒，以便失败回执完整写出。除小回执、源码、参数、run 与 SHA 外，不长期保存可重算数据。

## 1. 精确执行合同

源码为 [selected natural first connection](2026-11-15-r150-selected-natural-first-connection-f31-789f.py)，SHA256：

~~~
45991f0744fe8b020170c77a6f99e4b6e3e9433a3f18ca4c0405cdd76132bab6
~~~

在当前临时会话中的命令模板：

~~~sh
python -B {scripts}/2026-11-15-r150-selected-natural-first-connection-f31-789f.py \
  --point-model {selected_model} \
  --selected-model {work}/koszul-exact-sparse-preparation/exact-original-koszul-outside-model.json.gz \
  --unit-profile {work}/seven-original-exact-rational/seven-original-unit-row-profile.json \
  --kernel36 {bockstein_dir}/actual-original-kernel36.bin \
  --projected-input {work}/selected-second-transverse-projection/same-original-second-transverse-integer-input.json.gz \
  --native-model {native_model} \
  --pure-matrices {work}/selected-pure-projection-rank/selected-pure-projection-and-envelope-matrices.json.gz \
  --repo {repo} \
  --historical-ref 8c6304e273e64b0544d3dd58bc0e48a672a87c36 \
  --historical-path topics/invariant-subspace-problem/notes/r150-first-padic-residual-789f/original-primitive-integer-equations.json.gz \
  --out {work}/selected-natural-first-connection-f31 \
  --seconds 30 --memory-mib 512
~~~

`{repo}` 必须替换为已有该历史提交的真实 Git checkout；不是放模型数据的普通目录。若 session context 未提供这个键，由根线程填入实际 checkout 绝对路径。已有 primitive 文件时，可用 `--primitive-equations` 替代 Git 历史读取。可选 `--pure-matrices` 只顺带读取已成 $Q$ 的三个输出行，不改变新第一连接的来源。

运行依赖仅 Python 标准库、python-flint 与已安装 Git，不需要 NumPy。原稀疏整数乘回用 Python 精确整数列表，两个 field 来源组合交给 nmod_mat，完整字节输出逐行检查后写出。程序不安装依赖、不取令牌、不写 Git、不触发任务。

## 2. 输入身份

| 作用 | 字节数 | SHA256 |
| --- | ---: | --- |
| 原 primitive point | 87459 | 97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074 |
| 原完整 $J$ / free36 来源字典 | 814572 | 0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d |
| 原 $I$ / 单位行 profile | 62084 | 43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df |
| 原 kernel36 二进制 | 222788 | c008e57b7a7e80312f8ba292bb24241d53bb59d4c57b2a8d07ec1017b9de0744 |
| 已成 $585$ 原整数输入 | 170401 | eb7e216cceb96ff436b506c2c677f7740269ee9b63ae0b0457c83037c7d4f220 |
| 原 native 参数模型 | 128145 | 291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6 |
| 可选完整物理 $Q$ 的已成小矩阵 | 88134 | 1569efd597d0b6b3e746d6f4180371fd8c25f629a09c0da78d39a8a02850aa42 |
| 原 primitive 参数多项式 gzip | 65159 | 44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe |

primitive 解压后另核 SHA256 `fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3`。历史提交中的目录与原 manifest 已实际读取，manifest blob 为 `49302d78ab8a1fa8e2d1ef727a383715941b31a1`，记载相同完整字节数与 SHA。新运行仍须通过 `git show` 实际取得全部原字节并重新核对，不能用这条文字记录代替成功读取。

Git 读取只捕获到进程内及本次临时目录，凭据沿 session 既有环境，不在脚本或文件落盘。旧数据不作为 API 二进制附件传输，也不重新提交。

## 3. 数学步骤与自然参数

程序先从原整系数参数多项式逐项取

$$
F^h(0):\ N_{\rm lin}=L_{10},\ N_{\rm quad}=Q,\ 
\Gamma_{\rm quad}=G_5,
$$

$$
[u]F^h:\ N_{\rm lin}=L_9,\ N_{\rm quad}=0,\ 
\Gamma_{\rm quad}=G_4.
$$

$\Gamma$ 的线性部分仍恒零。它核全部 $17\times77=1309$ 个真实常项等式，并把原参数的全部 $4433$ 个系数模 $31$ 与冻结 native 模型逐项核对。

完整原 kernel36 以 `R150BC31`、$31,6188,36$ 解码，核全部非 $J$ 来源为零及原自由块 $I_{36}$。以原 $6188$ 来源和 $4367$ 输出构造全常项、全自然一次乘积；常项必须全部为零。这里直接使用自然系数，不把共动 $P_1$ 当成自然 $A_1$，也不省略来源微分项。

随后只对已成 $954\times585$ 原整数转置矩阵作有限域小消元，不约去可能含 $31$ 的 column content。完整左核 $L$ 必为 $585\times29$，全原来源乘回；三个删行上的 $L_E$ 必秩三，取其完整 $29\times26$ 核 $Z$。$LZ$ 在被删输出上严格为零。

准确同选余空间由十个纯输出与这二十六个配对组成，因而新连接是实际

$$
\beta_I\in\mathbb F_{31}^{36\times36}.
$$

程序保完整矩阵，不只保秩。它也输出完整全输出 selected $49\times36$ 连接；后者不是完整原 $A_0$ 的二十七维余空间。

对 $\beta_I$ 的完整右核，程序回乘旧原 kernel36，保存全部 $6188$ 来源的下一页**常头**以及原自然一次乘积。它尚未解同选 $B_0$ 来源校正，因此不会声称已得到新的整条 $u$ 来源或第二 Schur 系数。

可选的旧 $Q$ 小件用于精确计算被 $I$ 删除的原 $m_6,m_7,m_8$ 三行。物理反序顺序为 $z_2,z_3,z_4$，对应原 $m_8,m_7,m_6$。若三行秩为 $r_E$，已付完整像结构给

$$
\operatorname{rank}_{\mathbb Q}(A_0|_I)=4337+r_E.
$$

程序只报告实际矩阵与秩，不预填 $r_E$。

## 4. 回执、范围及恢复

主回执：`selected-natural-first-connection-f31-receipt.json`。

成功必须 `status=completed`，并保：

- `completeSameSelectedCokernelDimension=36`；
- `all4367ConstantKernelProductsZero=true`；
- `allOriginalNaturalFirstProductsRetained=true`；
- `all36OriginalKernelDirectionsRetained=true`；
- `sameOriginalSelectedSourceSupportVerified=true`；
- `allOriginalSmallCokernelProductsVerified=true`；
- `allOriginalParameterCoefficientsModulo31Verified=true`；
- `all1309ExactPrimitiveConstantCoefficientsVerified=true`；
- `coMovingSourceDerivativeTermDiscarded=false`。

`selectedNaturalFirstConnectionRankModulo31` 是新实际秩；它给特征零同选第一连接的下界，不能自行写成特征零等号。`selectedMinorInfinityOrderModulo31LowerBound=72-rank` 仍只是完整模 $31$ Smith 长度下界。

`nextFirstKernelSourceCorrectionsComputed`、`characteristicZeroSelectedFirstConnectionComputed`、`completeSelectedInfinitySmithLengthComputed`、`leadingUnitProved` 均保持 false。

完整小余空间与全自然乘积在阶段完成后写入临时文件，绑定全部输入字节与源码，不绑定临时目录。相同目录续算可复用这两份完成阶段；任何复用仍核完整小矩阵乘回及绑定。时间耗尽退出 $75$ 并保当前真实 phase；失败退出 $1$ 并留异常文本。所有大数组只在临时会话内存在，永久回执小于 $100000$ 字节。

后继仍须把同选第一连接核的原常头，配上原单位来源的真实 $B_0$ 校正后，才进入下一 $u$ 页。不能仅以常头的余配对为零，代替完整来源运输。
