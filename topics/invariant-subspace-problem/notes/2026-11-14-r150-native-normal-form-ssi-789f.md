# R150 continuation：同一完整正常形的 SSI 线性导入

作者：normal_annihilator / 789f。2026-11-14 UTC。

状态：**完整 2195 来源、九目标的正常形已成功导入 Singular。** 不重新计算正常形；同一二进制系数转换用时 16.729 秒，完整读入在 60 秒、1 GiB 上限内用时 4.575 秒。原商模标准基和共同分母仍未计算。

## 1. 被消除的解释器输入瓶颈

[原生正常形稿](2026-11-14-r150-native-normal-forms-789f.md)已完成全部来源，输出文本约 198 MB。该文本每列是长向量表达式；根的实际 60 秒、1 GiB 读入探测没有到达完成 marker。

新入口直接读取已经完成的 `nf-normal-forms.bin`，不再进入原方程生成、预基或正常形计算。其输入哈希为

```text
eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840
```

辅助程序是 [SSI 转换器](2026-11-14-r150-native-normal-form-ssi-789f.py)。完整实际回执见 [SSI receipt](2026-11-14-r150-native-normal-form-ssi-receipt-789f.json)。

## 2. 格式来自准确原实现，并在当前运行时自举

本机 4.4.0 手册的 `Ssi file links` 条目明确建议大数据使用 SSI 文件链接。准确格式另对照 [Singular 4.4.0 原源码](https://github.com/Singular/Singular/blob/Release-4-4-0/Singular/links/ssiLink.cc) 中的 `ssiWritePoly_R`、`ssiWriteIdeal_R`、`ssiReadPoly_R` 和 `ssiRead1` 的类型 10 分支。

在这里的 $\mathbf F_{31}[s]$ 中，一条向量由“非零项数”及逐项的“系数、分量、$s$ 指数”组成。模外层另保留自由秩与列数。读取器逐项建立链表，不需要对一个长向量表达式重复做加法。

转换器**不硬编码本地版本头或环头**。每次运行都让所指定的当前 Singular 写出一个很小的实际 SSI fixture：环为 `31,s,(c,dp)`，包含系数 30、16 等以及第 1034 分量。程序核验该 fixture 的全部模与项 token，确认系数表示、分量/指数布局和列数接口，再取它实际输出的版本、选项及环头。这样本地与 Actions 的 Singular 可不同；不支持的运行时格式会明确失败。

SSI 读取器不会替向量重新排序。转换器因此严格按 `(c,dp)` 要求输出：分量递增，同一分量内参数指数递减。它逐项检查系数属于 $1,\ldots,30$、同分量多项式末项非零、所有分量次序严格递增，并验证二进制原来源号/目标号与完整 mapping 一致。

## 3. 全量实际结果

本次转换覆盖全部 2195 原来源和九目标，1034 个自由分量，准确共 **26372227 个非零标量系数**，最大参数次数 45。未改写、删去或近似任何系数。

SSI 文件为 243366923 字节，SHA-256 为

```text
41f951f32e0715c5f98fb5c1ff8b969894977a815d764a32e07b29e230c192d2
```

这个文本系数流虽然比旧表达式文件大，但它绕开了表达式求值中的长向量相加。

完整读入探测实际返回：

```text
SSI_REDUCED_LOADED
SSI_NATIVE_ROWS=1034
SSI_NATIVE_COLUMNS=2195
SSI_TARGET_COLUMNS=9
SSI_NATIVE_INPUT_LOADED
```

退出码 0，无 Singular 错误。4.575 秒是完整导入及维数检查的实测墙钟时间；1 GiB 是地址空间上限，不写成峰值 RSS。

## 4. 精确接入与保留的限制

在同一 `ring R=31,s,(c,dp)` 中，若 `Reduced`、`Target` 已声明，入口是：

```text
link nativeInput="ssi:r /absolute/path/normal-forms.ssi";
Reduced=read(nativeInput);
Target=read(nativeInput);
close(nativeInput);
option(redSB);
```

SSI 会恢复文件头记录的选项字，所以需要的计算选项应在导入后重设。维数检查直接使用 `nrows(Reduced)`、`ncols(Reduced)` 等接口；无需为了查看维数把整个大模再次转换成矩阵。

完整来源编号仍由原 `normal-form-mapping.json` 支付。SSI 回执包含该 mapping 的哈希、所有 2195 个原行号及九个原目标号。接入时应连接三层真实来源：原正常形回执中的二进制哈希、SSI 回执的输入/输出哈希，以及实际使用的 mapping。不能把压缩后的第 $j$ 列当作原 6188 行中的第 $j$ 条。

大 SSI、原正常形及完整轨迹均只放运行临时目录。本稿仅保存短源码、回执、哈希和重建入口。下一实际计算从 `std(Reduced)` 开始；本稿没有计算它，也没有产生共同 annihilator、最大子式 gcd 或特征零的原 $I C=T$ 证书。

## 5. 原有限模入口联调与明确CI请求

[根入口实际联调回执](2026-11-14-r150-native-ssi-integrated-load-789f.json)保原6188行构造、全部来源/映射/哈希核对，再以SSI读入；退出0并到达R150_MODULE_NATIVE_INPUT_LOADED。它在std之前停止，没有将导入成功写成annihilator结果。

本次[明确请求](2026-11-14-r150-module-ci-request-789f.json)选择31/annihilator/constant/native-nf-f31+SSI。最终请求另采用[次数优先附录](../results/R150-appendix-parameter-degree-preserving-univariate-module-basis.md)的(dp,c)，保持全部模向量参数次数≤45。原生全NF限120秒/512MiB，按新序SSI转换限120秒/512MiB，余模标准基和annihilator限1800秒/4096MiB。SSI头仍由该运行器当前Singular产生；正常形输入、实际来源映射、全部小回执先保存，长计算之后按真实状态回存。标准基本身也以SSI流式输出，最终压缩/哈希采用流式处理。

这是新的直接余模任务；原43583257344的30分钟reduce未被重跑。发出请求时尚未有本次run号或计算结论，运行号由实际Actions状态登记。
