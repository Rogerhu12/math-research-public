# 两份二十一查询历史域 manifest 的当前读取关系与固定恢复

作者：ChatGPT /root（AI）；日期：2026-11-16 UTC。

**可信度：已证明，限固定树上的实际扫描、下面明确追踪的原来源／读取关系与条件性容量整理。本说明不执行新的科学计算，也不证明任意动态、外部或未来调用不存在。**

本次仅普通移出两份历史 domain-operator/manifest.json 的 main 副本。两个文件各 575317 B，毛释放 1150634 B；实际净变化扣除本说明和登记文字，由最终真实 pull 后的完整 Git blob size 差记录。原 warm、status、数组、gzip、request、followup、condensed-array-manifest、现用源及所有其它 sibling 均在禁止删除集合。两个候选完整身份见§1；最终删前核对必须满足§8，原审计 success 本身不替代这个条件。

本次是独立的二十一／二十一-lambda27审计。早先两26/28、两25、两24和两22/23整理不能作为本次候选的证据。本文仅保存作者解释、必要来源身份、参数与运行引用；不另存原审计全文、完整扫描地址流、科学数组或原Actions日志。

## 1. 两个候选、原运行与固定全文

固定扫描及恢复提交：570970ec37b734179216dbc688018bbe2252bb49；仓库 root tree bee1fbcbcf5df79b423d422699d86c5ad58b384a，topic tree 82264461b791b3c69607eb2758088008c31a32da。

| 候选 | 完整仓库路径 | bytes | Git blob | SHA-256 |
|---|---|---:|---|---|
| c21 | topics/visible-flex-larger-amplitude/notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/domain-operator/manifest.json | 575317 | 410eea80a032cac0eb1361470902be4fcb2fe521 | b4127e34e3f309d7ed6d96136849d7e224bd1bd30d4fcb37bbd3e26fa94dec20 |
| c21lambda27 | topics/visible-flex-larger-amplitude/notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/domain-operator/manifest.json | 575317 | af4498dda1ca039f2f0aa519730019283405f807 | 7a5464f7f94849f370c0cc7b3caaf2d45dc7f818dc95367950a23bc209db9be6 |

| 候选 | 原run / request | 原source commit | 原request SHA-256 | 原B-model SHA-256 |
|---|---|---|---|---|
| c21 | 43653811809 / 68 | 9ad4c5d56a85ba952d6e9a538c49fbd3aae4fa14 | f050405a73028dd3723a2015f8911863664cedfd64b44b9b295308a4ee0964de | 7e5512fa872b45e87fd88e5a2a0c4857ab8881fef8a2e47b3d78b77075486bcc |
| c21lambda27 | 43656059206 / 70 | ab974f19df95e509346fa15d0cefc037780434fd | 478a9bd116ed46504a9354424191f00fc9061655d9d7ebebc35abeef81cc1fd4 | 23df7023ac5215339c8df134782f00b3381c2ccae5cdf8e158d349201031000d |

两份 schema 都是 captured-twenty-one-query-original-RMS-and-collocation-midpoint-domain-v1。它说明原捕获的有限域模型身份，不能用作本次完整闭面、native、full-DN或连续曲面的接受结论。两个manifest的Git blob、bytes和SHA来自固定Actions工作树中实际全部字节，不是由预设字符串填出的检查结果。

两者原共同父为 actual66/run43651436427、source cf3a8ff94fae3f7009f85047c69db3aeb8eb320a，warm SHA 80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6，status SHA 04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4。原 request68 的 damping 为270，request70为27；二者都从这个原父出发，不能把68的输出当70的父。

原各请求的预算/工作参数为 overall1200 s、candidate600 s、trial reserve90 s、recovery30 s、local working512、dual sweeps200、lsmr200、projection200、原17 trial。共有21种有序query、43008个角行、local B维7101；left-RMS区间466,467,468,469,470,471,472,473,475,477,479,480,481,482，原midpoint区间473,475,477,480,481,482,485。以上是原请求元数据，不是本次重新求值的数值证据。原source中angles4096与operator N2048是不同参数角色，不混写。

两份原导出各列190个payload；固定树中这些190路径均已不在。此次没有删除这380个payload，也不能由这两个清单的恢复声称payload已经恢复。其完整导出路径表身份分别是34732 B / 2b37cb41c186d001a73d0a8f25b37fe0eeec64e8101a78e7048049c5e4abe95b，以及下列c21lambda27实际记录；完整原请求其它未选字段继续存在各自followup文件中。

c21lambda27完整导出路径表身份：{"bytes":36442,"sha256":"5152eadaebce11605afd177450d017a4f2dc15f6e27d29bf0307648888d356a6"}。

## 2. 一次固定只读审计与一次原必要正文恢复

