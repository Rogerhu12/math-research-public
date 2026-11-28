# 同一个原分母的完整 Hermite 返回与配对坐标复用

会话：Astra-rank2-Sha-0b097461-20261127；2026-11-28 UTC。

## 1. 原输入及此次改动的范围

[v13真实终日志](2026-11-28-v13-terminal-and-whole-denominator-return.md)表明原A0 y0的分母乘法矩阵MD第一次全Popov只耗28.729秒，但逐列重置整tail累计超过四千万次行加法，限时前未完成。这里只替换同一个原完整配对图的两个实现调用；目标矩阵、全行模、非约化厚度及其后全部数学门不变。

新helper只绑定original_triangular_artinian_values.complete_paired_fraction_graph的模块引用；只有完整标签 original A0 y0: complete zero/pole graph 和 original A1 y0: complete zero/pole graph 进入新函数。两原engine方法、完整preimage、一般division/Hermite API、scalar-primary绑定均不改。其它标签包括 original first factor yF: complete zero/pole graph 仍执行原函数。原生产F_y门确实要求真实MD转置附加HNF回执；这份门完整保留，不能用新方法的字典冒充它已执行。

## 2. 已有整图证明在同一次 H/U 返回下的实现

保持原多项式环R=k[t]、完整非奇异方阵MD与MN。调用固定Sage10.6的官方reversed_hermite_form，并要求实际返回整多项式变换。令J为反序矩阵；对B=J·MD·J执行官方方法得B'=V·B，再准确反序：
$$
H=J B'J,\qquad U=J VJ,\qquad H=U\,MD.
$$
官方原实现仅用交换、完整Bezout两行变换及非零常数归一。两行Bezout块的行列式为1，所以均为整环上的可逆行操作。源码不复制、不修改；当前固定镜像中的实际扩展文件hash进入回执。若镜像有同目录pyx，也逐字核其已读官方SHA256。

程序还在原R中实际核全部U·MD=H、首一上Hermite、每个非零对角以及原MD全部行对H的动态全余数为零。前一恒等式给row(H)包含于row(MD)，后一个完整余数返回给反向包含，故H是同一完整行模的唯一首一Hermite基；determinant与商长度由全部对角乘积/次数确定。没有用determinant相同代替行模相等。

若原MD全部系数实际落在该二次常数域自己的素子域，沿原完整_entire_prime_subfield_inputs逐项核后下降。H和U的每个系数再经同一嵌入返回原环，并在原环执行上述完整恒等式；不丢任何原行、变量或系数。非素域MD完整留在原域，不强行投影或选特征分量。

原R942的完整三角preimage不改：
$$
\operatorname{row}(Y)=\{y\in R^n:yMN\in\operatorname{row}(H)\}.
$$
在同一graph调用中，令W=Y·MN，以当前已绑定的原_whole_hermite_coordinates返回全矩阵C，实际核
$$
C H=W,\qquad X=C U,\qquad X MD=Y MN.
$$
因此(X,Y)生成完整图。确切地，任意(x,y)满足xMD=yMN时，y=aY；于是(x−aX)MD=0。MD非奇异给x=aX。这同时保全部source坐标，并证明X是给定Y的唯一整解，与原full_polynomial_left_division返回的全矩阵相同。没有分式核、清分母、缩行或reduced support替代。

H、U及不可变MD快照只属于本次session；division要求原MD对象身份、逐项相等及实际hash都不变。全部乘法和全余数实际执行后即释放session；audit只留标识与完整回执hash。原native完整表示的临时缓存政策不变，不跨graph复用数学解。

## 3. 两个可逆调用点与诚实回执

prepare_source_bindings读取已pin的原complete_paired_fraction_graph正文，只将complete_row_hermite调用改为session.image，将full_polynomial_left_division调用改为session.divide。两次逆替须逐字恢复原正文；原所有断言和外层receipt字段均保。每次运行再从原函数globals取当前引用，保后来合法安装的native/preimage/generic wrapper。

