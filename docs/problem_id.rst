Problem Identification
======================

.. epigraph::

   Make it work, and then make it work better.

   -- somebody on Reddit


How do I get my team to use [insert tool here]?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Or alternatively, how do I use tool X at work? I want to stress that despite the glamor or appeal that certain tools have, you want to avoid asking yourself the wrong question when it comes to adopting the most hyped-up technologies. The field is abuzz with all sorts of news claiming that X is going to revolutionize business, whether it be data science, machine learning, generative AI, and so on, and so forth.

Yet, what is the problem you are trying to solve here? Is it to first put on the appearance of being innovative, hiring people who claim to know these things and then figuring out how to use them later? Are you trying to solve real problems that your company faces, or are you just trying to pad your resume?

I want to stress that while we live in exciting times, with all sorts of interesting technologies that promise to make our lives easier, that our primary focus is on identifying insurance problems first, and then selecting the appropriate tools to solve them second. Hence, this book will revolve around solving a common problem in insurance and then building a Python package as the tool used to solve it.

Our Representative Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^

Throughout this book, we will be working to solve a common actuarial problem - estimating reserves. Because an in-depth guide of reserving is beyond the scope of this book (we have Friedland for that - insert citation here), we will focus on just a simplified case that can be solved with the well-known chainladder method.

Below is a triangle that you may have already seen if you've taken CAS Exam 5. It's just the Auto BI triangle from XYZ Insurer that you see in the chapter on the development technique in Friedland's paper.

.. list-table:: XYZ Insurer - Auto BI
   :header-rows: 1

   * - Accident Year
     - 12
     - 24
     - 36
     - 48
     - 60
     - 72
     - 84
     - 96
     - 108
     - 120
     - 132
   * - 1998
     -
     -
     - 11,171
     - 12,380
     - 13,216
     - 14,067
     - 14,688
     - 15,366
     - 16,163
     - 15,835
     - 15,822
   * - 1999
     -
     - 13,255
     - 16,405
     - 19,639
     - 22,473
     - 23,764
     - 25,094
     - 24,795
     - 25,071
     - 25,107
     -
   * - 2000
     - 15,676
     - 18,749
     - 21,900
     - 27,144
     - 29,488
     - 34,458
     - 36,949
     - 37,505
     - 37,246
     -
     -
   * - 2001
     - 11,827
     - 16,004
     - 21,022
     - 26,578
     - 34,205
     - 37,136
     - 38,541
     - 38,798
     -
     -
     -
   * - 2002
     - 12,811
     - 20,370
     - 26,656
     - 37,667
     - 44,414
     - 48,701
     - 48,169
     -
     -
     -
     -
   * - 2003
     - 9,651
     - 16,995
     - 30,354
     - 40,594
     - 44,231
     - 44,373
     -
     -
     -
     -
     -
   * - 2004
     - 16,995
     - 40,180
     - 58,866
     - 71,707
     - 70,288
     -
     -
     -
     -
     -
     -
   * - 2005
     - 28,674
     - 47,432
     - 70,340
     - 70,655
     -
     -
     -
     -
     -
     -
     -
   * - 2006
     - 27,066
     - 46,783
     - 48,804
     -
     -
     -
     -
     -
     -
     -
     -
   * - 2007
     - 19,477
     - 31,732
     -
     -
     -
     -
     -
     -
     -
     -
     -
   * - 2008
     - 18,632
     -
     -
     -
     -
     -
     -
     -
     -
     -
     -


Your job as an actuary is to develop these losses, estimate the reserves, and then communicate those results to upper management. Now, what tools do we choose to solve the problem?

Unless you're working at a startup, there's probably already a process in place. Within the actuarial world, you'll find solutions ranging from Excel spreadsheets, to enterprise software, and in-house systems. Each of these approaches has their own trade-offs when it comes to solving the problem. For example, spreadsheets offer a great deal of flexibility, but interface poorly with modern version control systems and are difficult to scale as the business grows. Enterprise software offers immediate functionality, but can be expensive and often times, closed-source. In-house systems have the promise of complete control over the solution, but requires the organization to spend resources to develop and maintain it.

In our scenario, suppose you're working at a small to mid-size carrier, reserving for this one line of business. The reserve studies are done quarterly and saved in a series of Excel files on a shared drive. When the company was small, this approach worked well. The actuaries have made Excel templates out of the main actuarial methods used by the department - Chain Ladder, Cape Cod, and Bornhuetter-Ferguson. Each quarter simply requires an actuary to copy the Excel file contianing last quarter's work, update it with the current quarter's data, and then perform the analysis. Selections are then aggregated and sent to a more senior actuary who then communicates them to executive management. Once IBNR is agreed upon, the numbers are sent to accounting for entry into the general ledger.

However, as the company grows, this approach will no longer be scalable.

Sometimes, it's OK to be old school
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