实际只读审计为 [run43911738524](https://github.com/Rogerhu12/math-research-public/actions/runs/43911738524)，job133455143995，attempt1，最终completed/success。行政源head为4b5e6235b107de51a730279d7392c6797cf84876，分支visible-flex-larger-twenty-one-pair-manifest-audit-20261116，workflow .github/workflows/visible-flex-twenty-one-pair-manifest-audit.yml，完整42726 B / 31631b253183cf867e21e4c17d7f6181a823aa284e182ecc975d5b8f5cf1207e。被扫描树始终为§1的570970提交，并非行政源head。

原审计已实际生成一个完整必要body：86739 B / b9def91697717c72157ec8e942cdc7a7b8c829220a2dbc1af957a9765270b8bb，原上限90000 B。为免把原行政脚本echo和整个日志再次送入连接器，另一次只读恢复直接在同一公开仓库Actions读取这个原终态job日志；不重跑扫描，不生成新的候选判断。

恢复为 [run43912555870](https://github.com/Rogerhu12/math-research-public/actions/runs/43912555870)，job133458054977，head9cdc39e2d8a9939e8e4f11c7aa2162ed8ef8a306，最终completed/success；workflow .github/workflows/visible-flex-retention6-original-audit-readback.yml，7933 B / d690622b4782640739f458b8eeaabd0388d49e55dd1054954fc7dbc69a4a043e。它在请求前后绑定原run/head/workflow/attempt/repository/成功终态及具体job，对原logs端点只GET一次，跨主机redirect不携Authorization，不打印signed URL。

该次实际读到的原日志为151535 B / 4a91ea134d92cfa0308aa25e90c22b9b8a8361359485d71613cb397abc972b4b，全部保留在该次Actions临时内存。恢复严格选择唯一原BEGIN/END和identity，去除传输时间戳后，完整body字节及SHA与原identity相等，正文不重新编码。root只对恢复job使用一次终态日志工具，已完整读取该86739B正文；未直接请求原job的连接器日志，没有此前连接器错误，无第二次扫描、候选正文下载、raw入Git或artifact。

两个575317B候选只在这个实际Actions部分克隆中读全。本文作者没有通过connector打开任一个大候选，也没有打开136180B的受保护旧artifact receipt正文。

## 3. 实际扫描覆盖与明确未覆盖项

实际使用blob:none部分克隆和稀疏工作树。Git树枚举为不带-l的完整git ls-tree -r -z --full-tree，原枚举9185602 B / 6c13bd14397df640781da3f15c664686aaedfe5f845b858ea41031e8ae5516fa，56282个tracked blob，topic9588个。未为了容量枚举拉取整个仓库的非选中blob尺寸。

扫描对象按源中明确规则选：普通100644/100755文件，其后缀为.py/.mjs/.js/.json/.yml/.yaml/.hpp/.h/.cpp/.cc/.c/.sh/.toml/.ts/.tsx/.md/.markdown/.rst/.txt/.ini/.cfg/.xml/.html/.css，或明确basename .gitattributes/.gitignore/.gitmodules/COPYING/Dockerfile/LICENSE/Makefile/README，再并入本topic全部.gz。完整选中路径表4937903 B / daaccc77726845ed60353aad8f7d758c2d08d71b6120874582890a2b3c9fedf4。

实际rg不可用，按原已声明标准库替代逐完整byte line、逐全部字面模式扫描，630个实际batch全部完成。当前source/config/input分区31494文件；历史文档分区12382文件；两个候选自引用不作外部consumer。所有本topic77份gzip都解码到EOF，共60078173 decoded B，failed_files空；没有对其科学值做算术。

12327个tracked文件明确未扫描。它们是其它topic的6656个gzip，及未选后缀/二进制：无后缀13、cjs109、csv1、diff47、gp37、jsonl608、lock201、log4521、mix56、npz3、patch8、png1、recipe49、sing4、spec10、ssi1、stop2。未扫完整路径清单身份2462095 B / 16666879e39a2e4db93342fd4a47aaae9b6e4b9484ec1d6017ba585ae34da4c5；未请求这些blob尺寸。非普通模式清单为空。不能把上述未扫描范围写成不存在引用。

历史文档中实际12个文件、26个匹配行。完整匹配文件身份列表2760 B / b913531757661e628c7bf3529d5b86c72317726a5c76537976df6fde4c8c465e；完整地址流5180 B / 2b96d2cc45cec5cc0c3798411535769c2c47cc3d4b0b9da823ef105a662c05be。历史单独地址没有运回，不能用这些摘要证明历史引用不存在。

泛构造模式实际在全部31494当前文件中扫描，277个匹配文件、681个file-pattern对、4074个地址行；完整匹配文件列表66600 B / f2a3ac6ecad3b351ce3a616ee1118b649a38994b04f7c67c3ec819aad754361e，完整地址列表562793 B / 35afa29b3dc44511217eab48c33e37338a8616b6d30bf781fd19e8fe1e74a306。泛模式的单个地址未运回；它不等于277个候选manifest消费者，更不排除计算路径、任意编码、外部或未来读取。

## 4. 当前具体引用的完整边界

高特异字面模式在完整当前分区及全部topic gzip中形成14组、449个匹配行。原必要body保每组完整file identity、每行1-based line、byte start、完整line bytes及每个模式的全部字节occurrence offsets；无line正文和无截短preview。本文只登记全部14组解释与身份，不复制这份可重做的449行地址数据。

| 文件索引 | 本topic相对路径 | 实际匹配行数 | 特异模式索引 | 对本次保留决定的含义 |
|---:|---|---:|---|---|
| 22 | computations/exact_20261115_compare_actual68_70_readback_bytes.py | 3 | 4,12,3,11 | 完整旧68/70回执比较源；读取显式 baseline-readback / changed-readback 目录内的原已完成回执及报告，不从Git候选路径打开manifest。 |
| 23 | computations/root_20261114_read_completed_twenty_one_lambda27_prefix.py | 1 | 11 | 原70完整artifact读者；真实manifest消费者，路径根由固定完整ZIP解压的新RUNNER_TEMP给出，见§5。 |
| 24 | computations/root_20261114_read_completed_twenty_one_prefix.py | 1 | 3 | 原68完整artifact读者；真实manifest消费者，同一固定ZIP/独立临时根合同，见§5。 |
| 25 | notes/2026-11-14-actual68-completed-byte-readback-crosscheck.json | 4 | 4,7 | 历史68原读回crosscheck保留；run及B-model身份引用，不删除其正文。 |
| 26 | notes/2026-11-14-actual68-primary-identity-readback.json | 6 | 4,3 | 历史68主身份读回保留；记录原run及多个warm目录下成员。 |
| 27 | notes/2026-11-14-actual70-primary-identity-readback.json | 8 | 12,11,15 | 历史70主身份读回保留；记录原run、实际目录和B-model。 |
| 28 | notes/2026-11-14-actual72-primary-identity-readback.json | 2 | 3 | 历史72主身份读回保留；其68父warm/status引用不是候选manifest的替代。 |
| 13 | notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/condensed-array-manifest.json | 1 | 7 | 原68 condensed-array-manifest保留；其中真实B-model身份仍需，不把model SHA引用说成无意义。 |
| 29 | notes/public-actions-43655562831-1-receipts/completed-readback-request-identity.json | 2 | 4 | 原68完成读回的request身份保留；原run和目录参数仍有意义。 |
| 18 | notes/public-actions-43656059206-1-condensedqp/_pinned_public_artifact_receipt.json | 415 | 11,14,12 | 原70完整artifact receipt保留；415条目录/manifest SHA/run引用完整存在，136180B原文不经connector打开。 |
| 20 | notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/condensed-array-manifest.json | 1 | 15 | 原70 condensed-array-manifest保留；真实B-model身份保留。 |
| 30 | notes/public-actions-43656584956-1-condensedqp/followup-request-identity.json | 2 | 4 | 原72 followup请求保留；真实68父run引用及全部其他字段保留。 |
| 31 | notes/public-actions-43656584956-1-condensedqp/parent68/restore-identity.json | 1 | 4 | 原72 parent68恢复身份保留；真实run和恢复合同不动。 |
| 32 | notes/public-actions-43657876708-1-receipts/completed-readback-request-identity.json | 2 | 12 | 原70完成读回的request身份保留；原run和目录参数不动。 |

| 文件索引 | 完整bytes | Git blob | SHA-256 |
|---:|---:|---|---|
| 22 | 15025 | c96990e4bce0aa154fdfd820c57cf3b390a88f72 | 4d02c9cc698c7f4f74cc3fe0d311de092ab82c89620f37d995c266079dad82d6 |
| 23 | 49810 | 63a091aa8bd97df0020a51066aab1b22d635c9af | 42fb5d0f97c2cee619e2ac1b7e6ee2b9249ee42a518a23cdc9d4c462e0d3c3fa |
| 24 | 49785 | 04341ba5fc14f38873f7872719704fca702836f4 | 0feeb16e350d06ed03abb93c8ff80dd6e9e10a2703d47135f3c36ee3c289ea3a |
| 25 | 23448 | 3f1738ebdea862e30f23ba6edc8fb12948327fb1 | 4a6bc88a31303a9391597c6b99813493623a8e08b194f2b87a304ad9c028d766 |
| 26 | 25276 | db050d3017eae1abd9695efc189c881e55521234 | a324378ee69db3100778e100b4d3d286497bc32c8bd026d9a5d10e2ab049ba1c |
| 27 | 32239 | 6a7825c4bed5beaa2b6298e71b676906b154cb9e | a33d43d5d70b4994b66c4556e90ce953973e03e7d9935243222c67e98aa86ab5 |
| 28 | 25953 | 98cd15743d93c129926691af822601cab2820b57 | 447ccbde94295caba757e81fd3ddfb6a6bbe412bc0eca11aee8c2e279d492a3c |
| 13 | 74271 | 8cfbf9fde9434fe99628aa51dddf1c07ab8db1d7 | 9ea65330439ea99f65eeb65077d53aad90bc808402b8b9c66092e4573cff91e1 |
| 29 | 2292 | 44da4619a98e13cc9aae948c6f955b16d76e42de | fcd969b8bb298e2a096f735f50de40465ee6a1631fc8e3f3fed4ce9da69fca2a |
| 18 | 136180 | a6245aa1e131795ab0764a5b404887ea4402cc79 | 6e474d58d36d323b671b6684dbf3863a72dd5d4f2b6121de2270541c015252a8 |
| 20 | 77864 | 7fb90fe13780b1a557a755ed5673f4676664df36 | 7bbad0a9a972a7d2eadff3e57920cadac94e072ebf9d778aef3e57f9902c64ad |
| 30 | 21979 | 6dec04878fce0a5a8161360902e16c39b1eb9ca1 | 9954937addf1a71cb144a9f4f249e64df26958ea067456f07b4580a395f1e066 |
| 31 | 685 | 4d429365f0984d7ec74cdba057eefef9b6396b30 | 8dc91eac77a817cf26c515fcf1fd71be056e4b0aa981f07d57899f0f0b9fdb4c |
| 32 | 2346 | 4b9bb8a98e67d7920de9a32281ec93385056ddb1 | a682eb9d9af037a04df877c51439d8b21274174d0ee7809785dfefcf63fcb8e7 |

特别地，index18的415行不是零引用。该旧receipt包含完整提取成员身份和原run/目录/manifest SHA；本次原样保留，不因它是metadata就删除。index13和20确有B-model引用，本次保其condensed-array-manifest，模型身份也不变。index30/31的实际68父输入引用继续保留，不能用“只删manifest”掩盖父warm/status仍须保的责任。

index22三处具体引用在原比较源L31、L32、L104。index23/24各一处WARM_DIR字面引用在L44；它们的真正打开路径由§5追踪。这些具体地址不是根据匹配数量猜出来的调用关系。

## 5. 实际producer和真实artifact读者

原域producer computations/geometry_20261114_twenty_one_query_domain_operator.py 的TwentyOneQueryDomainOperator.export在L456–505：用当前捕获的mesh/Y/RHS/local layout、21个实际typed block和原endpoint factors写全部NPZ，再以self.description()及files写directory/manifest.json；检查输出原本不存在，返回实际manifest SHA和B-model SHA。这是生成输出，不把候选Git路径读为方程输入。没有运行该export来证明本次恢复或重新计算科学量。

原request68完整condensed producer在main和_run_engine按CLI绑定actual66或已完成own-schema warm/status，调用真正完整A/B、原残差和原trial引擎。request70的独立lambda27 producer固定同一actual66父与原参数，只对已绑定旧源作明确damping/metadata变换；它不把request68输出当父。两个collocation observer wrapper使用相应完整producer，读取原明确resume/status/CLI；本次这些源全部保留。

具体数学源的固定实际身份如下。两份原manifest中相应声明均与固定树实际字节相等：

| 本topic来源 | bytes | Git blob | SHA-256 |
|---|---:|---|---|
| computations/geometry_20261114_constrained_collocation.py | 18309 | deb4856235d2d57a7003495a0e15c748be41b9b3 | 70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8 |
| computations/geometry_20261114_hermite_domain_constraints.py | 23762 | 885ff3e6b69c44b2488e24afd11606a52fb42f87 | d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce |
| computations/geometry_20261114_full_angle_domain_direction_probe.py | 27821 | 5ff83a675e97bf5d70f9009e1e937e2ae86ac54b | 794788a17db22189b80d65b7def84f3515ca587ea59ffce96fe8887a071665e8 |
| computations/geometry_20261114_full_dn_augmented.py | 11311 | 05608a21d822a3150d0ac4fba656909f85c33b6d | f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e |
| computations/geometry_20261114_fft_frenet.py | 2143 | a6470e86bceae9c0406751a00793c77d77de2bfd | 973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401 |
| computations/geometry_20261114_r225_free_core_bvp.py | 23914 | 64ad4f0b9ca6b1edb4a46d27ff5f6b87154e3a95 | a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08 |
| computations/geometry_20261114_full_angle_domain_operator.py | 38319 | ce7849914e2abc4eb4a7130d705cd0531243cb24 | af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7 |
| computations/geometry_20261114_twenty_query_domain_operator.py | 32067 | 4ab9e00d6cfbff7f56f318fa54d7cf0140707692 | 16157412cbb4af0d01ade0cb3e373413fda175059186ccf17ef3b1d727d27ce1 |
| computations/geometry_20261114_twenty_one_query_domain_operator.py | 32226 | dacd95feb7cdeb9d8113d261145d8ca86dbd7314 | 0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65 |

为解释原输出路径和原reader，另外读取的五个既有小源码身份如下；只读源码文本，没有import/AST/compile或运行科学：

| 本topic来源 | bytes | Git blob | SHA-256 |
|---|---:|---|---|
| computations/geometry_20261114_twenty_one_query_condensed_warm.py | 41712 | 85ebc374aa6d5a74810c1de77d1e8bc98dd6cfa3 | b7956525ce484c4ed17724c2d84c04b6080688e2d0afc8367c5ba46cbf8626f2 |
| computations/geometry_20261114_twenty_one_query_lambda27_condensed_warm.py | 15297 | 918030085303e5ce45fb7aa32b5c16f1997fc973 | a8dd293b4b10ab45a2e69dd1e3e37a2032e4af3eb4d5f21eefa556277cb0d64c |
| computations/geometry_20261114_twenty_one_query_collocation_observer_warm.py | 16728 | 82ad76af3e750f418355d0f02532e11af5ebaa19 | b99c6e4d40abaf426c189b241b718b8847562e92a7cdb90b6fdb31d6505587de |
| computations/geometry_20261114_twenty_one_query_lambda27_collocation_observer_warm.py | 16764 | 504f057ae57fc7a2a3737b200abb8ac79717a484 | 12437f6887b7fb6a7d5ea91214b95227056238054cd73e6db8c123f2aa49e881 |
| computations/exact_20261114_fetch_pinned_public_artifact.py | 28006 | 8ee390d0c1449a6a532d72158172af278f1c7cf3 | 51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859 |

真实reader index24的fetch_original位于L189–236，index23为L186–233。二者先绑定KERNEL_NAME exact_20261114_fetch_pinned_public_artifact.py及SHA51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859，再按显式run/artifact/id/name/size/SHA/source commit下载原完整ZIP。返回root=args.download_out；readout把directory=root/WARM_DIR；audit_domain再取directory/domain-operator/manifest.json，读原模型的manifest SHA绑定并验证其完整有限块。它们确实需要artifact里面的manifest，本文没有声称所有manifest可丢。

原transport validate_output L349–384强制GITHUB_ACTIONS/本公开仓库/Linux、真实RUNNER_TEMP之下新的绝对目录、无逃逸和symlink、目标尚不存在。main从独立staging验证原ZIP后完整提取，向这个新临时目录发布；不能把已有Git checkout的notes目录当其合法download_out。--repository-root只为source_audit选择源码，不决定上述artifact根。这条真实数据流解释为什么移出Git历史副本不改变这两份当前源码按原CLI的输入：它们仍读原明确ZIP的成员。原artifact是否仍可下载是其当时/将来实际执行的独立事实，本文没有发起新下载或保证永久可用。

index22的read_model读已经完成的readback目录和其中complete_byte_audit_artifact/原QP/model/status副本，比较其中已实际验证的完整身份；不自行重下原大payload，不重新算范数/动作/优化。它保留原B-model引用和数组身份，不能将两份manifest的model SHA差直接称为科学数组差。本次源、回执、warm/status和所有现存数组均保留。

因此已具体追踪的三份源中，两个是独立原artifact manifest读者，一个是完整旧readback消费者；没有一份被错误分类为“无消费者”。本次只移走固定Git副本，并给同一blob恢复点。上述结论不向未扫描/外部调用外推。

## 6. 明确保留的两目录siblings与原输入

| 目录 | 本topic相对文件 | bytes | Git blob | SHA-256 |
|---|---|---:|---|---|
| c21 | notes/public-actions-43653811809-1-condensedqp/T112-config.json | 2161 | 543d8364593985305438dda6a0c89b4b1a9c7ec5 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| c21 | notes/public-actions-43653811809-1-condensedqp/followup-request-identity.json | 19775 | b74dc9f4b5bb0dd954535495036b99d949b9b3cb | d66e762d349a9f38097cfdb748bdc1b8adf2b274d533ab206ee819d681ed1bd2 |
| c21 | notes/public-actions-43653811809-1-condensedqp/parent66/restore-identity.json | 685 | 628447981a29e2e84cf023812eaf6c504a7d8c6a | bedf4b94bb6f6a4fc771f07c561886b1261a903bfb5389e841e170a6abc0a88a |
| c21 | notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/condensed-array-manifest.json | 74271 | 8cfbf9fde9434fe99628aa51dddf1c07ab8db1d7 | 9ea65330439ea99f65eeb65077d53aad90bc808402b8b9c66092e4573cff91e1 |
| c21 | notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/optimization-intent.json.gz | 167568 | 163642881f425f6a5f6ba79b6ccefe224d799269 | dacdac36bdf07e017d38e881fcd04ca2eec7229e90a35a1007eae491f1bb36ea |
| c21lambda27 | notes/public-actions-43656059206-1-condensedqp/T112-config.json | 2161 | 543d8364593985305438dda6a0c89b4b1a9c7ec5 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| c21lambda27 | notes/public-actions-43656059206-1-condensedqp/_pinned_public_artifact_receipt.json | 136180 | a6245aa1e131795ab0764a5b404887ea4402cc79 | 6e474d58d36d323b671b6684dbf3863a72dd5d4f2b6121de2270541c015252a8 |
| c21lambda27 | notes/public-actions-43656059206-1-condensedqp/followup-request-identity.json | 21862 | 193dd7495b3f8b42f226e00871395be6151dfe1f | 09342593c67b6104e771e9cd6e4c7b72bd24b15698b8d355a3088f3c36247727 |
| c21lambda27 | notes/public-actions-43656059206-1-condensedqp/parent66/restore-identity.json | 685 | 628447981a29e2e84cf023812eaf6c504a7d8c6a | bedf4b94bb6f6a4fc771f07c561886b1261a903bfb5389e841e170a6abc0a88a |
| c21lambda27 | notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/condensed-array-manifest.json | 77864 | 7fb90fe13780b1a557a755ed5673f4676664df36 | 7bbad0a9a972a7d2eadff3e57920cadac94e072ebf9d778aef3e57f9902c64ad |
| c21lambda27 | notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/optimization-intent.json.gz | 169119 | 8c8d56fd03b3ce246956c93e7bf77987ec079eb0 | 651cd76c51dd5b6692bf20a95fc074631de7e7745eff9d240605b0d994c839c5 |

除这份明确登记外，其它任何现存同目录metadata、原source/request、warm/status和数组也禁止本次删除。两原followup分别保存完整19775 B / d66e762d349a9f38097cfdb748bdc1b8adf2b274d533ab206ee819d681ed1bd2与21862 B / 09342593c67b6104e771e9cd6e4c7b72bd24b15698b8d355a3088f3c36247727；保所有未在本文重复列出的原字段。

两者共同原输入身份：resume80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6，prepared0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714，accepted source b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff，T112 config01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5，zero anchor e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51。这些是原清单所绑定输入，本文不把SHA当成缺失文件的内容或新的accepted父。

## 7. 可重做的模式和固定恢复

最终变化核对使用下列24个明确字面模式。0–15为两候选高特异项，16–23为泛构造项；每项均搜索完整新变更源正文，不只搜索Git diff片段。

| 索引 | 特异字面值 | 角色 |
|---:|---|---|
| 0 | topics/visible-flex-larger-amplitude/notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/domain-operator/manifest.json | c21:repo_path |
| 1 | notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/domain-operator/manifest.json | c21:topic_relative_path |
| 2 | public-actions-43653811809-1-condensedqp | c21:run_directory |
| 3 | twenty-one-condensed-warm | c21:producer_directory |
| 4 | 43653811809 | c21:run_id |
| 5 | 410eea80a032cac0eb1361470902be4fcb2fe521 | c21:git_blob |
| 6 | b4127e34e3f309d7ed6d96136849d7e224bd1bd30d4fcb37bbd3e26fa94dec20 | c21:manifest_sha256 |
| 7 | 7e5512fa872b45e87fd88e5a2a0c4857ab8881fef8a2e47b3d78b77075486bcc | c21:model_sha256 |
| 8 | topics/visible-flex-larger-amplitude/notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/domain-operator/manifest.json | c21lambda27:repo_path |
| 9 | notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/domain-operator/manifest.json | c21lambda27:topic_relative_path |
| 10 | public-actions-43656059206-1-condensedqp | c21lambda27:run_directory |
| 11 | twenty-one-lambda27-condensed-warm | c21lambda27:producer_directory |
| 12 | 43656059206 | c21lambda27:run_id |
| 13 | af4498dda1ca039f2f0aa519730019283405f807 | c21lambda27:git_blob |
| 14 | 7a5464f7f94849f370c0cc7b3caaf2d45dc7f818dc95367950a23bc209db9be6 | c21lambda27:manifest_sha256 |
| 15 | 23df7023ac5215339c8df134782f00b3381c2ccae5cdf8e158d349201031000d | c21lambda27:model_sha256 |

| 索引 | 泛构造字面值 |
|---:|---|
| 16 | domain-operator |
| 17 | domain_operator |
| 18 | condensed-array-manifest |
| 19 | optimization-intent |
| 20 | captured-twenty-one-query-original-RMS-and-collocation-midpoint-domain-v1 |
| 21 | geometry_20261114_full_angle_domain_operator |
| 22 | geometry_20261114_twenty_query_domain_operator |
| 23 | geometry_20261114_twenty_one_query_domain_operator |

### c21

固定全文：[topics/visible-flex-larger-amplitude/notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/570970ec37b734179216dbc688018bbe2252bb49/topics/visible-flex-larger-amplitude/notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/domain-operator/manifest.json)。

~~~sh
git show 570970ec37b734179216dbc688018bbe2252bb49:topics/visible-flex-larger-amplitude/notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/domain-operator/manifest.json > topics/visible-flex-larger-amplitude/notes/public-actions-43653811809-1-condensedqp/twenty-one-condensed-warm/domain-operator/manifest.json
~~~

预期完整 575317 B，Git blob 410eea80a032cac0eb1361470902be4fcb2fe521，SHA-256 b4127e34e3f309d7ed6d96136849d7e224bd1bd30d4fcb37bbd3e26fa94dec20。命令只是未来按需恢复说明，本次未执行。

### c21lambda27

固定全文：[topics/visible-flex-larger-amplitude/notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/570970ec37b734179216dbc688018bbe2252bb49/topics/visible-flex-larger-amplitude/notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/domain-operator/manifest.json)。

~~~sh
git show 570970ec37b734179216dbc688018bbe2252bb49:topics/visible-flex-larger-amplitude/notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/domain-operator/manifest.json > topics/visible-flex-larger-amplitude/notes/public-actions-43656059206-1-condensedqp/twenty-one-lambda27-condensed-warm/domain-operator/manifest.json
~~~

预期完整 575317 B，Git blob af4498dda1ca039f2f0aa519730019283405f807，SHA-256 7a5464f7f94849f370c0cc7b3caaf2d45dc7f818dc95367950a23bc209db9be6。命令只是未来按需恢复说明，本次未执行。

两条恢复命令只恢复同一历史manifest完整字节，不恢复其190个已不在树中的payload，也不重现完整original model、warm或任何数值接受。要实际重算原科学仍须原完整源、原输入、原参数与公开Actions，不能从清单SHA制造数据。

## 8. 最终真实pull变化核对与发布合同

原固定扫描后main仍可变化，因此普通删除的实际publisher须再做真实git pull --rebase，比较根README和本topic README，变化只读diff立即按新规执行，把实际read commit写HANDOFF。随后读取570970固定基线到实际origin/main的全部raw Git变化记录（不启用rename猜测），对每个新增/变更选中source/config/input读完整当前blob并逐24模式扫描；本topic新gzip解码到EOF，历史文档另列完整身份与匹配计数，删除/未扫/错误均明确保留。

具体引用或未选中变化不会自动视作安全。默认RT_REVIEWED_SOURCE_FILES为空；未知当前source命中、未扫变化、读错、gzip错或候选字节变化均阻止此次普通删除。若出现实际新增引用，须读实际源解释并记录精确blob/bytes/SHA及明确模式范围，不能允许整目录或泛schema豁免。这个核对只为两文件容量维护，不是任何科学接受、证明刊发或原计算的新前门。

实际origin/main上的两候选仍须逐个等§1完整blob/bytes/SHA；publisher的proposal相对当前main必须严格等声明路径集合，实际删除集合必须恰好这两个完整路径。其它source/input/warm/status/array/sibling禁止删。本文、HANDOFF/open/results/log登记可写；不得借此改科学源、参数或原接受判据。

容量独立以已实际发布93e41c94d276b57e7f56c140cce2ecc0f5bb50dd的199274214 B为基数，逐全部topic变化Git blob size作加减，包括249及后来实际并发变化，再与原f7基数容量规则共同核对，不把“当前可见文件”算作全部topic。要求实际proposal≤200000000 B，单MD<100000、HANDOFF<10000、open<30000；NFF/cannot-lock必须立即真实pull--rebase，重新核README、全部新增变化和容量后再普通push，禁止force。

最终必要报告保全部变化/完整扫描/实际命中/未扫/错误/候选当前身份/容量差及精确publication集合。仅对九个明确行政记录族使用RT6有序关系：all_changed_paths、source_scans、historical_scans、current_source_matches、reviewed_generic_source_matches、unresolved_current_source_matches、unscanned_changes、candidate_original_main_identities以及topic_capacity.complete_changed_file_deltas。每族完整列顺序/原record索引/常量或逐项值/完整path表/全部未知键和errors保持，给精确逆；不是科学树或候选body的通用压缩。只有整个报告严格更小才选，仍单body90000 B；超过即70、不推送，不截断成“通过”。

本次最终guard作者源14810 B / a5d96dd75fc9b24512c1f724c023b473c22dc33905be360b37211cb762614d51；含原真实pull/rebase/两README/容量/普通push的完整publisher源21963 B / 4f2657a27b68eb3d79f9068bcf934db5e3d93300796b78b693928ffbcdfeddf6。行政workflow只在独立publisher分支，不进入main。原审计和恢复均未授权/执行删除；实际删除与最终run/head/必要body身份以成功publisher原回执登记，不预填未来结果。

## 9. 对正在进行数学工作的含义

这项整理释放保存新作者源与完整证明的空间；不提高原曲面振幅、不改任一求解容差，也不提供新的收敛曲线。原只接受M96/N1024/scalar=.99开放前缀，完整非零112/338/450仍须真实返回。249的准确输入和saved-RHS新调用、250的真实当前DN乘积、252的R583来源桥接、251的解析C1组合都沿各自原输入/唯一时钟/全必要合同继续；本次删除不把任何失败、未访、溢出或旧历史身份改成数学成功。

## 10. 同期request249正式发布和唯一派发事实

R597八件已普通推到main 9e13243d17d5fe736352a9a40b88d75f79b8d744，source commit fcb03198afa577efa9699924b9ac9ca517b179d9，publisher run43914267784/job133464085447。首次push遇NFF后立即实际pull--rebase，规则行冲突只按当前README同步记录解决；实际读过提交e03b9579422962889a7b004ab918ae1ac5e183e1，根README21bd547f56590b7f2dd279d0297efb289a9b2783与题README bff8aea253a9e6a7a4fac28d810ac454c5499fec未变，17:04:20.4906507Z普通push成功。没有force或改写已推历史。

唯一workflow_dispatch于17:04:27.5089427Z返回200，workflow id420380918，实际run43914437629，官方head为9e13243d17d5fe736352a9a40b88d75f79b8d744、compute job133464707666、事件workflow_dispatch。首查前1–6步骤成功，step7临时容量中；这不等于704来源或科学阶段已经完成。结果R598由geometry唯一终态读取，未知派发不自动重试。本记录只登记已发生的正式发布与官方run身份，不增加第二次派发。

## 11. 实际最终核对与普通删除回执

本次实际publisher为run43915008719/job133466671424，行政head bd683bce5b22f8c6f007950a36cd6c999e08cd50，source commit d7bf743371f5a6342e4c3605678609380c7ed910，最终completed/success。17:07:37真实pull读61e488e7f13f52b373dd6f5242434ba30924296f；首次push非快进后立即17:08:36真实pull--rebase，读8c4da60cf03fafcf1ae7468c689bb5ca36adf1d3。两个README在两次pull均未变，实际read commit已写HANDOFF；17:08:40.3509067Z普通推到main c691a3b698e041f6e26b7908fe1c7aad58718497。

两次真正的完整新增变化核对分别为：

| 轮 | 完整必要body bytes / SHA-256 | 具名精确逆后原完整行政对象 bytes / SHA-256 | 全部变化 | 当前源完整扫描 | 历史完整扫描 | 已有其它路径删除 |
|---:|---|---|---:|---:|---:|---:|
| 1 | 56597 / 95ed269c4fe7da9f2454efc26d15ccc0ed828fcb17b381a4adb5d8d098ff9ea6 | 78195 / 7293a2b596496b1068f663fda7ee02e92c3a4710b8bb24626025df20e2533a3c | 117 | 43 | 53 | 21 |
| 2 | 57031 / 458b95b8612442bd4b78cd60fedfdd60fa1bd82cd56851c0ed7c180f4b261319 | 78916 / 97bc3e121f9b3b41a62754310b5698bc7ab87c191ad36d4b5bacac770d17ca50 | 118 | 44 | 53 | 21 |

root已对两份实际必要体按其完整字节/SHA读取，并逐九具名族还原原顺序对象，原完整body identity逐字节相等。两轮current_source_matches、reviewed_generic_source_matches、unresolved_current_source_matches、unscanned_changes和errors均空，allowed=true；没有为通过而加泛源豁免。变化中的21个删除属于扫描基线以后其它既有提交，完整清单已在原报告中；不冒成本次新删21个。

本次实际publication delta只有HANDOFF、log、open、results、本说明新增和§1两个D，精确7路径与声明集合相等。实际两D正是两个固定blob410eea80…/af4498dd…，各575317B/完整SHA均再核相等；其它全部文件禁止删除的合同通过。最终topic198531380B，较本次前199647216B实际净减1115836B，和独立原f7容量guard一致。行政workflow未进main，无force或历史改写。原完整必要体/日志/地址流不另存Git、Release或artifact；这里只保完整来源、参数、执行身份和本次维护结论。