image仍返回H,None,receipt，原attached is None断言不改。新division回执明确method为同一H=U·MD、C·H=W、X=C·U，并写reduction=None和old_transposed_attached_hermite_reduction_executed=False；不声称执行旧attached-HNF、旧tail reset、旧操作stream或旧中间次数界。只在两个原direct endpoint使用这一回执，原F_y仍提供真实旧reduction。

这是既有完整多项式图和全坐标返回的实现接续，不新增一个关于rank306实际耗时、原完整几何、通常Sha或无穷p的定理。官方方法可能有大的中间次数和U矩阵；性能由下一实际运行判断，不凭API名称保证。

## 4. 固定公开软件检查

检查仍使用原固定420秒公开workflow、原Sage10.6镜像19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb、四线程、无网络/输出artifact。新kind只加入固定selector的明确白名单和两个SHA；不接受任意路径。生产trigger/原输入未改。

七组比较逐个实际运行未改原graph和新graph，要求全部X/Y逐项相同、零/极完整HNF、det、厚长和余数相同：含非素域二次系数、非平凡U、不可约平方/立方、实际素子域下降、素域输入、公共厚因子、单位分母、零分子及秩一重不可约分母。独立官方matrix.hermite_form也返回同一个全HNF及变换。

十项拒绝覆盖非方阵、奇异分母、附块超范围、非有限常数、同det错误H、错误U、另一MD对象、非整全source、异环source及同对象修改。root静态审查补入ArithmeticError，因为当前原完整坐标返回在非整包含时会以该类拒绝；只补拒绝捕获，算法不变。

真实模块绑定测试执行两个实际endpoint标签，并把旧两调用临时设为拒绝函数，确认新路径未偷用它们；实际F标签则统计原image/division各执行一次且返回旧attached-HNF。另在已PASS scalar-primary v2的原9维fixture上比较完整原primary，核原session/geometry/generic绑定保持。这个检查不执行原生产main，不做rank306性能实验。

输出固定为RANK2_FUNCTION_FIELD_DENOMINATOR_API_RESULT及RANK2_FUNCTION_FIELD_DENOMINATOR_API_SHA256。实际PASS仍须消费；未返回不记PASS。

## 5. 首次提交源码、官方来源与当时同步

官方固定源码：[Sage10.6 function-field Hermite](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/function_field/hermite_form_polynomial.pyx)，git blob cec29e022e3e699d1a3d0b555fbee83647c9fb6c，6979B/SHA256 e5ebac6e452f93aa85657c3c13671dc12468230c3aa975a414c3a1795464b63f。root已全文核实际操作与U返回。[矩阵反序API](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix0.html#sage.matrix.matrix0.Matrix.reverse_rows_and_columns)只用于准确实现上述J操作。

| 本次文件 | 字节数 | SHA256 |
|---|---:|---|
| original_function_field_denominator_return.py | 22715 | 11875739148b591c1b4faf725d13970682bc7e8af6bf613a26e1e55a56fd9242 |
| check-original-function-field-denominator-return.py | 21655 | 266e53526f771bf7746fe97f5a9006a8980cdf8a676c83e01b932ee5f719a013 |
| check-original-complete-quadratic-api.py | 9947 | 3b4d77fef4f76421e0450bd27408549a56a0878d4af8520038dd416f4e9d2f4a |
| original-complete-quadratic-api-request.json | 3041 | fc7c246d0f4f6452eba4a1589efdfb6b77e29d9780fc17a8d47e79411161880d |

固定request2026-11-28-original-function-field-denominator-return-v1，共27源码。推前actual run46073965457/job140875615341：公开2026-11-28 05:17:37 UTC至19f7a05ff66b0bb6038f8eb2237409a17c9b3c6b，私库2026-11-28 05:17:43 UTC至bfe95e2d6be57102eec6a58fcceeecbf976e3e17；四README与05:12已读版同blob，QUEUE本会话认领未变。日志14889B/hash77248820129e31e3a9cce1cc85293f9a9dadb2b239f76afa483116818414e7f5；库存3190blobs/45271839B/tree1629553fc4ad39f90ee6cba49e5a9bd59d41eb25，无>5MB，三旧必要gzip未变。只保脚本、参数、run/hash与必要原输入，不存可重算日志/矩阵。


## 6. v1 的真实软件失败与 v2 私有工作矩阵

[公开run46111621787](https://github.com/Rogerhu12/math-research-public/actions/runs/46111621787)/job140876205973，source80bf30b3ea0382e8ee0871ce7f57d286aa37630b，于2026-11-28 05:20:55 UTC在首个非素域fixture的新image入口失败。固定selector、源码hash、官方库元数据/版本与native准备已通过；reversed_input.reverse_rows_and_columns()实际抛ValueError：matrix is immutable。完整日志25225B/hash4f9ba0e727e98074d36e26d81b813be6d259559aff6c94678d174f0902778fe4，不入仓。没有新HNF完整返回或软件PASS。

原因是Sage的同环matrix(R,M)构造在此保留不可变状态，不能把它当私有可变副本。v2显式使用copy(rows)作独立快照，核对象不同后只冻结该快照；work、reversed_input、H_native、U_native和同环返回均用copy。反序前明确核私有工作矩阵可变。原算术、官方算法、每项U/余数/HNF/CH/XMD门完全不改。

checker的输入快照、故意不同对象及可变修改用例也改用copy，并在每次新graph调用前后核输入mutability不变。七组比较、十拒绝、原F路径及scalar兼容全部继续，未删除失败用例。v2仍27源/420秒固定公开请求，未回执不记PASS。

| v2 文件 | 字节数 | SHA256 |
|---|---:|---|
| original_function_field_denominator_return.py | 22771 | 0a1b6232348067cf9deb49498d97f9d32a0213dc3ef12d882d83ae35f00df5c4 |
| check-original-function-field-denominator-return.py | 21827 | 07b8e39757e998a91b64c2114253ec6072ebdb19ab53aeed58b3dea625c090eb |
| check-original-complete-quadratic-api.py | 9947 | d1a02a57c7be6acb3108fae9f788de6038dd557fc91f30d4267c368a11fc25aa |
| original-complete-quadratic-api-request.json | 3680 | 16033ed5cc6575b5ab6b52aab4991abf200cd6530db6d8232e6f332bfb37b8e1 |

request为2026-11-28-original-function-field-denominator-return-v2-private-mutable-workspaces。推前实际双pull run46073965457/job140876684554：公开2026-11-28 05:22:07 UTC至30da3bbaaf7282b565986876be1fdc7d80dece23，私库2026-11-28 05:22:12 UTC至bb579f0f8b3be9c7323c05a94023380ece571046；四README与05:17同blob、QUEUE未变。日志14887B/hash060d958704ee1138cdda80fa818ab63393629d6d4d57a3405b2a399682b846c9；库存3193/45327408B/tree55a0f86ba676e30744afa18fa5f2414e0e9816cd，无>5MB，三旧必要输入不变。原H逐字保于[本次归档](2026-11-28-handoff-before-denominator-workspace-fix.md)。当前无heavy；下一v15所有helper pins同步此真实修补版本后，仍须先消费软件回执。


## 7. v2 真实完整软件回执

同一分母软件v2已实际PASS：sourcee7518e7735b37bd213bab71158dfc4ca306c72aa/run46112089371/job140877645107，2026-11-28 05:26:48 UTC返回；结果5f93581839237c9e532074ffcbd7fe263fdf8270ec6b14ff832311ff0538fefa，完整日志85133B/hashdccc3d14cda880532840f18613a61cd0fc03c2810c5c3ffc79ce2ec559973a96。主体4.589509695999993秒，实际九次新图返回；七组完整X/Y/HNF/厚长/输入状态比较、十拒绝均通过，真实F标签仍走原image/division各一次并保attached-HNF。scalar-primary v2完整对照及当前合法包装器引用保持也通过。root已核全部实际source_file_sha256；27源请求中结果记录26源码，selector另由固定入口核验。没有执行原几何main、rank306性能实验或宣称数学终门。

当前无heavy。下一v15同步helper/producer/request的实际SHA，保两char0 pins、原65源和四交/一般Norm/18×9/九对/all-requested；软件PASS不替代原完整生产结果。
